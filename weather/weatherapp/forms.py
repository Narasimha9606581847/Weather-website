from django.forms import ModelForm,TextInput
from .models import city

class cityForms(ModelForm):
    class Meta:
        model=city
        fields=['name']
        widgets={'name':TextInput(attrs={'class':'input','placeholder':'city_name'})}
