from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def model(request):
    return HttpResponse('''<h1>lambhorgini has certain models like 

Urus
Huracan
Aventador
Gallardo
Lamborghini Aventador
Lamborghini Revuelto
Lamborghini LM002
Lamborghini Espada
Lamborghini Huracan EVO
Lamborghini Islero
Lamborghini Jarama
Countach
Huracan Sterrato
Lamborghini Diablo
Lamborghini Jalpa
Lamborghini Urraco
Lamborghini 400GT Monza
Lamborghini 400 GT
Lamborghini Huracan STO
Lamborghini Huracan Tecnica
Lamborghini Miura
Murcielago
Sesto Elemento
Aventador Lp700 4 Bsiv</h1>''')
