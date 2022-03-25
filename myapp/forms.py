from django import forms

OPTION_CHOICES = [('', 'opções'), ('temperatura', 'temperatura'), ('carga', 'carga'), ('tensão', 'tensão')]

class MyForm(forms.Form):
    option = forms.FloatField(
		required=True,
		widget=forms.Select(choices=OPTION_CHOICES, attrs={'placeholder': 'option'}),
	)
