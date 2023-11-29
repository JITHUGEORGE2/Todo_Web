from django.urls import reverse_lazy
from .models import Tasks
from django.shortcuts import render, redirect
from .form import todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class tasklist (ListView):
    model               = Tasks
    template_name       = 'index.html'
    context_object_name = 'task1'

class taskdetail (DetailView):
    model               = Tasks
    template_name       = 'detail.html'
    context_object_name = 'task'

class taskupdate (UpdateView):
    model               = Tasks
    template_name       = 'update.html'
    context_object_name = 'task'
    fields              = ['name','pri','date']
    def get_success_url(self):
        return reverse_lazy('taskdetail',kwargs={'pk':self.object.id})
    
class taskdelet (DeleteView):
    model               = Tasks
    template_name       = 'delet.html'
    context_object_name = 'task'
    success_url = reverse_lazy('tasklist')







def todoadd(request):
    task1=Tasks.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        pri  = request.POST.get('pri')
        date = request.POST.get('date')
        task = Tasks(name=name, pri=pri,date=date)
        task.save()
    return render(request, 'index.html',{'task1':task1})



##########  Delete  Button #############

def delet (request,taskid):
    task=Tasks.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render (request ,'delet.html')


##########  edit  Button #############
def update(request,id):
    task=Tasks.objects.get(id=id)
    form = todoform(request.POST, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render ( request,'edit.html',{'form':form,'task':task})



# def detail(request):
#     task=Tasks.objects.all()
#     return render(request, 'detail.html',{'task':task})