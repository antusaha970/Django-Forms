from django.shortcuts import render
from .form import TestForm, TestModelForm
# Create your views here.


def formApi(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = TestForm()
    return render(request, 'formApi.html', {'form': form})


def modelForm(request):
    if request.method == 'POST':
        form = TestModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = TestModelForm()
    return render(request, 'modelForm.html', {'form': form})
