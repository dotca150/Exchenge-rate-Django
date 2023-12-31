from django.shortcuts import render


def main(request):
    return render(request, 'main/exchange rate.html')
