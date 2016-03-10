from django.shortcuts import render
from .forms import RegistrationForm


def registration_form(request):
    context = {}
    template = 'registration_form.html'
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            template = 'registration_confirm.html'
    else:
        form = RegistrationForm()

    context['form'] = form
    return render(request, template, context)
