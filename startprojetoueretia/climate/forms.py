from django.forms import ModelForm
from django import forms
from. models import Forecast

class ForecastForm (ModelForm):
    class Meta:
     model = Forecast
     fields = ['name', 'city', 'coutry', 'temperature', 'description', 'humidity', 'wid']




