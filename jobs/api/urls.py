
from django.urls import path
from jobs.api.views import JobsListCreateAPIView,JobsDetailCreateAPIView


urlpatterns = [
    path("",JobsListCreateAPIView.as_view(),name="job-list"),
    path("<int:pk>/",JobsDetailCreateAPIView.as_view(),name="job-detail")
    # path("<int:pk>/",jobs_detail_api_view,name='job-detail')
]