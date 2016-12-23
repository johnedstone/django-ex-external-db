from django.conf.urls import url
from customers.views import CustomerListView

urlpatterns = [
    url(r'^$', CustomerListView.as_view(), name='list'),
]
