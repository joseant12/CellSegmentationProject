from django.http import HttpResponse
from django.shortcuts import render

def login_view(request):
    if request.method == 'POST':
        print(request.POST.get("usuario",""))
    return render(request, 'login_form.html')