from django import forms
from horusmonitorweb.dashboard.models import Machine, AlertConfig

class CreateServer(forms.ModelForm):
    name = forms.CharField(label='Nome',widget=forms.TextInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = Machine
        fields = ['name']
        exclude = ["user"]

class AlertConfig(forms.ModelForm):
	max_warning = forms.DecimalField(label='Máximo Atenção',widget=forms.NumberInput(attrs={'class' : 'form-control','step': '0.1'}))
	max_critical = forms.DecimalField(label='Máximo Critico',widget=forms.NumberInput(attrs={'class' : 'form-control','step': '0.1'}))
	alert_type = forms.IntegerField(label='Tipo de Alerta', widget=forms.Select(attrs={'class' : 'form-control'}, choices=AlertConfig.ALERT_TYPES))
	class Meta:
		model = AlertConfig
		fields = ['max_warning', 'max_critical', 'alert_type']


		