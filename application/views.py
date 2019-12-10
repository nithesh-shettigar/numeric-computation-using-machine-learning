from django.shortcuts import render

# Create your views here.


def demo(request):
    return render(request,"home.html")

def main(request):
    return render(request,"main.html")