from django.shortcuts import render



def show_home(request):
    return render(request=request, template_name='home.html')

# Create your views here.
