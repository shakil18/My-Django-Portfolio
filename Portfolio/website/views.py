from django.http import request
from django.shortcuts import render


# get client-ip
def get_client_ip(func):
    def wrapper(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        context = {"client_ip":ip}
        return render(request, 'index.html', context)
    return wrapper

    
@get_client_ip
def index(request):
    return render(request, 'index.html')


