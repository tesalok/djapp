from django.urls import path
from ebooks.api.views import EbookListCreateAPIView,EbookDetailAPIView,ReviewCreateAPIView,ReviewDetailAPIView

urlpatterns=[
    path("",EbookListCreateAPIView.as_view(),name="ebook-list"),
    path("<int:pk>/",EbookDetailAPIView.as_view(),name="ebook-detail"),
    path("<int:ebook_pk>/review/",ReviewCreateAPIView.as_view(),name="review-list"),
    path("review/<int:pk>/",ReviewDetailAPIView.as_view(),name="review-detail")
]