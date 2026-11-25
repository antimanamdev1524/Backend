from django.contrib import auth
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
import random
from django.core.mail import send_mail

from .models import Address, Product
from .models import Category
from .models import BuyerProfile
from .models import SellerProfile
from .models import BankDetails

# Create your views here.
def index(request):
    bestsellers = Product.objects.order_by('?')[:4]
    products = Product.objects.order_by('?')[4:8]
    return render(request, 'index.html', {'products': products, 'bestsellers': bestsellers})

def about(request):
    return render(request, 'about.html')

def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})

def category(request):
    categories = Category.objects.filter(parent=None)
    products = Product.objects.all()

    print("PRODUCTS:", products)
    return render(request, 'category.html', {'categories': categories, 'products': products})

def category_products(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'category_products.html', {'category': category, 'products': products})

def category_single_product(request, category_id, product_id):
    category = Category.objects.get(id=category_id)
    product = Product.objects.get(id=product_id)
    return render(request, 'category_single_product.html', {'product': product, 'category': category})

def blog_single(request):
    return render(request, 'blog_single.html')

def blog(request):
    return render(request, 'blog.html')

def cart(request):
    return render(request, 'cart.html')

def contact(request):
    return render(request, 'contact.html')

def product_single(request, id):
    product = Product.objects.get(id=id)
    related_products = Product.objects.filter(category= product.category).exclude(id=product.id)
    return render(request, 'product_single.html', {'product': product, 'related_products': related_products})

