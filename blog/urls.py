from django.urls import path
from .views import AplicationSponsorView, DetailSponsorView, AllSponsorView, FilterSponsorView, DashboardView


urlpatterns=[
    path('aplication/', AplicationSponsorView.as_view()),
    path('sponsor/<int:id>/', DetailSponsorView.as_view()),
    path('all_sponsor/', AllSponsorView.as_view()),
    path('', DashboardView.as_view()),
    path('sponsor/filter/', FilterSponsorView.as_view()),
]