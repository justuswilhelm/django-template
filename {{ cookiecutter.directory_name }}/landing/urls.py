"""Landing app URLpatterns."""
from django.conf.urls import url
from django.views.generic import TemplateView

from .views import LandingView, FAQView, TOSView, ImprintView

urlpatterns = (url(r'^$', LandingView.as_view(), name='landing'),
               url(r"^faq/$", FAQView.as_view(), name="faq"),
               url(r"^imprint/$", ImprintView.as_view(), name="imprint"),
               url(r"^tos/$", TOSView.as_view(), name="tos"))