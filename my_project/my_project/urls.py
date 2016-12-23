from django.conf.urls import url, include
from customers.views import index, health

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='home'),
    url(r'^health$', health, name='health'),
    url(r'^customers/', include('customers.urls', namespace='customers')),
]

from django.conf import settings

if settings.DEBUG or settings.FORCE_SQLITE:
    import debug_toolbar
    urlpatterns += [
      url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
