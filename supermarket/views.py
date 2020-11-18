from django.shortcuts import render, redirect
from .models import Products, Categories, Units, Students
from django.contrib import messages

# Create your views here.

def set_validate(request, field, sanitize):
    strings = ["\'", "\"", ";", ">", "<", "/", "(", ")", "{", "}"]
    try:
        if not request.POST[field] or request.POST[field].isspace():
            return None
    except:
        return None
    else:
        data = request.POST[field]
        if sanitize:
            for x in strings:
                data.replace(x, '')
        return data

def index(request):
    products = Products.objects.all()
    return render(request, 'index.html', {"products": products})


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    elif request.method == 'POST':
        if request.POST['password1'] != request.POST['password2']:
            messages.error(request, "Two Password does not matched!")
            return redirect('register')

        if Students.objects.filter(email=request.POST['email']):
            messages.error(request, "A client already registerd with this ID!")
            return redirect('register')

        #Inserting user in db
        S = Students (
            first_name = set_validate(request, 'first_name', sanitize=True),
            last_name = set_validate(request, 'last_name', sanitize=True),
            email = set_validate(request, 'email', sanitize=True),
            mobile = set_validate(request, 'mobile', sanitize=True),
            password = set_validate(request, 'password1', sanitize=False),
            )

        S.save() # Inserting user in database
        request.session['client'] = request.POST['email']
        messages.success(request, "Successfully registered!")
        return redirect('index')
    else:
        return None


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    elif request.method == 'POST':
        student_id = set_validate(request, 'email', sanitize=False)
        password = set_validate(request, 'password', sanitize=False)
        try:
            S = Students.objects.get(email=request.POST['email'])
            if S.password == password:
                request.session['client'] = request.POST['email']
                messages.success(request, 'Successfully logged in!')
                return redirect('index')
            else:
                messages.error(request, 'Password does not matched!')
                return redirect('login')
        except Exception as e:
            print(e)
            messages.error(request, 'Client does not exists!')
            return redirect('login')
    else:
        return None


def logout(request):
    try:
        del request.session['client']
        request.session.flush()
        messages.success(request, 'Successfully logged out!')
    except:
        messages.error(request, 'You are already logged out')
    return redirect('login')