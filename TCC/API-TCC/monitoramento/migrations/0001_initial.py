# Generated by Django 3.2.25 on 2024-05-25 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('cpf', models.CharField(max_length=11)),
                ('doenca', models.CharField(max_length=15)),
                ('data_nascimento', models.DateField()),
                ('diagnostico', models.CharField(choices=[('1', 'Bom'), ('2', 'Regular'), ('3', 'Grave')], default='1', max_length=1)),
            ],
        ),
    ]
