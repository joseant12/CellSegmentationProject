from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1> Image home page <h1>")
    my_context = {
        "my_text": "About the author"
    }
    return render(request,"home.html",my_context) 