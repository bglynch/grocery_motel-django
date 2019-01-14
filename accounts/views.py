from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from checkout.models import OrderLineItem, Order


def register(request):
    '''Registers a new user or gets user the registration form'''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('username')
            user_password = form.cleaned_data.get('password1')

            user = auth.authenticate(username=user_name, password=user_password)
            auth.login(request, user)
            
            messages.success(
                request, 
                'Account created for {}!'.format(user_name)
                )
            return redirect('get_products')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


# function to view user profile page, if user is logged in
@login_required
def my_account(request):
    # get logged in user
    user_id = request.user.id

    # get users previous purchased products
    previous_orders = OrderLineItem.objects.filter(shopper=user_id)

    # get order numbers of the purchased products
    order_numbers = sorted(list(set(order.order_id for order in previous_orders)), reverse=True)

    # get a list of the customers previous orders
    customer_orders = [Order.objects.filter(id=number).first() for number in order_numbers]

    return render(request, 'accounts/my-account.html', {'customer_orders': customer_orders})
