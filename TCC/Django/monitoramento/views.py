from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from monitoramento.models import Fotografia
from usuarios.models import Perfil
import numpy as np
import pandas as pd
from sklearn.neural_network import MLPRegressor
from django.http import JsonResponse

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    perfil = Perfil.objects.filter(user=request.user).first()
    if perfil:
        categoria_usuario = perfil.categoria

        Fotografia.objects.filter(usuario=request.user, publicada=1).update(publicada=0)

        Fotografia.objects.filter(categoria=categoria_usuario, usuario=request.user).update(publicada=1)

    fotografias = Fotografia.objects.filter(publicada=1, usuario=request.user)
    return render(request, 'monitoramento/index.html', {"cards": fotografias, "usuario": request.user})


def imagem(request, foto_id):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    fotografia = get_object_or_404(Fotografia, pk=foto_id)

    perfil = Perfil.objects.filter(user=request.user).first()
    if perfil and fotografia.categoria == perfil.categoria:
        fotografia.usuario = request.user
        fotografia.save()

    return render(request, 'monitoramento/imagem.html', {"fotografia": fotografia})

def perfil_usuario(request, username):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    usuario = get_object_or_404(User, username=username)
    fotografias = Fotografia.objects.filter(usuario=usuario)

    return render(request, 'monitoramento/perfil_usuario.html', {
        'usuario': usuario,
        'fotografias': fotografias,
})

def execute_prediction(request):
    dataset = pd.read_csv('static/assets/dataset/heart_rate.csv')
    heartbeats = dataset.iloc[:, 0].values 

    def create_sequences(data, seq_length):
        xs = []
        ys = []
        for i in range(len(data) - seq_length):
            x = data[i:i+seq_length]
            y = data[i+seq_length]
            xs.append(x.tolist()) 
            ys.append(y)
        return np.array(xs), np.array(ys)

    seq_length = 10

    X, y = create_sequences(heartbeats, seq_length)

    split_index = int(0.7 * len(X))
    X_train, X_test = X[:split_index], X[split_index:]
    y_train, y_test = y[:split_index], y[split_index:]

    model = MLPRegressor(hidden_layer_sizes=(50,), activation='relu', solver='adam', max_iter=200)

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    predictions = np.round(predictions).astype(int)

    new_heartbeats = np.array([89, 90, 91, 91, 92, 91, 91, 90, 92, 93, 88, 89, 90, 91, 92])
    next_heartbeats = []

    for i in range(10):
        input_seq = new_heartbeats[-seq_length:].reshape(1, -1)
        next_heartbeat = model.predict(input_seq)
        next_heartbeat = np.round(next_heartbeat).astype(int)[0]
        next_heartbeats.append(int(next_heartbeat))
        new_heartbeats = np.append(new_heartbeats, next_heartbeat)

    mean_predicted = int(np.round(np.mean(next_heartbeats)))
    manual_heartbeats = np.array([95, 99, 103, 100, 100, 100, 101, 104, 104, 105])
    mean_manual = int(np.round(np.mean(manual_heartbeats)))

    if mean_predicted > (mean_manual + 5):
        alert_message = "CUIDADO! Seus batimentos cardíacos estão acima do normal."
    elif mean_predicted < (mean_manual - 5):
        alert_message = "CUIDADO! Seus batimentos cardíacos estão abaixo do normal."
    else:
        alert_message = "Os batimentos cardíacos estão dentro do normal, sua saúde está ótima!"

    return JsonResponse({
        'next_heartbeats': next_heartbeats,
        'mean_predicted': mean_predicted,
        'mean_manual': mean_manual,
        'alert_message': alert_message,
    })