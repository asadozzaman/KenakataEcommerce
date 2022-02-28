from django.shortcuts import render
from django.http import HttpResponse
from account.forms import RegistrationForm

#auth function

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate


from order.models import Cart, Order
from payment.models import BillingAddress
from payment.forms import BillingAddressForm
from account.models import Profile

from django.views.generic import TemplateView

# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return HttpResponse('You are authenticated')
    else:
        form = RegistrationForm()
        if request.method == 'post' or request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse('your account has been created')
    context = {
        'form': form
    }

    return render(request,'register.html',context)

def CustomerLogin(request):
    if request.user.is_authenticated:
        return HttpResponse("you are login in")
    else:
         if request.method == 'POST' or request.method == 'post':
             username = request.POST.get('username')
             password = request.POST.get('password')
             customer = authenticate(request,username=username,password=password)
             if customer is not None:
                login(request,customer)
                return HttpResponse("You are login in succesfully")
             else:
                return HttpResponse("404")

    return render(request,'login.html')


# customers profile

class ProfileView(TemplateView):
    def get(self, request, *args, **kwargs):
        orders = Order.objects.filter(user=request.user, ordered=True)
        billingaddress = BillingAddress.objects.get(user=request.user)
        billingaddress_form = BillingAddressForm(instance=billingaddress)


        context = {
            'orders': orders,
            'billingaddress': billingaddress_form,
        }
        return render(request, 'profile.html', context)


    def post(self, request, *args, **kwargs):
        pass


