from django.shortcuts import render, redirect
from .models import*
import random
import requests
from django.views.decorators.csrf import csrf_exempt
from .models import Product
from django.shortcuts import get_object_or_404
from .models import Cart, Product
from django.contrib.auth.models import User
from django.conf import settings
import razorpay
from django.contrib.auth.hashers import check_password


# Create your views here.

def index(request):
    product = Product.objects.all()
    return render(request, 'index.html', {'product': product})

def about(request):
    return render(request, 'about.html')

def CPass(request):
    user= User.objects.get(email= request.session['email'])
    if request.method== "POST":
        try:
            
            if user.password== request.POST['Opassword']:
                if request.POST['Npassword'] == request.POST['CNpassword']:
                    user.password= request.POST['Npassword']
                    user.save() 
                    return redirect('Logout')
                else:
                    msg = "password & Confirm password Doesn't Match!!"
                    if user.usertype=="buyer":
                        return render(request, 'CPass.html',{'msg':msg})
                    else:
                        return render(request, 'scpass.html', {'msg': msg})

            else:
                msg = "Old password doesn't match"
                if user.usetype=="buyer":
                    return render(request, 'CPass.html', {'msg': msg})
                else:
                     return render(request, 'scpass.html', {'msg': msg})
            

        except Exception as e:
             print("*************", e)
             return render(request, 'CPass.html')
 
    else:
            if user.usertype=="buyer":
                return render(request, 'CPass.html')
            else:
                return render(request, 'scpass.html')

def Signup(request):
    if request.method== "POST":
        try:
            user = User.objects.get(email=request.POST['email'])
            print("email error")
            msg = "email already exist!!"
            return render(request, 'signup.html',{'msg':msg})
       
        except:
            if request.POST['password'] == request.POST['Cpassword']:
                User.objects.create(
                    usertype= request.POST['usertype'],
                    name = request.POST['name'],
                    email = request.POST['email'],
                    mobile = request.POST['mobile'],
                    password = request.POST['password'], 
                    uprofile = request.FILES['uprofile']
                )
                user.save()
                msg= "Signup Successfully!!"
                return render(request, 'Login.html', {'msg': msg})
            

            else:
                msg= "password & Confirm password doesn't match!!"
                return render(request, 'signup.html', {'msg': msg})
                 
    else:
        return render(request, 'signup.html')
    
@csrf_exempt
@csrf_exempt
def Login(request):
    if request.method == "POST":
        try:
            email = request.POST['email']
            print(f"🔍 Debug: Email entered - {email}")

            user = User.objects.get(email=email)  # Check email exist karta hai ya nahi
            print(f"✅ Debug: User found - {user}")

            if check_password(request.POST['password'], user.password):
                request.session['email'] = user.email
                request.session['uprofile'] = user.uprofile.url

                if user.usertype == "buyer":
                    return redirect('index')
                else:
                    return redirect('sindex')
            else:
                msg = "Invalid password!!"
                print("❌ Debug: Password incorrect")
                return render(request, 'Login.html', {'msg': msg})

        except Exception as e:
            print(f"⚠ Debug: Error - {e}")  # Yeh error message print karega
            msg = "Invalid email!!"
            return render(request, 'Login.html', {'msg': msg})
    else:
        return render(request, 'Login.html')

# def Login(request):
#          if request.method== "POST":
#              try:
#                  user= User.objects.get(email=request.POST['email'])
#                  print(user.password)  # 🔍 Dekho kya password hash format me hai?

#                  if check_password(request.POST['password'], user.password):
#                 #  user.password== request.POST['password']:
#                      request.session['email']= user.email
#                      request.session['uprofile']= user.uprofile.url
                                     
#                      if user.usertype== "buyer":
#                             return redirect('index')
#                      else:
#                             return redirect('sindex')          
#                  else:
#                      msg= "Invalid password!!"
#                      return render(request, 'Login.html', {'msg': msg})
                 
#              except:
#                  msg = "Invalid email!!"
#                  return render(request, 'login.html', {'msg': msg})
#          else:
#              return render(request, 'Login.html')
         
def Logout(request):
    del request.session['email']
    del request.session['uprofile']
    return redirect('Login')

