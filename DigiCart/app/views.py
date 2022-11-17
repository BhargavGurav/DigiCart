from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib import messages
import hashlib #for password
from .models import AddMobile, AddLaptop, AddMenItem, AddWomenItem, AddKidsItem, AddHomeItem, AddGrocery, AddWatche, AddFootwear, Customer, Cart, History
# Create your views here.

@cache_control(no_cache=True, must_revalidade=True, no_store=True)
def home(request):
    if request.method=='POST':
        name = request.POST['item_name']
        price = request.POST['item_price']
        category = request.POST['item_category']
        disc = request.POST['item_disc']
        current_user = Customer.objects.get(user=request.user)
        item = Cart(user=current_user, item_name=name, category=category, item_price=price, item_disc=disc, quantity=1)
        if category=='Mobiles':
            req_item = AddMobile.objects.get(name=name)
            item.item_image = req_item.image
        elif category=='Laptops':
            req_item = AddLaptop.objects.get(name=name)
            item.item_image = req_item.image
        elif category=='Men':
            req_item = AddMenItem.objects.get(name=name)
            item.item_image = req_item.image
        elif category=='Women':
            req_item = AddWomenItem.objects.get(name=name)
            item.item_image = req_item.image
        elif category=='Kids':
            req_item = AddKidsItem.objects.get(name=name)
            item.item_image = req_item.image
        elif category=='Home':
            req_item = AddHomeItem.objects.get(name=name)
            item.item_image = req_item.image
        elif category=='Grocery':
            req_item = AddGrocery.objects.get(name=name)
            item.item_image = req_item.image
        elif category=='Watches':
            req_item = AddWatche.objects.get(name=name)
            item.item_image = req_item.image
        elif category=='Footwear':
            req_item = AddFootwear.objects.get(name=name)
            item.item_image = req_item.image
        
        
        item.save()
        messages.success(request, 'Added successfully')
        
    context = dict()
    context['Mobiles'] = list(AddMobile.objects.all())
    context['Laptops'] = list(AddLaptop.objects.all())
    context['Men'] = list(AddMenItem.objects.all())
    context['Women'] = list(AddWomenItem.objects.all())
    context['Kids'] = list(AddKidsItem.objects.all())
    context['Home'] = list(AddHomeItem.objects.all())
    context['Grocery'] = list(AddGrocery.objects.all())
    context['Watches'] = list(AddWatche.objects.all())
    context['Footwear'] = list(AddFootwear.objects.all())
    dictionary = {}
    dictionary['data'] = context
    return render(request, 'home.html', dictionary)

@cache_control(no_cache=True, must_revalidade=True, no_store=True)
@login_required(login_url='loginuser')
def checkout(request):
    current_user = Customer.objects.get(user=request.user)
    items_of_current_user = Cart.objects.filter(user=current_user)
    total = 0
    for i in items_of_current_user:
        total += i.item_price
    return render(request, 'checkout.html', {'items' : items_of_current_user, 'total' : total})

