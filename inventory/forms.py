from django import forms
from django.utils.text import slugify
from .models import Product, Category, Attribute, AttributeValue


class FormCategory(forms.ModelForm):
    name = forms.CharField(
        label="Product Name",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label_suffix='',
    )
    
    slug = forms.CharField(
        label="Slug",
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'readonly': 'readonly',
                'placeholder':'Automatic Fill'
            }
        ),
        label_suffix='',
    )

    class Meta:
        model = Category
        fields = ('name', 'slug', 'is_active')

    def clean_slug(self):
        name = self.cleaned_data['name']
        return slugify(name)


class FormProduct(forms.ModelForm):
    name = forms.CharField(
        label="Product Name",
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label_suffix='',
    )

    description = forms.CharField(
        label="Description",
        required=False,
        max_length=100,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 3,
                'cols': 30,
            }
        ),
        label_suffix='',
    )

    slug = forms.CharField(
        label="Slug",
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'readonly': 'readonly',
                'placeholder':'Automatic Fill'
            }
        ),
        label_suffix='',
    )

    class Meta:
        model = Product
        fields = ('name', 'description', 'slug', 'is_active', 'category')

    def clean_slug(self):
        name = self.cleaned_data['name']
        return slugify(name)
    

class FormAttr(forms.ModelForm):
    name = forms.CharField(
        label="Attribute Name",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label_suffix='',
    )

    description = forms.CharField(
        label="Description",
        required=True,
        max_length=100,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 3,
                'cols': 30,
            }
        ),
        label_suffix='',
    )

    class Meta:
        model = Attribute
        fields = ('name', 'description')

class FormAttrValue(forms.ModelForm):
    value = forms.CharField(
        label="Attribute Value",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label_suffix='',
    )

    class Meta:
        model = AttributeValue
        fields = ('attribute', 'value')