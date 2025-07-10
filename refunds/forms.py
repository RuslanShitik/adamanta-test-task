from django.forms import ModelForm, DateInput, ValidationError
from refunds.models import RefundRequest
from refunds.services import IBANService


class RefundRequestForm(ModelForm):
    class Meta:
        model = RefundRequest
        exclude = ['user', 'status', 'iban_verified']
        widgets = {
            'order_date': DateInput(attrs={'type': 'date',}),
        }

    def clean_iban(self):
        iban = self.cleaned_data.get('iban')
        if not iban:
            raise ValidationError("IBAN is required.")

        is_iban_valid = IBANService.validate_iban(iban)
        if not is_iban_valid:
            raise ValidationError("Invalid IBAN.")

        return iban
