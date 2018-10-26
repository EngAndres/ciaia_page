from django import forms
from .models import Attender
from .models import Category

class NewRegister(forms.Form):
	temp = Category.categories.get_categories()
	categories = ()
	categories += (("-1", "Seleccione por favor..."),)

	for category in temp:
		categories += ((category[0], category[1]),)

	category = forms.ChoiceField(label="Categoría de Inscripción", requiered=True, choices=categories)
	
