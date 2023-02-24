from django.shortcuts import render
from .forms import personaform

# Create your views here.

def home(request):
    return render(request, 'app/Home.html')


def preguntas(request):
    data={
        'form':personaform()
    }

    if request.method == 'POST':
        formulario = personaform(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Informacion Guardada"
        else:
            data['form'] = formulario

    return render(request, 'app/Preguntas.html', data)