def seller_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        owner_name = request.POST['owner_name']
        business_name = request.POST['business_name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        profile_picture = request.FILES.get('profile_picture')

        if password != confirm_password:
            return render(request, 'seller_signup.html', {'error': 'Passwords do not match!'})
        
        user = User.objects.create_user(
            username=email, 
            email=email, 
            password=password
            )
        
        seller_profile = SellerProfile.objects.create(
            user=user,
            owner_name=owner_name,
            business_name=business_name,
            mobile=mobile,
            profile_picture=profile_picture
        )
        return render(request, 'signup_success.html', {'user': user})
    return render(request, 'seller_signup.html')

def buyer_signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        profile_picture = request.FILES.get('profile_picture')

        if  password != confirm_password:
             return render(request, 'buyer_signup.html', {'error': 'Password & Confirm Password does not match!'})
                            
        user = User.objects.create_user(
            username=email,
            first_name=first_name,
            last_name= last_name, 
            email= email, 
            password=password
            )
        
        buyer_profile = BuyerProfile.objects.create(
                user = user,
                mobile=mobile,
                profile_picture= profile_picture
            )
        return render(request, 'signup_success.html')
           
    return render(request, 'buyer_signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                auth.login(request, user)
                request.session['email'] = user.email

                try:
                    seller_profile = SellerProfile.objects.get(user=user)
                    return redirect('seller_dashboard')
                except SellerProfile.DoesNotExist:
                     try:
                        buyer_profile = BuyerProfile.objects.get(user= user)
                        return redirect('home')
                     except BuyerProfile.DoesNotExist:
                        return redirect('home')
            else:
                return render(request, 'login.html', {'error': 'Invalid Password!'})
        except User.DoesNotExist:
                return render(request, 'login.html', {'error': 'Email does not exist!'})
    return render(request, 'login.html')
	  

def seller_dashboard(request):
    return render(request, 'seller_dashboard.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def c_pass(request):
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_new_password = request.POST['confirm_new_password']

        current_user= request.user
        if current_user.check_password(old_password):
         
                if(new_password == confirm_new_password):
                    current_user.set_password(new_password)
                    current_user.save()
                    update_session_auth_hash(request, current_user)
                    try:
                        seller_profile = SellerProfile.objects.get(user=current_user)
                        return redirect('seller_dashboard')
                    except SellerProfile.DoesNotExist:
                        return redirect('home')
                else:
                    return render(request, 'c_pass.html', {'error': 'password & confirm password doesnot match!'})            
        else:
                return render(request, 'c_pass.html', {'error': 'Incorrect old password!'})
        
    return render(request, 'c_pass.html')

def f_pass(request):
    if request.method == 'POST':
        email = request.POST['email']
       
        try:
            user= User.objects.get(email=email)
            otp = random.randint(100000, 999999)

            request.session['otp'] = otp
            request.session['email'] = email

            send_mail(
             'OTP Verification',
              f'Welcome to bloomshop!\n\n Your OTP for password reset is {otp}.',
             'antimanamdev1524@gmail.com',
             [email]
            )
            return redirect('verify_otp')
        except User.DoesNotExist:
            return render(request, 'f_pass.html', {'error': 'Invaild email-id'})
 
    return render(request, 'f_pass.html')

def verify_otp(request):
    if request.method=='POST':
        entered_otp= request.POST['otp']
        session_otp=request.session.get('otp')

        if str(entered_otp)==str(session_otp):
            return render(request, 'n_pass.html')
        else:
            return render(request, 'verify_otp.html', {'error': 'Invalid OTP!'})
    return render(request, 'verify_otp.html')

def n_pass(request):
    if request.method == 'POST':
            new_password = request.POST['new_password']
            confirm_new_password = request.POST['confirm_new_password']
            try:
                email = request.session.get('email')
                current_user= User.objects.get(email=email)

                if new_password == confirm_new_password:
                  current_user.set_password(new_password)
                  current_user.save()
                  request.session.flush()
                  return redirect('login')
                else:
                  return render(request, 'n_pass.html', {'error': 'Password & Confirm Password does not match!'})

            except User.DoesNotExist:
                 return render(request, 'n_pass.html', {'error': 'User not found!'})                             
    return render(request, 'n_pass.html')

def profile(request):
    current_user = request.user
    try:
        seller_profile = SellerProfile.objects.get(user=current_user)
        return render(request, 'profile.html', {'profile': seller_profile})
    except SellerProfile.DoesNotExist:
        try:
            buyer_profile = BuyerProfile.objects.get(user=current_user)
            address = Address.objects.get(user=current_user)
            return render(request, 'buyer_profile.html', {'profile': buyer_profile, 'address': address})
        except BuyerProfile.DoesNotExist:
            return redirect('home')

def buyer_profile(request):
    current_user = request.user
    try:
        buyer_profile = BuyerProfile.objects.get(user=current_user)
    except BuyerProfile.DoesNotExist:
        return redirect('home') 
    address = Address.objects.filter(user=current_user).first()
    bank_details = BankDetails.objects.filter(user=current_user).first()
    return render(request, 'buyer_profile.html', {'profile': buyer_profile, 'address': address, 'bank_details': bank_details})
       

def seller_profile(request):
    current_user = request.user
    try:
        seller_profile = SellerProfile.objects.get(user=current_user)
        return render(request, 'profile.html', {'profile': seller_profile})
    except SellerProfile.DoesNotExist:
        return redirect('home')

@login_required
def update_profile(request):
    if request.method == 'POST':
        current_user = request.user
        try:
            buyer_profile = BuyerProfile.objects.get(user=current_user)

            current_user.first_name = request.POST.get('first_name')
            current_user.last_name = request.POST.get('last_name')
            current_user.save()
            
            mobile = request.POST.get('mobile')
            buyer_profile.mobile = mobile

            profile_picture = request.FILES.get('profile_picture')
            if profile_picture:
                buyer_profile.profile_picture = profile_picture
            buyer_profile.save()

            country = request.POST.get('country')
            state = request.POST.get('state')
            district = request.POST.get('district')
            city = request.POST.get('city')
            apartment = request.POST.get('apartment')
            street = request.POST.get('street')
            pincode = request.POST.get('pincode')

            try:
                address = Address.objects.get(user=current_user)
                address.country = country
                address.state = state
                address.district = district
                address.city = city
                address.apartment = apartment
                address.street = street
                address.pincode = pincode
                address.save()
                return redirect('buyer_profile')
            except Address.DoesNotExist:
                address = Address.objects.create(
                user=current_user,
                country=country,
                state=state,
                district=district,
                city=city,
                apartment=apartment,
                street = street,
                pincode = pincode
            )   
            address.save()
            return redirect('buyer_profile')
        except BuyerProfile.DoesNotExist:
            return redirect ('index')
    return render(request, 'update_profile.html', {'profile': BuyerProfile.objects.get(user=request.user), 'address': Address.objects.get(user=request.user)})

@login_required
def bank_account(request):
    current_user = request.user
    buyer_profile = BuyerProfile.objects.get(user=current_user)
    address = Address.objects.filter(user=current_user).first()

    if request.method == "POST":
            bank_name = request.POST.get('bank_name')
            branch = request.POST.get('branch')
            account_holder = request.POST.get('account_holder')
            ifsc_code = request.POST.get('ifsc_code')
            account_number = request.POST.get('account_number')
            reenter_account_number = request.POST.get('confirm_account_number')
            
            if account_number != reenter_account_number:
                return render(request, 'buyer_profile.html', {'profile': buyer_profile, 'active-tab': 'sec-bank-details', 'address': address, 'msg': 'Account number and re-entered account number do not match!'})
            else:
                try:
                    bank_details = BankDetails.objects.get(user=current_user)
                    bank_details.bank_name = bank_name
                    bank_details.branch = branch
                    bank_details.account_holder = account_holder
                    bank_details.account_number = account_number
                    bank_details.ifsc_code = ifsc_code
                    bank_details.save()
                except BankDetails.DoesNotExist:
                    bank_details = BankDetails.objects.create(
                        user=current_user,
                        bank_name=bank_name,
                        branch=branch,
                        account_holder=account_holder,
                        ifsc_code=ifsc_code,
                        account_number=account_number,
                    )     
                return render(request, 'buyer_profile.html', {'profile': buyer_profile, 'address': address, 'bank_details' : bank_details, 'active-tab': 'sec-bank-details', 'msg': 'Bank details updated successfully!', 'msg_type': 'success'})
    return render(request, 'buyer_profile.html', {'profile': buyer_profile, 'address': address, 'active-tab': 'sec-bank-details', 'msg': 'Please fill in your bank details.', 'msg_type': 'info'})

def checkout(request):
    return render(request, 'checkout.html')