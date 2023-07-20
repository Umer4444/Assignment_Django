from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .models import *
from .forms import OrderForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt




def home(request):
    return render(request, 'home.html')

def howitworks(request):
    return render(request, 'howitworks.html')

def reviews(request):
    return render(request, 'reviews.html')

def blog(request):
    return render(request, 'blog.html')

def homeworkanswer(request):
    return render(request, 'homeworkanswer.html')
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('home')
    else:
        form = OrderForm()
    
    return render(request, 'account/signup.html', {'form': form})

def login(request):
    return render(request, 'account/login.html')

def submit(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('home')
    else:
        form = OrderForm()
    
    return render(request, 'submit.html', {'form': form})

def economics(request):
    return render(request, 'economics.html')

def engineering(request):
    return render(request, 'engineering.html')

def mathematics(request):
    return render(request, 'mathematics.html')

def physics(request):
    return render(request, 'physics.html')

def programming(request):
    return render(request, 'programming.html')

def orders(request):
    order = Order.objects.filter(user=request.user)
    context = {'order': order}
    return render(request, 'orders.html', context)

def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    messages.info(request, 'Order deleted successfully.')
    return redirect('orders')