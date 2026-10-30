from django.shortcuts import render


def admission_home(request):
    return render(request, 'admissions/admissions.html')