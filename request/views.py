from django.shortcuts import render
from django.views import generic, View
from .models import Request
from .forms import RequestForm

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
        request_form = RequestForm(data=request.post)
        if request_form.is_valid():
            request_form.instance.requester = request.user.username
            new_request = request_form.save()
        else:
            request_form = RequestForm()

        return render(
            request,
            "request_detail.html",
            {
                "request": new_request
            },
        )