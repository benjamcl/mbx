from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def home(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        company = request.POST['company']

        #send email
        '''
        send_mail(
            'Check-In Confirmation for ' + first_name + ' ' + last_name, #subject
            'You have completed your check-in!', #message
            ['bencliu92@gmail.com'], #from email
            ['bencliu92@gmail.com'], # to email
            fail_silently=False
        )
        '''

        return render(request, 'home.html', {'first_name': first_name})
    else:
        return render(request, 'home.html', {})


# Use this to print post to page
# return render(request, 'home.html', {}, {'first_name': first_name})