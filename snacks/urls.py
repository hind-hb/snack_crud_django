from django.urls import path

from .views import (SnackDeleteView, SnackDetailView,
                    SnackListView, SnackUpdateView, SnackAddNew)

urlpatterns = [
    path('', SnackListView.as_view(), name='home'),
    path('snack/<int:pk>/', SnackDetailView.as_view(), name='snack_detail'),
    path('snack/new/', SnackAddNew.as_view(), name='snack_new'),
    path('snack/<int:pk>/update/', SnackUpdateView.as_view(), name='snack_update'),
    path('snack/<int:pk>/delete/', SnackDeleteView.as_view(), name='snack_delete')
]