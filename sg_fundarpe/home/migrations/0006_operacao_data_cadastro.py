# Generated by Django 4.2.11 on 2024-05-16 17:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_projeto_n_empenho_alter_projeto_n_sei'),
    ]

    operations = [
        migrations.AddField(
            model_name='operacao',
            name='data_cadastro',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]