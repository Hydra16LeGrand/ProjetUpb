from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Utilisateur(models.Model):

	choix_filiere = [

		('miage', 'MIAGE'),
		('assri', 'ASSRI'),
		('3ea', '3EA'),
		('sea', 'SEA')
	]
	filiere = models.CharField(max_length=200, choices=choix_filiere, blank=True, null=True)

	user = models.OneToOneField(User, on_delete=models.CASCADE)

# Technologies concernees par un probleme
class Technologie(models.Model):

	nom = models.CharField(max_length=200)
	description = models.CharField(max_length=255, default="Du lourd")

# Fichiers qui seront uploader lors de la creation de probleme

class Probleme(models.Model):

	titre = models.CharField(max_length=200)
	description = models.TextField()
	# status = True si le probleme est resolu False sinon
	status = models.BooleanField(blank=True, default=False)
	date_creation = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	date = models.DateTimeField(auto_now=True)
	# Nombre de fois que le probleme a ete consulte
	nbre_vue = models.PositiveIntegerField(default=0)

	# Les technologies concernees par le probleme
	technologie = models.ManyToManyField(Technologie, through='TechnologieProbleme')
	user = models.ForeignKey(User, on_delete=models.CASCADE)


class TechnologieProbleme(models.Model):

	technologie = models.ForeignKey(Technologie, on_delete=models.CASCADE)
	probleme = models.ForeignKey(Probleme, on_delete=models.CASCADE)
	# specifications des technologies. Ex: django 
	specifications = models.CharField(max_length = 255, blank=True, null=True)
# class Fichier(models.Model):

# 	fichier = models.FileField(upload_to='fichier')
# 	probleme = models.ForeignKey(Probleme, on_delete = models.CASCADE)

class Reponse(models.Model):

	# is_solution = True si la reponse est la solution
	is_solution = models.BooleanField(default=False)
	# le nombre de like pour cette reponse
	nbre_like = models.PositiveIntegerField(default=0)
	date = models.DateTimeField(auto_now_add=True)
	reponse = models.TextField()

	probleme = models.ForeignKey(Probleme, on_delete = models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
