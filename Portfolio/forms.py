from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=500, label="Your Name(Required)",
                           widget=forms.TextInput(attrs={'class': 'form-field'}))
    email = forms.EmailField(required=True, max_length=500, label="Your Email(Required)",
                             widget=forms.TextInput(attrs={'class': 'form-field'}))
    subject = forms.CharField(max_length=500, label="Subject", widget=forms.TextInput(
        attrs={'class': 'form-field'}))
    message = forms.CharField(label='Your Message', widget=forms.Textarea(
        attrs={'class': 'form-field'}))
