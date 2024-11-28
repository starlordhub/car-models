from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def model(request):
    return HttpResponse('''<h1>nissan has certain models like 

Renault Kiger
Renault Kwid
Renault Triber
Renault Duster
Renault Kardian
Captur
Renault Pulse
Renault Fluence
Renault Duster 2025
Renault Scala
Twingo
Renault Koleos
Renault Bigster
Renault Clio
Renault Lodgy</h1>''')
