from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите название товара'}))
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание'}))
    price = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    image = forms.ImageField()
