from django.shortcuts import render
from django.views import generic, View
from .models import Request
from .forms import RequestForm
from django.contrib import messages
from django.utils.text import slugify

# Create your views here.
class RequestList(generic.ListView):
    model = Request
    queryset = Request.objects.filter(active=True).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

class Request(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            "new_request.html",
            {
                "request_form": RequestForm()
            }
        )

    def post(self, request, *args, **kwargs):
        request_form = RequestForm(data=request.POST)
        if request_form.is_valid():
            request_form.instance.requester = request.user
            slug_str = request.user.username + '-' + request_form.instance.requested_item + '-' + request_form.instance.required_date.strftime("%d%m%Y")
            request_form.instance.slug = slugify(slug_str)
            new_request = request_form.save()
            messages.add_message(request, messages.SUCCESS, 'Request Created!')
        else:
            request_form = RequestForm()
            messages.add_message(request, messages.ERROR, 'Request Failed')

        return render(
            request,
            "new_request.html",
            {
                "request_form": RequestForm()
            }
        )