from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View

from accounts.forms import SignUpForm


class SignUpView(View):
    template_name = 'registration/signup.html'
    form_class = SignUpForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("refund_list")
        return render(request, self.template_name, {'form': form})