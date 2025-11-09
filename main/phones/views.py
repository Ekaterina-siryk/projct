from django.shortcuts import render, redirect, get_object_or_404

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = {}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
def catalog(request):
    sort_param = request.GET.get('sort', 'name')  # по умолчанию по названию
    order_param = request.GET.get('order', 'asc')  # по умолчанию по возрастанию

    if sort_param == 'name':
        phones = Phone.objects.all().order_by('name')
    elif sort_param == 'price':

        order = '-' if order_param == 'desc' else ''
        phones = Phone.objects.all().order_by(f'{order}price')
    else:

        phones = Phone.objects.all()

    context = {
        'phones': phones,
        'sort': sort_param,
        'order': order_param,
    }
    return render(request, 'catalog.html', context)

def phone_detail(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    return render(request, 'phone_detail.html', {'phone': phone})
