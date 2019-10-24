from django.urls import path
from home.views import HomeView , AboutView ,PrivacyView ,ContactView

urlpatterns = [
    path('', HomeView.as_view(), name = 'home' ),
    path('about/', AboutView.as_view(), name = 'about' ),
    path('privacy/', PrivacyView.as_view(), name = 'privacy' ),
    path('contact/', ContactView.as_view(), name = 'contact' ),
    ]
