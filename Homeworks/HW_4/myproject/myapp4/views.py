from django.shortcuts import render
from .models import Product
from .forms import ProductForm
from django.core.files.storage import FileSystemStorage


def index(request):
    return render(request, 'myapp4/index.html')


def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            product = Product(name=name, description=description, price=price, image=image)
            print(
                f'Product name: {product.name}\nPrice: {product.price}\n'
                f'Description: {product.description}\nImage: {product.image.name}')
    else:
        form = ProductForm()

    return render(request, 'myapp4/product_form.html', {'form': form})

