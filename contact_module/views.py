from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactUsModelForm
from django.views.generic.edit import FormView, CreateView

from .models import ContactUs


class ContactUsView(CreateView):
    form_class = ContactUsModelForm
    template_name = 'contact_module/contact_us_page.html'
    success_url = '/contact-us/'


class CreateProfileView(View):
    def get(self, request):
        return render(request, 'contact_module/create_profile_page.html')

    def post(self, request):
        print(request.FILES)
        return redirect('/contact-us/create-profile')
