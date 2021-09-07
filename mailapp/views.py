from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def home(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message='Xabar yuborgan shaxs: '+name+'\n'+'xabar: '+subject+'\n'+'email adresi: '+email
        send_mail(name,message,email,['bunyodkoson@gmail.com'],
                  fail_silently=False )
               
           
    return render(request, 'mail.html')