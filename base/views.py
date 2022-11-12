from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
from base.models import Event


# Create your views here.
# Create your views here.
#---------------------------------------------------------------------------------
#------------------------ HELLO, ABOUT US AND CONTACT US VIEWS START --------------------
#---------------------------------------------------------------------------------

def hello(request):
    s = request.GET.get('s', '')
    return HttpResponse(f'Hello, {s} world!')


def aboutus_view(request):
    return render(request,'aboutus.html')



class HomepageView(TemplateView):
    template_name = "homepage.html"
    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        category = self.request.GET.get("category")

        if category:
            events = Event.objects.filter(category=category)
        else:
            events = Event.objects.all()

        #if self.request.user.is_authenticated:
        #   cart, created = Cart.objects.get_or_create(user=self.request.user)
        #else:
        #    cart = None
        context.update({
            "events": events,
            #"cart": cart
        })
        return context
#def filter():
    #pass
# for checkout of cart
def cart_view(request):
    #for cart counter
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    # fetching product details from db whose id is present in cookie
    products=None
    total=0
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids != "":
            product_id_in_cart=product_ids.split('|')
            products=models.Product.objects.all().filter(id__in = product_id_in_cart)

            #for total price shown in cart
            for p in products:
                total=total+p.price
    return render(request,'ecom/cart.html',{'products':products,'total':total,'product_count_in_cart':product_count_in_cart})


'''
def events(request, pk):
    event = Event.objects.get(id=pk)
    #messages = event.message_set.all()

     # GET
    context = {'room': event, 'messages': messages}
    return render(request, 'base/room.html', context)
    '''