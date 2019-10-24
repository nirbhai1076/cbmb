from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home/home.html"
    

class AboutView(TemplateView):
    template_name = "home/about.html"

class PrivacyView(TemplateView):
    template_name = "home/privacy.html"

class ContactView(TemplateView):
    template_name = "home/contact.html"