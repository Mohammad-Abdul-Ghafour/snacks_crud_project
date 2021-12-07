from django.urls import path
from .views import SnackDetailsView,SnackListView,CreateSnackView,DeleteSnackView,UpdateSnackView

urlpatterns = [
    path('',SnackListView.as_view(),name="snack_list"),
    path('<int:pk>/',SnackDetailsView.as_view(),name="snack_details"),
    path('create/',CreateSnackView.as_view(),name="create_snack"),
    path('<int:pk>/delete/',DeleteSnackView.as_view(),name="delete_snack"),
    path('<int:pk>/update/',UpdateSnackView.as_view(),name="update_snack")
]