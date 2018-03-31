from django.conf.urls import url
from Notification import views

app_name = 'Notification'

urlpatterns = [

    url(r'^Fac/(?P<fac_id>[0-9]+)/$' , views.FacHome , name="FacHome"),
]