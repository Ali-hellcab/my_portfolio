from django.shortcuts import render, redirect
from .models import Project, Aboutme, Profilepic, Resume
from django.core.mail import send_mail
from django.contrib import messages
from .models import ContactMessage

def displaypage(request):
    # This is a safer and more direct way to get the single instance.
    profilepic = Profilepic.objects.first()
    projects = Project.objects.all()
    aboutme = Aboutme.objects.all()
    resume = Resume.objects.first()  # Retrieve the first Resume object

    context = {
        'aboutme': aboutme,
        'profilepic': profilepic,
        'projects': projects,
        'resume': resume,  # Add the Resume object to the context
    }
    return render(request, 'display/display.html', context)



def send_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_text = request.POST.get('message')

        # Save to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message_text
        )

        messages.success(request, "Your message has been saved. Thank you!")
        return redirect('display_page')  # Replace 'home' with your home view name or URL name

    return redirect('display_page')
