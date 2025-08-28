from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """Form for contact submissions"""

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add placeholders and classes
        placeholders = {
            'name': 'Your Name',
            'email': 'Your Email',
            'subject': 'Subject',
            'message': 'Your Message',
        }

        for field in self.fields:
            placeholder = placeholders.get(field, '')
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            self.fields[field].label = False

        # Make message field a textarea with rows
        self.fields['message'].widget.attrs['rows'] = 5
        