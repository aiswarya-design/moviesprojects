from django.shortcuts import render, redirect
from app1.models import Movie


# Create your views here.
def home(request):
    k = Movie.objects.all()
    return render(request, 'home.html', {'movie': k})


def add_movie(request):
    if request.method == "POST":
        t = request.POST['t']
        d = request.POST['d']
        l = request.POST['l']
        y = request.POST['y']
        i = request.FILES['i']

        m = Movie.objects.create(title=t, description=d, language=l, year=y, image=i)
        m.save()
        return home(request)
    return render(request, 'add.html')


def details(request, p):
    k = Movie.objects.get(id=p)
    return render(request, 'details.html', {'movie': k})


def edit(request, p):
    k = Movie.objects.get(id=p)
    if request.method == "POST":
        k.title = request.POST['t']
        k.description = request.POST['d']
        k.language = request.POST['l']
        k.year = request.POST['y']
        if request.FILES.get('i') == "None":
            k.save()
        else:
            k.image = request.FILES.get('i')
        k.save()
        return home(request)

    return render(request, 'edit.html', {'movie': k})


def delete(request, p):
    k = Movie.objects.get(id=p)
    k.delete()
    return home(request)
