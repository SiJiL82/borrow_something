from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BorrowRequest(models.Model):
    slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    requester = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="requests")
    requested_item = models.CharField(max_length=50)
    details = models.TextField()
    required_date = models.DateField()
    required_duration = models.IntegerField(default=1)
    active = models.BooleanField(default=True)
    accepted_response = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.requester} requested {self.requested_item}"


class BorrowResponse(models.Model):
    borrow_request = models.ForeignKey(
        BorrowRequest, on_delete=models.CASCADE, related_name='borrow_responses')
    responder = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='borrow_responder')
    created_on = models.DateTimeField(auto_now_add=True)
    details = models.TextField()
    accepted = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.responder} can lend {self.borrow_request.requested_item}"


class AcceptedResponse(models.Model):
    borrow_response = models.ForeignKey(
        BorrowResponse, on_delete=models.CASCADE, related_name='borrow_response')
    created_on = models.DateTimeField(auto_now_add=True)
    details = models.TextField()

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.borrow_response.responder}'s response accepted"
