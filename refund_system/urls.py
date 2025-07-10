from django.contrib import admin
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView
)
from django.urls import path

from accounts.views import SignUpView
from refunds.views import (
    RefundRequestListView, CreateRefundRequestView,
    RefundRequestDetailView, ValidateIBANView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('refunds/', RefundRequestListView.as_view(), name='refund_list'),
    path('refunds/create/', CreateRefundRequestView.as_view(), name='create_refund'),
    path('refunds/<int:pk>/', RefundRequestDetailView.as_view(), name='refund_detail'),
    path('api/validate-iban/', ValidateIBANView.as_view(), name='validate_iban'),

    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

handler404 = 'refund_system.views.custom_404_view'