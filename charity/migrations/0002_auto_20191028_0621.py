# Generated by Django 2.0.9 on 2019-10-28 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='necessiteux',
            name='health_state',
            field=models.SmallIntegerField(choices=[(0, 'En bonne santé'), (1, 'Malade'), (2, 'Maladie chronique')], default=0, verbose_name='état de santé'),
        ),
        migrations.AddField(
            model_name='necessiteux',
            name='investigated',
            field=models.BooleanField(default=False, verbose_name='investigation effectuée?'),
        ),
        migrations.AddField(
            model_name='necessiteux',
            name='other_infos',
            field=models.TextField(blank=True, null=True, verbose_name='informations supplémentaires'),
        ),
        migrations.AddField(
            model_name='necessiteux',
            name='tel_2',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Téléphone 2'),
        ),
        migrations.AlterField(
            model_name='necessiteux',
            name='appartient_famille',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='charity.Famille', verbose_name='appartient-il à une famille?'),
        ),
        migrations.AlterField(
            model_name='necessiteux',
            name='prenom',
            field=models.CharField(max_length=100, verbose_name='prénom'),
        ),
        migrations.AlterField(
            model_name='necessiteux',
            name='represent_famille',
            field=models.BooleanField(default=False, verbose_name='représente-il une famille?'),
        ),
        migrations.AlterField(
            model_name='necessiteux',
            name='tel',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Téléphone 1'),
        ),
    ]
