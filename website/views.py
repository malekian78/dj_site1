from django.shortcuts import render

# Create your views here.
def home(request):
    # return HttpResponse("<h1>Text from view Home</h1>")
    return render(request, 'website/index.html')

def contatct(request):
    return render(request, 'website/contact.html')