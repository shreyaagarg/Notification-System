from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$' , TemplateView.as_view(template_name='index.html') , name="index"),
    url(r'accounts/', include('accounts.urls')),
    url(r'home/', include('Notification.urls')),
]