from django.shortcuts import render

def gallery(request):
    return render(request, 'coloring/gallery.html')

def testwrite(request):
    return render(request, 'coloring/testwrite.html')

def landing(request):
    return render(request, 'coloring/landing.html')
