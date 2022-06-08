from django.urls import path
from .views import LocatorIPView

urlpatterns = [
    path(r'', LocatorIPView.as_view(), name='locator'),
]