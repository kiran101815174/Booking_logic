from django import forms
from django.contrib.admin import widgets         
#input_formats=['%d/%m/%Y %H:%M']
class AvailabilityForm(forms.Form):
    car_no = forms.CharField(required=True)
    time_in = forms.DateTimeField(required=True,input_formats=['%d/%m/%Y %H:%M'])
    time_out = forms.DateTimeField(required=True,input_formats=['%d/%m/%Y %H:%M'])
    

