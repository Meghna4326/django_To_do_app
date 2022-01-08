from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import*
from .forms import*
def index(request):
    Tasks=Task.objects.all()
    form=Taskform()
    if request.method=="POST":
        form=Taskform(request.POST)
        if form.is_valid():
            form.save()
        return  redirect('/')
    context = {'tasks': Tasks, 'form':form}
    return render(request, 'tasks/list.html',context)

def update(request,pk):
    task=Task.objects.get(id=pk)
    form= Taskform(instance=task)
    if request.method =='POST':
       form= Taskform(request.POST, instance=task)
       if form.is_valid():
            form.save()
            return  redirect('/')
    context={'form': form}
    return render(request,'tasks/update.html',context)


def delete_task(request, pk):
    item=Task.objects.get(id=pk)
    context={'item':item}
    if request.method =='POST':
        item.delete()
        return redirect('/')
    
    return render(request,'tasks/delete_task.html',context)