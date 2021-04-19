from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from sweetlandapp.forms import UploadFileForm, OrderForm
from sweetlandapp.models import Products, Cart


def adding_prod(request):
    if request.method == 'GET':
        return render(request, 'adding.html', {'form': UploadFileForm})
    elif request.method == 'POST':
        Products.objects.create(name=request.POST['name'],
                                image=request.FILES['file'],
                                description=request.POST['description'],
                                full_description=request.POST['full_description'],
                                product_type=request.POST['product_type'],
                                price=request.POST['price'])
        products = Products.objects.filter(product_type='chocolate')
        return render(request, 'adding.html', {'form': UploadFileForm})



def main_page(request):
    cart_counter = len(Cart.objects.all())
    return render(request, 'main_page.html', {'cart_counter': cart_counter})


def products_showcase(request, product_type, product_id):
    cart_counter = len(Cart.objects.all())
    products = Products.objects.filter(product_type=product_type)
    if request.method == 'GET':
        return render(
            request,
            'products_showcase.html',
            {'products': products, 'cart_counter': cart_counter, 'product_id': product_id}
        )
    else:
        return render(request,
                      'products_showcase.html',
                      {'products': products, 'cart_counter': cart_counter, 'quantity': 1, 'product_id': product_id}
                      )


def specific_product(request, product_id):
    cart_counter = len(Cart.objects.all())
    product = Products.objects.get(id=product_id)
    return render(request, 'specific_product.html', {'cart_counter': cart_counter, 'product': product})


def cart(request):
    products = Cart.objects.all()
    cart_counter = len(products)
    return render(request, 'cart.html', {
        'products': products,
        'cart_counter': cart_counter,
        'form': UploadFileForm,
    })


def add_to_cart(request, id):
    isproductincart = False
    product = Products.objects.get(id=id)
    for cart_prod in Cart.objects.all():
        if cart_prod.product == product:
            quantity = int(request.GET['quantity'])
            if quantity > 0:
                cart_prod.quantity += quantity
                cart_prod.save()
                isproductincart = True
            else:
                return redirect('products-showcase', product_type=product.product_type, product_id=0)
    if not isproductincart:
        Cart.objects.create(
            name=product.name,
            image=product.image,
            description=product.description,
            full_description=product.full_description,
            product_type=product.product_type,
            price=product.price,
            quantity=request.GET['quantity'],
            product=product
        )
    return redirect('products-showcase', product_type=product.product_type, product_id=0)


def order_page(request):
    if request.method == 'POST':
        total_sum = 0
        products = Cart.objects.all()
        for product in products:
            prod_id = str(product.id)
            updated_quantity = request.POST[prod_id]
            if int(updated_quantity) > 0:
                product.quantity = updated_quantity
                product.save()
            else:
                products = Cart.objects.all()
                cart_counter = len(products)
                err = 'quantity cannot be negative'
                return render(request,
                              'cart.html',
                              {'products': products, 'cart_counter': cart_counter, 'form': UploadFileForm, 'err': err})
        for product in products:
            total_sum += product.price * int(product.quantity)
        cart_counter = len(products)
        return render(request, 'order_page.html', {
            'form': OrderForm,
            'total': round(total_sum),
            'cart_counter': cart_counter
        })
    else:
        return HttpResponse('blabla')


def send_mail_sw(request):
    html_message = loader.render_to_string(
        'message.html', {
            'name': request.POST['firstname'],
            'delivery_time': request.POST['delivery_time'],
            'address': request.POST['address']
        }
    )

    send_mail(
        subject='sweetland',
        message='',
        html_message=html_message,
        from_email='tms.sweetland@gmail.com',
        recipient_list=[request.POST['email'], 'Wherefored@gmail.com'],
        fail_silently=False,
    )
    return redirect('cart-clear')


def cart_clear(request):
    Cart.objects.all().delete()
    return redirect('main-page')


def prod_clear(request):
    Products.objects.all().delete()
    return redirect('main-page')
