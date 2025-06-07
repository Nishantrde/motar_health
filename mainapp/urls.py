from django.urls import path
from .views import Index, RC_info

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('RC_info', RC_info.as_view(), name='RC_info')
]
