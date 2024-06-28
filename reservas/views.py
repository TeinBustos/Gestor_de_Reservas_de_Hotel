from django.shortcuts import render, redirect, get_object_or_404
from . import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
        'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'username already exist'
                })
        return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': 'Password do not match'
            })

@login_required
def signout(request):
    logout(request)
    return redirect('index')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm()
        })
    else:
        user = authenticate(
            request, 
            username=request.POST['username'], 
            password=request.POST['password']
        )
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm(),
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('index')

def index(request):
    mensaje = models.Encabezado.objects.first()
    bienvenida = models.Bienvenida.objects.first()
    hoteles_una_estrella = models.HotelesUnaEstrella.objects.all()
    hoteles_dos_estrellas = models.HotelesDosEstrellas.objects.all()
    hoteles_tres_estrellas = models.HotelesTresEstrellas.objects.all()
    hoteles_cuatro_estrellas = models.HotelesCuatroEstrellas.objects.all()
    hoteles_cinco_estrellas = models.HotelesCincoEstrellas.objects.all()
    
    datos = {
        'mensaje':mensaje,
        'bienvenida':bienvenida,
        'hoteles_una_estrella': hoteles_una_estrella,
        'hoteles_dos_estrellas': hoteles_dos_estrellas,
        'hoteles_tres_estrellas': hoteles_tres_estrellas,
        'hoteles_cuatro_estrellas': hoteles_cuatro_estrellas,
        'hoteles_cinco_estrellas': hoteles_cinco_estrellas,
    } 
    return render(request, 'index.html', datos)

def detallesHotel(request, categoria, id):
    model_mapping = {
        'una': models.HotelesUnaEstrella,
        'dos': models.HotelesDosEstrellas,
        'tres': models.HotelesTresEstrellas,
        'cuatro': models.HotelesCuatroEstrellas,
        'cinco': models.HotelesCincoEstrellas
    }

    HotelModel = model_mapping.get(categoria)
    print(categoria)
    if not HotelModel:
        return HttpResponse("Categoría no válida", status=404)

    hotel = get_object_or_404(HotelModel, id=id)
    mensaje = models.Encabezado.objects.first()

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                reserva = form.save(commit=False)
                setattr(reserva, f'hotel_{categoria}_estrella', hotel)
                reserva.user = request.user
                reserva.save()
                return redirect('index')
        return redirect('signin')
    else:
        form = ReservationForm()

    return render(request, 'detallesHotel.html', {'hotel': hotel, 'form': form, 'mensaje': mensaje})


@login_required
def reservations(request):
    mensaje = models.Encabezado.objects.first()
    reservas = models.Reservation.objects.filter(user=request.user)
    return render(request, 'mis_reservas.html', {'reservas': reservas, 'mensaje': mensaje})


@login_required
def edit_reservation(request, id):
    reservation = get_object_or_404(models.Reservation, id=id, user=request.user)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservations')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'edit_reservation.html', {'form': form, 'reservation': reservation})

@login_required
def delete_reservation(request, id):
    reservation = get_object_or_404(models.Reservation, id=id, user=request.user)
    if request.method == 'POST':
        reservation.delete()
        return redirect('reservations')
    return render(request, 'confirm_delete.html', {'reservation': reservation})