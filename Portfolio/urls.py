from django.urls import path
from .views import (
	PortFolioListView
)

urlpatterns = [
    path('', PortFolioListView.as_view(), name='portfolio'),
]