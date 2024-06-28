from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['nombre', 'correo', 'fechaLlegada']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['nombre', 'correo', 'fechaLlegada']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite su nombre....'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo@gmail.com'}),
            'fechaLlegada': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de llegada', 'type': 'date'}),
        }
        labels = {
            'nombre': 'Nombre',
            'correo': 'Correo electrónico',
            'fechaLlegada': 'Fecha de Llegada'
        }