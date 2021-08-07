from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def demo(request):
    return render(request, 'coloring/demo.html')

def new_interaction(request):
    return render(request, 'coloring/new_interaction.html')

def home(request):
    return render(request, 'coloring/home.html')

def drawPad(request):
    return render(request, 'coloring/drawPad.html')

def gallery(request):
    return render(request, 'coloring/gallery.html')

def colorPicker(request):
    return render(request, 'coloring/colorPicker.html')