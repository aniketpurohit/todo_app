from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Todo
from django.utils import timezone
# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, 'todo/index.html',{"todo_items":todo_items})
@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    Todo.objects.create(added_date = current_date,text=content)
    length_of_todo = Todo.objects.all().count()
    return HttpResponseRedirect('/')

@csrf_exempt
def del_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')
