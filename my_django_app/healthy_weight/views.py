from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def bmi_calculator(request):
    if request.method == 'POST':
        weight = float(request.POST.get('weight'))
        height = float(request.POST.get('height')) / 100
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2) 
        
        if bmi < 18.5:
            category = "Kurus"
        elif bmi < 24.9:
            category = "Normal"
        elif bmi < 29.9:
            category = "Kegemukan"
        else:
            category = "Obesitas"
        
        context = {
            'bmi': bmi,
            'category': category
        }
        return render(request, 'hasilbmi.html', context)
    return render(request, 'aplikasibmi.html')

def article1(request):
    return render(request, 'article1.html')

def article2(request):
    return render(request, 'article2.html')

def article3(request):
    return render(request, 'article3.html')

def article4(request):
    return render(request, 'article4.html')

def article5(request):
    return render(request, 'article5.html')

# Create your views here.
