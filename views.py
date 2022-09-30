from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Order
from math import ceil
# Create your views here.


def index(request):
    products = Product.objects.all()

    # allprods = [[products , range(1,n_slides),n_slides],
    #             [products , range(1,n_slides),n_slides]]
    allprods = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        n_slides = n//4 + ceil((n/4) - (n//4))
        allprods.append([prod, range(1, n_slides), n_slides])

    context = {'allprods': allprods}
    # context = {'no_of_slides':n_slides, 'range':range(1, n_slides),'products':products}
    return render(request, 'shop/index.html', context)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return render(request, 'shop/contact.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def search(request):
    return HttpResponse('seach page')


def productView(request, myid):
    products = Product.objects.filter(id=myid)
    print(products)
    return render(request, 'shop/productview.html', {'product': products[0]})


def checkout(request):
    if request.method == 'POST':
        item_json = request.POST.get('item_json')
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address1') + \
            "" + request.POST.get('address2')
        state = request.POST.get('state')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip_code')
        phone_no = request.POST.get('phone_no')
        order = Order(name=name, email=email, address=address, state=state,
                      city=city, zip_code=zip_code, phone_no=phone_no, items_json=item_json)
        order.save()
        thank = True
        id = order.id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})

    return render(request, 'shop/checkout.html')
