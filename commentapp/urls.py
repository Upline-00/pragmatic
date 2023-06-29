from django.urls import path

from commentapp.views import CommentCreateView, CommentDeleteView

app_name = 'commentapp'

urlpatterns = [
    path('create/', CommentCreateView.ac_view(), name="create"),
    path('delete/<int:pk>', CommentDeleteView.ac_view(), name="delete"),
]