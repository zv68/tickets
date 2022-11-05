from django.http import HttpResponse
from django.views.generic import TemplateView

from base.models import Event


# Create your views here.
# Create your views here.
def hello(request):
    s = request.GET.get('s', '')
    return HttpResponse(f'Hello, {s} world!')

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

        context.update(
            "events": events,
            #"cart": cart
        })

        return context
#def filter():
    #pass

'''
def events(request, pk):
    event = Event.objects.get(id=pk)
    #messages = event.message_set.all()

     # GET
    context = {'room': event, 'messages': messages}
    return render(request, 'base/room.html', context)
    '''