def register(request):
    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['mobile']
        email = request.POST['email']
        pic = request.POST['profile']
        dob = request.POST['dob']
        address = request.POST['add']
        gender = request.POST['gender']
        password = request.POST['password']

        
        
        if fname=='':
            messages.error(request, 'First name field cannot be empty')
            return HttpResponseRedirect('/register')
        elif lname=='':
            messages.error(request, 'Last name field cannot be empty')
            return HttpResponseRedirect('/register')
        elif phone=='':
            messages.error(request, 'Phone number field cannot be empty')
            return HttpResponseRedirect('/register')
        elif email=='':
            messages.error(request, 'Email field cannot be empty')
            return HttpResponseRedirect('/register')
        elif User.objects.filter(email=email):
            messages.error(request, 'Email already used !')
            return HttpResponseRedirect('/register')
        elif dob=='':
            messages.error(request, 'Date of birth field cannot be empty')
            return HttpResponseRedirect('/register')
        elif address=='':
            messages.error(request, 'Address field cannot be empty')
            return HttpResponseRedirect('/register')
        elif gender=='':
            messages.error(request, 'Gender field cannot be empty')
            return HttpResponseRedirect('/register')
        elif password=='':
            messages.error(request, 'Password field cannot be empty')
            return HttpResponseRedirect('/register')
        elif len(password) < 8:
            messages.error(request, 'Password must contain atleast 8 characters')
            return HttpResponseRedirect('/register')
        elif not any(x.islower() for x in password):
            messages.error(request, 'Password must contain atleast 1 lowercase character')
            return HttpResponseRedirect('/register')
        elif not any(x.isupper() for x in password):
            messages.error(request, 'Password must contain atleast 1 uppercase character')
            return HttpResponseRedirect('/register')
        elif not any(x.isdigit() for x in password):
            messages.error(request, 'Password must contain atleast 1 digit')
            return HttpResponseRedirect('/register')
            

        
        else:
            user = User.objects.create_user(fname, email, password)
            user.first_name = fname 
            user.last_name = lname
            user.save()
            
            data = Customer(user=user, phone=phone, profile_pic=pic, dob=dob, address=address, gender=gender)
            data.save()
            messages.success(request, 'Account created successfully.')
            return HttpResponseRedirect('/')
    return render(request, 'register.html')

def loginuser(request):
    if request.method=='POST':
        user = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(email=user):
            requesting_user = requesting_user = User.objects.get(email=user)
            if authenticate(username=requesting_user.username, password=password):
                messages.success(request, 'Logged in successfully')
                login(request, requesting_user)
                return HttpResponseRedirect('/')
            else:
                messages.error(request, 'Wrong password !')
                return HttpResponseRedirect('/loginuser')
        else:
            messages.error(request, 'No user found ! Register first')
            return HttpResponseRedirect('/register')


    return render(request, 'login.html')

def profile(request, name):
    user = Customer.objects.get(user=name)
    return render(request, 'profile.html', {'customer' : user})

# def add_cart(request, item_cat, item):
#     item_to_add = item_cat.item
#     return render(request, 'checkout.html', {'received' : item_to_add })

def delete_item(request, id):
    item_to_delete = Cart.objects.get(id=id)
    item_to_delete.delete()
    messages.success(request, 'Removed successfully')
    return HttpResponseRedirect('/checkout')

def buy(request):
    context = {}
    if request.method=='POST':
        name = request.POST.get('item_name')
        price = request.POST.get('item_price')
        category = request.POST.get('item_category')
        disc = request.POST.get('item_disc')
        context['name'] = name
        context['price'] = price

    
    return render(request, 'buy.html', context)

def history(request):
    if request.method=='POST':
        name = request.POST['name']
        price = request.POST['price']
        current_user = Customer.objects.get(user=request.user)
        history = History(user=current_user, item_name=name, total_price=price)
        history.save()
        messages.success(request, 'Order placed successfully')
        return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')

def history_page(request):
    user = Customer.objects.get(user=request.user)
    hist = History.objects.filter(user=user)
    return render(request, 'history_page.html', {'hist' : hist})

def delete_history(request):
    user = Customer.objects.get(user=request.user)
    hist = History.objects.filter(user=user)
    for i in hist:
        i.delete()

    messages.success(request, 'History cleared successfully')
    return HttpResponseRedirect('/history_page')

def save_cart_items(request):
    current_user = Customer.objects.get(user=request.user)
    items_of_current_user = Cart.objects.filter(user=current_user)
    for i in items_of_current_user:
        history = History(user=current_user, item_name=i.item_name, total_price=i.item_price)
        history.save()
    for i in items_of_current_user:
        i.delete()
    messages.success(request, 'Order placed successfully')
    return HttpResponseRedirect('/')

def logoutuser(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return HttpResponseRedirect('/')