from django.urls import path
from .views import VerifyMobileAPIView, GetUserProfileAPIView, UserProfileUpdateAPIView, ApplicantSubmissionView,ApplicantListView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('verify/', VerifyMobileAPIView.as_view(), name='verify_Mobile'),
    path('profile/<int:pk>/', GetUserProfileAPIView.as_view(),
         name='user-profile-detail'),
    path('updateprofile/<int:pk>/',
         UserProfileUpdateAPIView.as_view(), name='update_profile'),
    path('submit-applicant/', ApplicantSubmissionView.as_view(),
         name='submit_applicant'),
    path('applicants/', ApplicantListView.as_view(), name='applicant-list'),
]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
