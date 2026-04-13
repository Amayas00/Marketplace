from django import forms
from .models import Listing

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class NewListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('category', 'name', 'description', 'price', 'condition', 'location', 'image',)
        widgets = {
            'category': forms.Select(attrs={'class': INPUT_CLASSES}),
            'name': forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'e.g. Vintage Leather Jacket'}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASSES, 'rows': 4}),
            'price': forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder': '0.00'}),
            'condition': forms.Select(attrs={'class': INPUT_CLASSES}),
            'location': forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'e.g. London, UK'}),
            'image': forms.FileInput(attrs={'class': INPUT_CLASSES}),
        }


class EditListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('name', 'description', 'price', 'condition', 'location', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASSES, 'rows': 4}),
            'price': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'condition': forms.Select(attrs={'class': INPUT_CLASSES}),
            'location': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'image': forms.FileInput(attrs={'class': INPUT_CLASSES}),
        }
