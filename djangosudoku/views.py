from django.shortcuts import render


def main(request):
    contex = {}
    return render(request, 'main.html', context)
