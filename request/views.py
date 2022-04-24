from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse
from django.views import generic, View
from .models import BorrowRequest, BorrowResponse
from .forms import RequestForm, ResponseForm
from django.contrib import messages
from django.utils.text import slugify
from datetime import datetime

# Create your views here.
class RequestList(generic.ListView):
    model = BorrowRequest
    context_object_name = 'request_list'
    template_name = 'index.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = self.model.objects.filter(active=True).order_by('-required_date')
        if self.request.user.is_authenticated:
            return queryset.exclude(requester=self.request.user)
        return queryset

class NewRequest(View):
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
            slug_str = request.user.username + '-' + request_form.instance.requested_item + '-' + request_form.instance.required_date.strftime("%d%m%Y") + '-' + datetime.now().strftime("%H%M%S")
            request_form.instance.slug = slugify(slug_str)
            new_request = request_form.save()
            messages.add_message(request, messages.SUCCESS, 'Request Created!')
        else:
            request_form = RequestForm()
            messages.add_message(request, messages.ERROR, 'Request Failed')

        return HttpResponseRedirect(reverse('request_detail', args=[new_request.slug]))

class RequestDetail(View):
    def get(self, request, slug, *args, **kwargs):
        borrow_request = get_object_or_404(BorrowRequest.objects, slug=slug)
        responses = borrow_request.borrow_responses.order_by('created_on')

        return render(
            request,
            "request_detail.html",
            {
                "borrow_request": borrow_request,
                "borrow_responses": responses,
                "response_form": ResponseForm()
            },
        )
    
    def post(self, request, slug, *args, **kwargs):
        borrow_request = get_object_or_404(BorrowRequest.objects, slug=slug)
        responses = borrow_request.borrow_responses.order_by('created_on')

        response_form = ResponseForm(data=request.POST)
        if response_form.is_valid():
            response_form.instance.responder = request.user
            borrow_response = response_form.save(commit=False)
            borrow_response.borrow_request = borrow_request
            borrow_response.save()
            messages.add_message(request, messages.SUCCESS, 'Response Added!')
        else:
            response_form = ResponseForm()
            messages.add_message(request, messages.ERROR, 'Could Not Add Response.')
        
        return render(
            request,
            "request_detail.html",
            {
                "borrow_request": borrow_request,
                "borrow_responses": responses,
                "response_form": ResponseForm()
            },
        )

class MyRequestList(generic.ListView):
    model = BorrowRequest
    context_object_name = 'request_list'
    template_name = 'my_requests.html'
    paginate_by = 6

    def get_queryset(self):
        return self.model.objects.filter(requester=self.request.user).order_by('-created_on')

class CancelBorrowRequest(View):
    def post(self, request, slug):
        borrow_request = get_object_or_404(BorrowRequest, slug=slug)
        borrow_request.active = False
        borrow_request.save()
        messages.add_message(request, messages.SUCCESS, 'Request Cancelled')
        
        return HttpResponseRedirect(reverse('request_detail', args=[slug]))

class AcceptResponse(View):
    def post(self, request, slug):
        borrow_request = get_object_or_404(BorrowRequest, slug=slug)
        response_id = request.POST.get('accept_response')
        borrow_response = get_object_or_404(BorrowResponse, id=response_id)
        borrow_response.accepted = True
        borrow_response.save()
        borrow_request.accepted_response = True
        borrow_request.save()
        messages.add_message(request, messages.SUCCESS, 'Response Accepted!')

        return HttpResponseRedirect(reverse('request_detail', args=[slug]))