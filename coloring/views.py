from django.shortcuts import render

def gallery(request):
    return render(request, 'gallery.html')

def testwrite(request):
    return render(request, 'testwrite.html')

def index(request):
    return render(request, 'index.html')