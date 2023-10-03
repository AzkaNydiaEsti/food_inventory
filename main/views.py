from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from main.models import Barang
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404

@login_required(login_url='/login')

def show_main(request):
    products = Barang.objects.filter(user=request.user)
    jumlah_item = len(products)
    context = {
        'creator_name': 'Azka Nydia Estiningtyas',
        'nama': request.user.username,
        'npm': '2206028970',
        'class': 'PBP E',
        'products' : products,
        'last_login': request.COOKIES['last_login'],
        'total_items' : f'You have {jumlah_item} types of food items in here',
    }

    return render(request, "main.html", context)

def add_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "add_item.html", context)

def edit_item(request, id):
    product = Barang.objects.get(pk = id)

    form = ItemForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_item.html", context)

def show_xml(request):
    data = Barang.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Barang.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Barang.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Barang.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def dec_amount(request, id):
    item = Barang.objects.get(pk=id)
    if request.method == 'POST':
        if item.amount > 0:
            if item.amount > 0:
                item.amount -= 1
                item.save() 
            elif item.amount <= 0:
                item.delete()
    return redirect('main:show_main')

def inc_amount(request, id):
    item = Barang.objects.get(pk=id)
    if request.method == 'POST':
        if item.amount > 0:
            item.amount += 1
            item.save() 
    return redirect('main:show_main')

def delete_item(request, id):
    if request.method == 'POST':
        item = Barang.objects.get(id=id)
        item.delete()
    
    return redirect('main:show_main')