from django import forms

class Probleme(forms.Form):

	tech = [

		('python', "PYTHON"),
		('java', "JAVA"),
		('shell', "SHELL"),
		('autre', "Autre"),
	]
	titre = forms.CharField(label = "Titre du Probleme")
	description = forms.CharField(label = "Description du probleme", widget = forms.Textarea)
	technologie = forms.MultipleChoiceField(label="Technologie concernees", widget=forms.CheckboxSelectMultiple, choices=tech)
	specifications = forms.CharField(label="Sous technologie")


class Reponse(forms.Form):

	reponse = forms.CharField(label="Reponse", widget=forms.Textarea)