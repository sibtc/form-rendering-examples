from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from .forms import ContactForm, ColorfulContactForm

def _form_view(request, template_name='basic.html', form_class=ContactForm):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = form_class()
    return render(request, template_name, {'form': form})


def basic(request):
    return _form_view(request)


def manual(request):
    return _form_view(request, template_name='manual.html')


def field(request):
    return _form_view(request, template_name='field.html')


def attrs(request):
    return _form_view(request, form_class=ColorfulContactForm)


def tweaks(request):
    return _form_view(request, template_name='tweaks.html')


def bootstrap4(request):
    return _form_view(request, template_name='bootstrap4.html')

def user(request):
    return _form_view(request, template_name='user.html', form_class=UserCreationForm)
