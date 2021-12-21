
from django.contrib import admin
from django.urls import path
from send_email.views import ReviewEmailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reviews/' , ReviewEmailView.as_view(), name="reviews")
]
