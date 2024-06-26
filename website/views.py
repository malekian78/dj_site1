from django.http import HttpResponse
from django.shortcuts import render
from .forms import contactForm1,ContactForm2
from website.models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    # return HttpResponse("<h1>Text from view Home</h1>")
    return render(request, 'website/index.html')

def contatct(request):
    if request.method == "POST":
        form = ContactForm2(request.POST)
        print(request.POST)
        # print(form.cleaned_data)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, 'اطلاعات شما با موفقیت دریافت شد')
            form.save()
        else:
            messages.add_message(request, messages.ERROR, 'متاسفانه اطلاعات شما دریافت نشد')
    form = ContactForm2()
    return render(request, 'website/contact.html', {'form':form})

def testingForm1(request):
    if request.method == "POST":
        form = contactForm1(request.POST)
        if form.is_valid():
            c = Contact()
            c.name = form.cleaned_data['name']
            c.subject = form.cleaned_data['subject']
            c.email = form.cleaned_data['email']
            c.message = form.cleaned_data['message']
            c.save()
            print(form.cleaned_data)
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')
    
    form = contactForm1()
    return render(request, 'testForm1.html', {'form1':form})

def testingForm2(request):
    if request.method == "POST":
            form = ContactForm2(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
                form.save()
                return HttpResponse('done')
            else:
                return HttpResponse('not valid')
    
    form = ContactForm2()
    return render(request, 'testForm2.html', {'form2':form})