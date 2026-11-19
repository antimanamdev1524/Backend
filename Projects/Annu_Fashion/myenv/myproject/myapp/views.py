from django.shortcuts import render, redirect
from .models import*
import requests
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

# def contact(request):
#     return render(request, 'contact.html')

def cpass(request):
    if request.method== "POST":
        
        try:
            user= User.objects.get(email= request.session['email'])
            
            if user.password== request.POST['opassword']:
                if request.POST['npassword']== request.POST['cnpassword']:
                    user.password= request.POST['npassword']
                    user.save()
                    return redirect('logout')
                else:
                    msg= "Password & confirm password doesn't match!!"
                    return render(request, 'cpass.html', {'msg': msg})
            
            else:
                msg= "old password doesn't match!!"
                return render(request, 'cpass.html', {'msg': msg})
            
        except:
            pass
    
    else:
        return render(request, 'cpass.html')
    
def blog(request):
    return render(request, 'blog.html')

def signup(request):
    if request.method == "POST":
       try:
          user = User.objects.get(email= request.POST['email'])
          msg = "Email already exists!!"
          return render(request, 'signup.html', {'msg':msg})
       except:
          if request.POST['password']== request.POST['cpassword']:
             User.objects.create(
                name= request.POST['name'],
                email= request.POST['email'],
                mobile= request.POST['mobile'],
                password= request.POST['password'],
                profile= request.FILES['profile']
          )
             msg = "signup successfully!!"
             return render(request, 'login.html', {'msg': msg})
            
          else:
            msg= "Password and confirm password does not match!!"
            return render(request, 'signup.html', {'msg':msg})

    else:
        return render(request, 'signup.html')


def login(request):
   if request.method== "POST":
        
        try:
            user= User.objects.get(email= request.POST['email'])
           
            if user.password== request.POST['password']:
               request.session['email']= user.email
               request.session['profile']= user.profile.url
               return redirect('index')
            
            else:
                msg= 'Invalid Password'
                return render(request, 'login.html', {'msg': msg})
            
        except:
           msg= 'Invalid Email'
           return render(request, 'login.html', {'msg': msg})

   else:
        return render(request, 'login.html') 
    

def logout(request):
    del request.session['email']
    del request.session['profile']
    return redirect('login')

def fpass(request):
    if request.method=="POST":
        try: 
            user= User.objects.get(mobile=request.POST['mobile'])
            mobile= request.POST['mobile']
            otp = random.randint(1000, 9999)
            
            url = "https://www.fast2sms.com/dev/bulkV2"
 
            querystring = {"authorization":"TcqwTbtYbjggBz35DusxGLuo9P1HpRgf6Q1tBpxMaBUSw7qOH1tIEO49xdeY","variables_values":str(otp),"route":"otp","numbers":str(mobile)}

            
            headers = {
                'cache-control': "no-cache"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            print(response.text) 

            request.session['mobile']= user.mobile 
            print("****************", user.mobile)

            request.session['otp']=otp     
            print("**************", otp)

            return render(request, 'otp.html')
        
        except Exception as e:
            msg= "Invalid mobile number"
            print("*************", e)
            return render(request, 'fpass.html', {'msg': msg})            

    else:
        return render(request, 'fpass.html')


def otp(request):
    # if request.method== "POST":
     try:
        uotp = int(request.POST['uotp'])
        otp = int(request.session['otp'])

        if otp == uotp:
            del request.session['otp']
            return render(request, 'newpass.html')

        else:
            msg= "Invalid otp"
            return render(request, 'otp.html', {'msg': msg})
    
     except Exception as e:
        print("***************", e)
        return render(request, 'otp.html')

    # else:
    #   return render(request, 'otp.html')


def newpass(request):
    if request.method== "POST":
        try:
            user= User.objects.get(mobile=request.session['mobile'])
            print("****************", user)
            if request.POST['npassword']== request.POST['cnpassword']:
               user.password = request.POST['npassword']
               user.save()
               del request.session['mobile'] 
               return redirect('login')

            else:
                msg= "New password & confirm password doesn't match" 
                return render(request, 'newpass.html', {'msg':msg})
            
        
        except Exception as e:
            print("***********", e)
            return render(request, 'newpass.html')  

    else:
        return render(request, 'newpass.html')


def cprofile(request):
    user= User.objects.get(email=request.session['email'])
    if request.method=="POST":
        try:
            user.name= request.POST['name']
            user.mobile=request.POST['mobile']
            user.save()
            return redirect('index')
        except:
            pass
    else:
        return render(request, 'cprofile.html', {'user':user})


