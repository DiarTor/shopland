from django.urls import path
from contact_module.views import contact_us_page
urlpatterns = [
    path('', contact_us_page)
]