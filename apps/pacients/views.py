from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import PacientForm
from .models import Pacient

# Create your views here.

def add_pacient(request):
    template_name = 'pacients/add_pacient.html'
    context = {}
    if request.method == 'POST':
        form = PacientForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('pacients:list_pacients')
    form = PacientForm
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_pacients(request):
    template_name = 'pacients/list_pacients.html'
    pacients = Pacient.objects.filter()
    context = {
        'pacients': pacients
    }
    return render(request, template_name, context)

def edit_pacient(request, id_pacient):
    template_name = 'pacients/add_pacient.html'
    context = {}
    pacient = get_object_or_404(Pacient, id=id_pacient)
    if request.method == 'POST':
        form = PacientForm(request.POST, instance=pacient)
        if form.is_valid():
            form.save()
            return redirect('pacients:list_pacients')
    form = PacientForm(instance=pacient)
    context['form'] = form
    return render(request, template_name, context)

def delete_pacient(request, id_pacient):
    pacient = Pacient.objects.get(id=id_pacient)
    pacient.delete()
    return redirect('pacients:list_pacients')