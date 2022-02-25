from django.shortcuts import render
from ServicesApp.models import Service 

def services(request):
    services = Service.objects.all()
    return render(request, "services.html", {"services": services})