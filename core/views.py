from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/index.html', {})

def laboratorio(request):
    return render(request, 'core/laboratorio.html', {})