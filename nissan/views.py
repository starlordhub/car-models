from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def model(request):
    return HttpResponse('''<h1>nissan has certain models like 

Altima
Nissan Magnite
Nissan Leaf
Qashqai
Murano
Nissan Ariya
Nissan GT-R
Nissan Kicks
Sentra
Nissan Sunny
Nissan X-Trail
Juke
Nissan Armada
Nissan Frontier
Nissan Micra
Nissan Rogue
Nissan Terrano
Nissan Titan
Nissan Z
Pathfinder
Armada
Kicks
Nissan e-NV200
Nissan azeal</h1>''')
