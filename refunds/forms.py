from django.forms import ModelForm, DateInput
from refunds.models import RefundRequest


class RefundRequestForm(ModelForm):
    class Meta:
        model = RefundRequest
        exclude = ['user', 'status', 'iban_verified']
        widgets = {
            'order_date': DateInput(attrs={'type': 'date',}),
        }
    # Additional fields and validation can be added
