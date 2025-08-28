from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Review


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    """Form for creating/editing reviews"""

    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add placeholders and classes
        self.fields['comment'].widget.attrs['placeholder'] = (
            'Write your review here...'
        )
        self.fields['comment'].widget.attrs['rows'] = 4
        self.fields['comment'].widget.attrs['class'] = 'border-black rounded-0'

        # Set default rating value
        if not self.instance.pk:  # Only for new reviews
            self.fields['rating'].initial = 5
