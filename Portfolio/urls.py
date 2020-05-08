from django.urls import path
from .views import (
	PortFolioListView
)
from . import views

urlpatterns = [
	path('', views.home, name = 'home'),
    path('portfolio/', PortFolioListView.as_view(), name='portfolio'),
]