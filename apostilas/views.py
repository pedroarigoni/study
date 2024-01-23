from django.shortcuts import render


def apostilas(request):
    return render(request, 'apostilas.html')
