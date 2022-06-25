from django.shortcuts import render, get_object_or_404, redirect

from .forms import MedicForm
from .models import Medic

# Create your views here.

def add_medic(request):
    template_name = 'medics/add_medic.html'
    context = {}
    if request.method == 'POST':
        form = MedicForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('medics:list_medics')
    form = MedicForm
    context['form'] = form
    return render(request, template_name, context)

def list_medics(request):
    template_name = 'medics/list_medics.html'
    medics = Medic.objects.filter()
    context = {
        'medics': medics
    }
    return render(request, template_name, context)

def edit_medic(request, id_medic):
    template_name = 'medics/add_medic.html'
    context = {}
    medic = get_object_or_404(Medic, id=id_medic)
    if request.method == 'POST':
        form = MedicForm(request.POST, instance=medic)
        if form.is_valid():
            form.save()
            return redirect('medics:list_medics')
    form = MedicForm(instance=medic)
    context['form'] = form
    return render(request, template_name, context)

def delete_medic(request, id_medic):
    medic = Medic.objects.get(id=id_medic)
    medic.delete()
    return redirect('medics:list_medics')