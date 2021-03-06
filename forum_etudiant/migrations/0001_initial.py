# Generated by Django 3.1.5 on 2021-04-01 20:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Probleme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('status', models.BooleanField(blank=True, default=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('nbre_vue', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Technologie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(choices=[('python', 'PYTHON'), ('java', 'JAVA'), ('shell', 'SHELL'), ('autre', 'Autre')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filiere', models.CharField(blank=True, choices=[('miage', 'MIAGE'), ('assri', 'ASSRI'), ('3ea', '3EA'), ('sea', 'SEA')], max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TechnologieProbleme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specifications', models.CharField(blank=True, max_length=255, null=True)),
                ('probleme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum_etudiant.probleme')),
                ('technologie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum_etudiant.technologie')),
            ],
        ),
        migrations.CreateModel(
            name='Reponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_solution', models.BooleanField(default=False)),
                ('nbre_like', models.PositiveIntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('probleme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum_etudiant.probleme')),
                ('utilisateur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='forum_etudiant.utilisateur')),
            ],
        ),
        migrations.AddField(
            model_name='probleme',
            name='technologie',
            field=models.ManyToManyField(through='forum_etudiant.TechnologieProbleme', to='forum_etudiant.Technologie'),
        ),
        migrations.AddField(
            model_name='probleme',
            name='utilisateur',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='forum_etudiant.utilisateur'),
        ),
    ]
