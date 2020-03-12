from django.shortcuts import render, redirect


def home(request):
    return render(request, 'aa_application/home.html', context=None)