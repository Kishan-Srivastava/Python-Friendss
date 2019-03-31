from django.shortcuts import render, get_object_or_404, redirect
from first.models import Person
from first.form import Contactform, PersonForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def index(request):
    return render(request, 'index.html')


def details(request, num):
    p = get_object_or_404(Person, id=num)
    return render(request, 'details.html', {'p': p})

def Contact(request):
    form = Contactform(request.POST or None)
    if form.is_valid():
        subject = 'From Django'
        message = 'This is the message that you have typed---\n' + request.POST.get('contact_text')
        from_email = settings.EMAIL_HOST_USER
        user_mail = request.POST.get('contact_email')
        to_list = [user_mail, from_email]
        send_mail(subject, message, from_email, to_list, fail_silently = False)
        return HttpResponseRedirect('success')
    return render(request, 'contact.html', {'form':form})

def success(request):
    return render(request, 'success.html')


def display(request):
    p = Person.objects.all()
    return render(request, 'display.html', {'p':p})


def about(request):
    return render(request, 'about.html')

def join(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PersonForm()
    return render(request, 'join.html', {'form':form })


def landing(request):
    return render(request, 'landing.html')
