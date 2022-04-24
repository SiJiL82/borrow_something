from .models import Request
from django import forms

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('requested_item', 'details', 'required_date', 'required_duration')
    
    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        self.fields['requested_item'].label = 'I would like to borrow:'
        self.fields['details'].label = 'More details:'
        self.fields['required_date'].label = 'On this day:'
        self.fields['required_duration'].label = 'For this many days:'