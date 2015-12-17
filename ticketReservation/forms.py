from django import forms
from django.core.mail import send_mail, BadHeaderError
from django.core.validators import EmailValidator, MinLengthValidator, MaxLengthValidator


class ContactForm(forms.Form):
    name = forms.CharField(
        label='Your name', max_length=20, required=True,
        validators=[MinLengthValidator(3)])
    email = forms.EmailField(validators=[EmailValidator], required=True)
    message = forms.CharField(widget=forms.Textarea, required=True,
                              validators=[MaxLengthValidator(200)])

    def send_email(self):
        userName = self.cleaned_data['name']
        subject = "Contact on site"
        message = self.cleaned_data['message'] + ',\n' + userName
        sender = self.cleaned_data['email']

        recipients = ['ivan.simicic92@gmail.com']
        if message and sender:
            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:
                raise forms.ValidationError("Bad header error")
