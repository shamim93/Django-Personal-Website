from django.shortcuts import render
#from django.http import HttpResponse


from .models import Contact

# Create your views here.

#when we want to return html/css/js file then needs to return render function

def index(request):
    #return HttpResponse("Hello World!")
    return render(request, 'mysite/index.html')


def portfolio(request):

    return render(request, 'mysite/portfolio.html')


def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        c = Contact(email=email,subject = subject, message=message)
        c.save()

        return render(request, 'mysite/thanks.html')
    else:
        return render(request, 'mysite/contact.html')

