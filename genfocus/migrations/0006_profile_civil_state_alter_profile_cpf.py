# Generated by Django 5.1.2 on 2024-10-25 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genfocus', '0005_profile_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='civil_state',
            field=models.CharField(choices=[('solteiro', 'solteiro'), ('casado', 'casado')], default='solteiro', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cpf',
            field=models.CharField(blank=True, max_length=11),
        ),
    ]
