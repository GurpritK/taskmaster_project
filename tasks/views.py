from django.shortcuts import render

# Create your views here.

from .models import Task
from .forms import TaskForm


def index(request):
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			form = TaskForm()  # reset form after save
	else:
		form = TaskForm()

	uncompleted_tasks = Task.objects.filter(completed=False).order_by('due_date')
	completed_tasks = Task.objects.filter(completed=True).order_by('due_date')
	return render(
		request,
		'tasks/index.html',
		{
			'form': form,
			'uncompleted_tasks': uncompleted_tasks,
			'completed_tasks': completed_tasks
		}
	)
