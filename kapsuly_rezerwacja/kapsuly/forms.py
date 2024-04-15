from django import forms
from kapsuly.models import Kapsula

STANDARD_FORM_CHOICES = [("", "-------")] + Kapsula.STANDARD_CHOICES
POZIOM_FORM_CHOICES = [("", "-------")] + Kapsula.POZIOM_CHOICES
PLEC_FORM_CHOICES = [("", "-------")] + Kapsula.PLEC_CHOICES

class KapsulaForm(forms.ModelForm):
    standard = forms.ChoiceField(choices=STANDARD_FORM_CHOICES, required=False)
    poziom = forms.ChoiceField(choices=POZIOM_FORM_CHOICES, required=False)
    plec = forms.ChoiceField(choices=PLEC_FORM_CHOICES, required=False)

    class Meta:
        model = Kapsula
        fields = ["standard", "poziom", "plec"]



