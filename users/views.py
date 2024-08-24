from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404, redirect

from django.contrib import messages

from django.urls import reverse_lazy

from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import RegisterCustomUserForm, LoginCustomUserForm


class RegisterCustomUserView(SuccessMessageMixin, CreateView):
    form_class = RegisterCustomUserForm
    template_name: str = "users/register_custom_user.html"
    success_url: str = reverse_lazy("login")
    success_message: str = "Вы успешно зарегистрировались!"
    extra_context = {"title": "Регистрация"}

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password1"])
        user.save()
        return super().form_valid(form)


class LoginCustomUserView(SuccessMessageMixin, LoginView):
    form_class = LoginCustomUserForm
    template_name: str = "users/login_custom_user.html"
    success_url: str = reverse_lazy("home")
    success_message: str = "Вы успешно вошли в систему!"
    extra_context = {"title": "Авторизация"}

    def get_form(self, form_class=None):
        return self.form_class()

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)

            if user:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Неверные учетные данные.")

        return render(request, self.template_name, {"form": form})


def home(request):
    return render(request, "users/home.html")
