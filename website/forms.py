from django import forms
from website.models import Contact
from captcha.fields import CaptchaField


class ContactForm2(forms.ModelForm):
    captcha = CaptchaField()
    # another_field = forms.CharField(max_length=255)
    class Meta:
        model = Contact
        fields = '__all__' #! به کاربر نمایش دهی html فیلدهایی که میخواهی در 
        # fields = ['name','email']
        # exclude = ['name'] #! ... همه فیلدهارو بیار به غیر از
        #? https://docs.djangoproject.com/en/4.2/topics/forms/modelforms/#field-types


class contactForm1(forms.Form):
    name = forms.CharField(max_length=225)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)

