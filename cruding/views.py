from django.shortcuts import render,redirect

# Create your views here.

from django.http import HttpResponse

from . models import *
from . forms import *

def index(request):
    '''
    return HttpResponse('CURSO DE DJANGO 3.0')  
    '''
    crudings = Cruding.objects.all()
    
    form = CrudingForm()

    if request.method == 'POST':
        form = CrudingForm(request.POST)
    
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {'crudings':crudings,'form':form}

    return render(request, 'cruding/list.html', context)

def crudingUpdate(request,pk):
    cruding = Cruding.objects.get(id=pk)
    form = CrudingForm(instance=cruding)
    if request.method == 'POST':
        form = CrudingForm(request.POST, instance=cruding)
    
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {'form': form}
    return render(request, 'cruding/update_task.html', context)

def crudingDelete(request,pk):
    item = Cruding.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect("/")
    
    context = {'item': item}
    return render(request, 'cruding/delete_task.html',context)