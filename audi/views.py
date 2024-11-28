from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def model(request):
    return HttpResponse('''<h1>audi has certain models like 
                        <img src= "https://imgd.aeplcdn.com/1920x1080/n/cw/ec/51909/a4-exterior-left-front-three-quarter-3.jpeg?q=80&q=80">
Q5 <br>
Audi A6 <br>
Audi e-tron GT <br>
Q7 <br>
Audi A4 <br>
Audi Q8 <br>
Audi Q3 <br>
Audi Q8 E-tron <br>
Audi RS5 <br>
Audi S5 Sportback <br>
R8 <br>
Audi A5 <br>
Audi e-tron <br>
Audi RS Q8 <br>
Audi A8 L <br>
Audi RS7 <br>
Audi Q3 Sportback <br>
Audi Q6 e-tron <br>
Audi Q2 <br>
Audi A6 e-tron <br>
Audi A8 <br>
Q8 <br>
2024 Audi e-tron GT <br>
Audi A7</h1>''')
