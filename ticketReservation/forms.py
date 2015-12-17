from django import forms
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        userName = self.cleaned_data['name']
        subject = "Contact on site"
        message = self.cleaned_data['message'] + ',\n' + userName
        sender = self.cleaned_data['email']

        recipients = ['ivan.simicic92@gmail.com']
        print message
        send_mail(subject, message, sender, recipients)
