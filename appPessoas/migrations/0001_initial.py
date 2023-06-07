# Generated by Django 4.0.4 on 2023-06-07 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'pessoa',
            },
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.CharField(max_length=100)),
                ('tipo', models.IntegerField(choices=[(1, 'Residencial'), (2, 'Celular')], default=1)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPessoas.pessoa')),
            ],
            options={
                'db_table': 'telefone',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('uf', models.CharField(default='', max_length=5)),
                ('cidade', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=100)),
                ('rua', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=20)),
                ('complemento', models.CharField(max_length=100)),
                ('pessoa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appPessoas.pessoa')),
            ],
            options={
                'db_table': 'endereco',
            },
        ),
    ]
