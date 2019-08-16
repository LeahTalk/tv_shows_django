from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

def all_shows(request):
    context = {
        'shows': Shows.objects.all()
    }
    return render(request, 'tv_shows_app/index.html', context)

def add_show(request):
    return render(request, 'tv_shows_app/add_show.html')

def edit_show(request, show_id):
    show = Shows.objects.get(id = show_id)
    context = {
        "id" : show_id,
        "title" : show.title,
        "network" : show.network,
        "release_date" : str(show.release_date),
        "desc" : show.desc,
    }
    return render(request, 'tv_shows_app/edit_show.html', context)

def update_show(request, show_id):
    errors = Shows.objects.show_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{show_id}/edit')
    else:
        show = Shows.objects.get(id = show_id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['date']
        show.desc = request.POST['desc']
        show.save()
    return redirect('/shows/' + str(show_id))

def show_details(request, show_id):
    show = Shows.objects.get(id = show_id)
    context = {
        "id" : show_id,
        "title" : show.title,
        "network" : show.network,
        "release_date" : show.release_date,
        "desc" : show.desc,
        "last_updated" : show.updated_at
    }
    return render(request, 'tv_shows_app/show_details.html', context)

def delete_show(request, show_id):
    show = Shows.objects.get(id = show_id)
    show.delete()
    return redirect('/shows')

def create_show(request):
    errors = Shows.objects.show_validator(request.POST)
    if Shows.objects.filter(title=request.POST['title']).exists():
        errors['exists'] = "This show already exists!"
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        Shows.objects.create(title = request.POST['title'], network = request.POST['network'], 
                        release_date = request.POST['date'], desc = request.POST['desc'])
    return redirect('/shows')
