from django.shortcuts import render, get_object_or_404, redirect

from .forms import ScheduleForm
from .models import Schedule

# Create your views here.

def add_schedule(request):
    template_name = 'schedules/add_schedule.html'
    context = {}
    if request.method == 'POST':
        form = ScheduleForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('schedules:list_schedules')
    form = ScheduleForm()
    context['form'] = form
    return render(request, template_name, context)

def list_schedules(request):
    template_name = 'schedules/list_schedules.html'
    schedules = Schedule.objects.filter()
    context = {
        'schedules': schedules
    }
    return render(request, template_name, context)

def edit_schedule(request, id_schedule):
    template_name = 'schedules/add_schedule.html'
    context ={}
    schedule = get_object_or_404(Schedule, id=id_schedule)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, request.FILES,  instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('schedules:list_schedules')
    form = ScheduleForm(instance=schedule)
    context['form'] = form
    return render(request, template_name, context)

def delete_schedule(request, id_schedule):
    schedule = Schedule.objects.get(id=id_schedule)
    schedule.delete()
    return redirect('schedules:list_schedules')