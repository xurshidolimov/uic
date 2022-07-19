from django.urls import path
from .views import AllStudentView, DetailStudentView, FilterStudentView, MetsenatView
urlpatterns = [
    path('', AllStudentView.as_view()),
    path('<int:id>/', DetailStudentView.as_view()),
    path('filter/', FilterStudentView.as_view()),
    path('metsenat/<int:id>/', MetsenatView.as_view()),
]