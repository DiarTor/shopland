from django.shortcuts import render

from contact_module.forms import ContactUsForm


# Create your views here.

def contact_us_page(request):
    if request.method == "POST":
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            print(contact_form.changed_data)
    return render(request, 'contact_module/contact_us_page.html', {"contact_form": contact_form})
