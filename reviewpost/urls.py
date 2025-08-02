from django.urls import path
from .views import SignUpView, CustomLoginView, CustomLogoutView, listview, detailview, CreateClass, columnview, profileview, ProfileUpdateView, inboxview, message_detailview, send_messageview, like_review
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', listview, name='list'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('detail/<int:pk>', detailview, name='detail'),
    path('create/', CreateClass.as_view(), name='create'),
    path('column/', columnview, name='column'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('profile/<str:username>/', profileview, name='profile'),
    path('inbox/', inboxview, name='inbox'),
    path('message/<int:message_id>/', message_detailview, name='message_detail'),
    path('send-message/', send_messageview, name='send_message'),
    path('send-message/<str:recipient_username>/', send_messageview, name='send_message_to_user'),
    path('like/<int:review_id>/', like_review, name='like_review'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)