from django.shortcuts import render, redirect

from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from datetime import date
from . import forms
from . import models
# Create your views here.

class Probleme:

	@method_decorator(login_required, name='dispatch')
	class PoserProbleme(View):

		form_class = forms.Probleme
		template_name = "forum_etudiant/Probleme/poser.html"
		context = {'form_class': form_class}
		def get(self, request):

			return render(request, self.template_name, self.context)

		def post(self, request):

			self.form_class = self.form_class(request.POST)

			if self.form_class.is_valid():
				print(request.user)
				try:
					user = User.objects.get(username=request.user)					
					probleme = models.Probleme.objects.create(

						titre = self.form_class.cleaned_data['titre'],
						description = self.form_class.cleaned_data['description'],
						user = user
						)

					for tech in self.form_class.cleaned_data['technologie']:
						models.TechnologieProbleme.objects.create(

							technologie = models.Technologie.objects.get(nom = tech),
							probleme = probleme,
							specifications = self.form_class.cleaned_data['specifications']
							)
				except Exception as e:
					raise e
				else:
					return HttpResponse("<h1>Probleme pose</h1>")
				# return HttpResponseRedirect('/success/')

			return render(request, self.template_name, self.context)


	class ListerProbleme(View):

		template_name = "forum_etudiant/Probleme/lister.html"

		def get(self, request):

			try:
				problemes = models.Probleme.objects.all()
			except Exception as e:
				raise e
			else:
				context = {'problemes': problemes}
				return render(request, self.template_name, context)


	class RechercherProbleme(View):

		template_name = "forum_etudiant/Probleme/resultat_recherche.html"

		def post(self, request):

			form = request.POST

			resultat_recherches = models.Probleme.objects.filter(

				Q(titre__icontains=form.get('recherche'))|
				Q(description__icontains=form.get('recherche'))
				)
			context = {'resultat_recherches': resultat_recherches}
			return render(request, self.template_name, context)

	class DetailProbleme(View):

		template_name = "forum_etudiant/Probleme/detail.html"
		def get(self, request, pk):
			try:
				probleme = models.Probleme.objects.get(pk= pk)
				reponses = models.Reponse.objects.filter(probleme=probleme)
			except Exception as e:
				raise e
			else:
				probleme.nbre_vue += 1
				probleme.save()
				if request.user.is_authenticated:
					if User.objects.get(username=request.user) == probleme.user:
						context={'probleme': probleme, 'reponses': reponses, 'is_poseur_probleme': True}
						return render(request, self.template_name, context)

				context={'probleme': probleme, 'reponses': reponses}
				return render(request, self.template_name, context)



class Dashboard:

	@method_decorator(login_required, name='dispatch')
	class MesProblemes(View):

		template_name = "forum_etudiant/Dashboard/mes_problemes.html"

		def get(self, request):

			user = User.objects.get(username = request.user)
			problemes = models.Probleme.objects.filter(user = user)

			context = {'problemes': problemes}

			return render(request, self.template_name, context)

	@method_decorator(login_required, name='dispatch')
	class ModifierProbleme(View):

		template_name = "forum_etudiant/Dashboard/modifier_probleme.html"

		def get(self, request, pk):
			try:
				user = User.objects.get(username = request.user)
				probleme = models.Probleme.objects.get(pk = pk, user = user)
			except Exception as e:
				raise e
			else:
				context = {'probleme': probleme}
				return render(request, self.template_name, context)

		def post(self, request, pk):
			try:
				user = User.objects.get(username = request.user)
				probleme = models.Probleme.objects.get(pk = pk, user = user)
			except Exception as e:
				raise e
			else:
				probleme.description += f"\nMis a jour du :{str(date.today())}\n{request.POST.get('ajouter_lignes_probleme')}"
				probleme.save()
				context = {'probleme': probleme}
				return render(request, self.template_name, context)

	@method_decorator(login_required, name='dispatch')
	class MesReponses(View):

		template_name = "forum_etudiant/Dashboard/mes_reponses.html"

		def get(self, request):

			user = User.objects.get(username = request.user)
			reponses = models.Reponse.objects.filter(user = user)

			context = {'reponses': reponses}

			return render(request, self.template_name, context)


class Reponse:

	@method_decorator(login_required, name='dispatch')
	class DonnerReponse(View):

		def post(self, request, id_probleme):

			user = User.objects.get(username = request.user)
			probleme = models.Probleme.objects.get(pk = id_probleme)
			try:
				models.Reponse.objects.create(
					reponse = request.POST.get('reponse'),
					probleme = probleme,
					user = user
					)
			except Exception as e:
				raise e
			else:
				return redirect('detail_probleme', probleme.id)

	@method_decorator(login_required, name='dispatch')
	class SolutionAuProbleme(View):


		def get(self, request, id_probleme, id_reponse):

			user = User.objects.get(username = request.user)
			try:
				
				reponse = models.Reponse.objects.get(pk = id_reponse)
				probleme = models.Probleme.objects.get(pk = id_probleme, user=user)
				reponse.is_solution = True
				probleme.status = True
				reponse.save()
				probleme.save()
			except Exception as e:
				raise e
			else:
				return redirect('detail_probleme', probleme.id)
	@method_decorator(login_required, name='dispatch')
	class LikerReponse(View):

		def get(self, request, id_probleme, id_reponse):

			try:
				reponse = models.Reponse.objects.get(pk = id_reponse)
				probleme = models.Probleme.objects.get(pk = id_probleme)
			except Exception as e:
				raise e
			else:
				reponse.nbre_like += 1
				reponse.save()
				
				return redirect('detail_probleme', probleme.id)