def FPass(request):
    if request.method=="POST":
     
     try: 
            user= User.objects.get(mobile= request.POST['mobile'])
            mobile = request.POST['mobile']

            otp = random.randint(1000, 9999)
            
         
            url = "https://www.fast2sms.com/dev/bulkV2"

            querystring = {"authorization":"PnwT18P3x681zEc7m10miRONiOB5LYbeyE9PGo82gzQtyKM9J55WajHj2eOD","variables_values":str(otp),"route":"otp","numbers":str(mobile)}
            

            headers = {
                'cache-control': "no-cache"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            print(response.text)

            request.session['mobile']= user.mobile
            print("***************",user.mobile)
            
            request.session['otp'] = otp
            print("*************", otp)
            
            return render(request, 'OTP.html')
     
     except Exception as e:
         msg= "Invalid mobile number"
         print("***********", e)
         return render(request, 'FPass.html', {'msg':msg})
       

    else:
      return render(request, 'FPass.html')

def OTP(request):
    if request.method=="POST":
        
        try:
            uotp= int(request.POST['uotp'])
            otp= int(request.session['otp'])
            
            if otp==uotp:
                del request.session['otp']
                return render(request, 'New_Pass.html')
            
            else:
                msg= "Invalid OTP!!"
                return render(request, 'OTP.html', {'msg': msg})
        
        except Exception as e:
            print("**********", e)
            return render(request, 'OTP.html')
        
    else:
        return render(request, 'OTP.html')      

def New_Pass(request):
        if request.method=="POST":
            try:
                user= User.objects.get(mobile = request.session['mobile'])
                if request.POST['Npassword'] == request.POST['CNpassword']:
                    user.password= request.POST['Npassword']
                    user.save()
                    del request.session['mobile']
                    return redirect('Login')
                else:
                    msg= "New password & Confirm password doesn't match"                
                    return render(request, 'New_Pass.html', {'msg': msg})
            
            
            except Exception as e:
                print("**************", e)
                msg= "Invalid mobile"
                return render(request, 'New_Pass.html', {'msg': msg})
            
        else:
            return render(request, 'New_Pass.html')    

def CProfile(request):
    user= User.objects.get(email= request.session['email'])
          
    if request.method== "POST":
            print("POST Data:", request.POST)
            user.name= request.POST['name']
            user.mobile= request.POST['mobile']
                    
            try:
                print("************")
                user.uprofile= request.FILES['uprofile']
                user.save()
                print("****************", user.uprofile)
                request.session['uprofile']= user.uprofile.url  
                if user.usertype=="buyer":
                    return redirect('index')
                else:
                    return redirect('sindex')

            except Exception as e:
               print("*****************", e)
               return redirect('index')
        
    else:
        if user.usertype=="buyer":
            return render(request, 'CProfile.html', {'user': user})
        else:           
            return render(request, 'scprofile.html', {'user': user})
def sindex(request):
    return render(request, 'sindex.html')

def scpass(request):
    return render(request, 'scpass.html')

def add(request):
    if request.method=="POST":
        Seller= User.objects.get(email=request.session['email'])
    
        try:
            Product.objects.create(
                Seller = Seller,
                Scategory= request.POST['Scategory'],
                Sbrand= request.POST['Sbrand'],
                Pname= request.POST['Pname'],
                Ssize= request.POST['Ssize'],
                Price= request.POST['Price'],
                Description= request.POST['Description'],
                Image= request.FILES['Image']
            )
            msg= "Product added successfully!!"
            return render(request, 'add.html', {'msg': msg})
            
        
        except Exception as e:
            print("***********", e)
            msg= "error"
            return render(request, 'add.html', {'msg': msg})

    else:
          return render(request, 'add.html')
    
def view(request):
    Seller= User.objects.get(email=request.session['email'])
    products = Product.objects.filter(Seller=Seller) 
    return render(request, 'view.html', {'products': products})

def update(request, pk):
     Seller = User.objects.get(email=request.session['email'])
     product = Product.objects.get(pk=pk)

     if request.method== "POST":

             product.Scategory = request.POST['Scategory']
             product.Sbrand = request.POST['Sbrand']
             product.Ssize = request.POST['Ssize']
             product.Price = request.POST['Price']
             product.Description = request.POST['Description']
             product.Pname = request.POST['Pname']
             product.save()

             try:
                 product.Image = request.FILES['Image']
                 
             
             except:
                 pass
             
             return redirect('sindex')
     
     else:
            return render(request, 'update.html', {'product': product})  
     
def delete(request, pk):
    Seller= User.objects.get(email=request.session['email'])
    product= Product.objects.get(pk=pk)
    product.delete()
    return redirect('sindex')

def mdetails(request, pk):
    w= False
    user= User.objects.get(email= request.session['email'])
    product= Product.objects.get(pk=pk)
    
    try:
        wishlist= Wishlist.objects.get(user=user, product=product)
        w = True
    except:
        pass

    return render(request, 'mdetails.html', {'product': product, 'w': w})

def addwish(request, pk):
     try:
        user= User.objects.get(email= request.session['email'])
        product= Product.objects.get(pk=pk)

        Wishlist.objects.create(
            user=user,
            product = product
        
        )

        return redirect('wishlist')

     except Exception as e:
        print("****************",e)
        return redirect('index')
    

def wishlist(request):
    user= User.objects.get(email= request.session['email'])
   
    wishlist = Wishlist.objects.filter(user=user)
    return render(request,'wishlist.html', {'wishlist':wishlist})

def dwishlist(request, pk):
    user= User.objects.get(email= request.session['email'])
    product = Product.objects.get(pk=pk)
    
    wishlist= Wishlist.objects.get(user=user, product=product)
    wishlist.delete()

    return redirect('wishlist')

def addcart(request, pk):
    user= User.objects.get(email= request.session['email'])
    product= Product.objects.get(pk=pk)

    Cart.objects.create(
        user= user,
        product= product,
        qty = 1,
        price = product.price,
        total = product.price
    )
    return redirect('cart')


def cart(request):

    user = User.objects.get(email = request.session['email'])
    cart = Cart.objects.filter(user= user)

    total = sum(item.price for item in cart)
    net = 0

    for i in cart:
        net+= i.price

    client = razorpay.Client(auth = (settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    payment = client.order.create({'amount': net * 100, 'currency': 'INR', 'payment_capture':1})

    context = {
                'cart' : cart,
                'net' : net,
                'payment' : payment,
                #'book':book, #Ensure the amount is in paise
                }

    return render(request, 'cart.html', {'cart':cart, 'net': net, 'context': context})


def dcart(request, pk):
    user = User.objects.get(email = request.session['email'])

    cart = Cart.objects.get(pk=pk)
    cart.delete()

    return redirect('cart')

