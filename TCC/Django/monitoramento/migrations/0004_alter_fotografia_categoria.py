# Generated by Django 3.2.25 on 2024-06-22 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoramento', '0003_alter_fotografia_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('HIPERTENSÃO', 'Hipertensão'), ('HIPOTENSÃO', 'Hipotensão'), ('ARRITMIA', 'Arritmia'), ('TAQUICARDIA', 'Taquicardia')], default='', max_length=100),
        ),
    ]
