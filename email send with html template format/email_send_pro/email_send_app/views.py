from django.shortcuts import render,redirect
from .forms import Contact_Form
# Create your views here.
''' ************************* send_mail *********************** '''
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.template.loader import render_to_string

#html email required stuff
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags



def Contact_us(request):
    c_form = Contact_Form(request.POST or None)
    if c_form.is_valid():

        '''name = c_form.cleaned_data.get('name')
        mail_subject = "Thank you for Contact to our site"
        mail_message = render_to_string('contact_email.html', {
            "name": name,
        })
        to_email = c_form.cleaned_data.get('email')
        to_list = [to_email]
        from_email = settings.APPLICATION_EMAIL
        send_mail(mail_subject, mail_message, from_email, to_list, fail_silently=True)'''

        name = c_form.cleaned_data.get('name')
        to_email = c_form.cleaned_data.get('email')
        #receiver_email = 'abc@gmail.com'
        html_content = render_to_string('contact_email.html', {'name': name})
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(
            "Thank you for Contact to our site",
            text_content,
            settings.APPLICATION_EMAIL,
            [to_email],
            #[receiver_email],
            reply_to=[settings.APPLICATION_EMAIL]

        )
        email.attach_alternative(html_content,"text/html")
        email.send(fail_silently=False)
        return redirect('result')

    context={
        'c_form':c_form,

    }
    return render(request, 'contact.html', context)

def result(request):
    return render(request, 'result.html')