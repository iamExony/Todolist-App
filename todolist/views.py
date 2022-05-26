from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import todo
from .forms import todoform

def index(request):
    todo_list = todo.objects.order_by('id')
    form = todoform()
    context = {'todo_list': todo_list, 'form' : form}
    return render(request, 'todolist/index.html', context)

#For the add button
@require_POST
def addTodo(request):
    form = todoform(request.POST)

    if form.is_valid():
        new_todo = todo(text=request.POST['text'])
        new_todo.save()

    return redirect('index')

#To enable the link when completed
def completeTodo(request, todo_id):
    Todo = todo.objects.get(pk=todo_id)
    Todo.complete = True
    Todo.save()

    return redirect('index')

#For 'Delete Completed' button
def deleteCompleted(request):
    todo.objects.filter(complete__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    todo.objects.all().delete()
    
    return redirect('index')
