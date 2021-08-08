from django.shortcuts import render

def gallery(request):
    return render(request, 'coloring/gallery.html')

def preview(request):
    return render(request, 'coloring/preview.html')

def add_story(request):
    return render(request, 'coloring/add_story.html')

def write_summary(request):
    return render(request, 'coloring/write_summary.html')

def view_book(request):
    return render(request, 'coloring/view_book.html')

def testwrite(request):
    return render(request, 'coloring/testwrite.html')

def landing(request):
    return render(request, 'coloring/landing.html')

def genre(request):
    return render(request, 'coloring/genre.html')

def instructions(request):
    return render(request, 'coloring/instructions.html')

def language(request):
    return render(request, 'coloring/language.html')
