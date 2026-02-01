from django.shortcuts import render
from .models import Application

def onboarding(request):
    if request.method == "POST":
        Application.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            role=request.POST.get("role")
        )
        return render(request, "partials/success.html")

    return render(request, "onboarding.html")
