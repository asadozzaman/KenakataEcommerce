from django.shortcuts import render
from  django.views.generic import ListView,DetailView
from store.models import Category,Product
# Create your views here.

class HomeListView(ListView):
    model = Product
    template_name = 'store/index.html'
    context_object_name = 'products'


# def home(request):
#     return render(request,'store/index.html')

# def product_details(request,pk):
#     item = Product.objects.get(id=pk)
#     context = {
#         'item': item
#     }
#     return render(request,'store/product.html',context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product.html'
    context_object_name = 'item'
