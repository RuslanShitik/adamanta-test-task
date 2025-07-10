from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from rest_framework.response import Response
from rest_framework.views import APIView

from refunds.forms import RefundRequestForm
from refunds.models import RefundRequest
from refunds.services import IBANService


class RefundRequestListView(LoginRequiredMixin, ListView):
    model = RefundRequest
    template_name = 'refunds/list.html'
    context_object_name = 'refund_requests'
    paginate_by = 1 # Test pagination

    def get_queryset(self):
        return RefundRequest.objects.filter(user=self.request.user)


class CreateRefundRequestView(LoginRequiredMixin, CreateView):
    model = RefundRequest
    form_class = RefundRequestForm
    template_name = 'refunds/create.html'
    success_url = reverse_lazy('refund_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RefundRequestDetailView(DetailView):
    model = RefundRequest
    template_name = 'refunds/detail.html'


class ValidateIBANView(APIView):

    def get(self, request):
        iban = request.query_params.get('iban', '')
        is_valid = IBANService.validate_iban(iban)
        if is_valid:
            return Response(
                {"message": "IBAN is valid."}, status=200
            )
        else:
            return Response(
                {"message": "IBAN is invalid."}, status=400
            )