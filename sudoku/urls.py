from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

from . import views

urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+[
    url(r'^$', views.index, name='index'),
    url(r'^verify.json$', views.verify, name='verify'),
#//    url(r'^.*$', RedirectView.as_view(url='/', permanent=False), name='redirect'),
]