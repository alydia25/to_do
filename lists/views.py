from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.db.models import F


# Create your views here.

# these are for the tasks
def task_list(request):
    sort_by = request.GET.get('sort', 'created_at')
    sorting_options = {
        'name': 'title',
        'date_created': 'created_at',
        'date_due': F('due_date').asc(nulls_last=True)
    }

    order_field = sorting_options.get(sort_by, 'created_at')
    tasks = Task.objects.all().order_by(order_field)
    
    form = TaskForm()
    return render(request, 'lists/task_list.html', {
        'form': form,
        'tasks': tasks,
        'sort_by': sort_by
    })

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f"{request.META.get('HTTP_REFERER', '/')}?sort={request.GET.get('sort', 'created_at')}")

        else:
            form = TaskForm()
        tasks = Task.objects.all()
        return render(request, 'task_list.html', {'form': form, 'tasks': tasks})
        # title = request.POST.get('title')
        # if title:
        #     Task.objects.create(title=title)
    # return redirect('task_list')

def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('task_list')

def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.toggle_completion()
    return redirect('task_list')

# # this part is for the pomodoro timer
# def start_timer(request):

