from django.urls import path, include
from watchlist_app.views import WatchListAPIView, WatchDetailAPIView, StreamPlatformAPIView, StreamPlatformDetailAPIView,\
    ReviewAPIView, ReviewDetailAPIView, ReviewCreate


urlpatterns = [
    path('list/', WatchListAPIView.as_view()),
    path('<int:pk>/', WatchDetailAPIView.as_view()),
    path('stream/<int:pk>/', StreamPlatformDetailAPIView.as_view()),
    path('stream/', StreamPlatformAPIView.as_view()),
    path('review/', ReviewAPIView.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetailAPIView.as_view(), name='review-detail'),
    path('<int:pk>/review/', ReviewAPIView.as_view(), name='review-list'),
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('review/<int:pk>/', ReviewDetailAPIView.as_view(), name='review-detail'),
]
