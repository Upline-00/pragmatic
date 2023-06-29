from django.urls import path

from commentapp.views import CommentCreateView

app_name = 'commentapp'

urlpatterns = [
    path('create/', CommentCreateView.ac_view(), name="create"),

]