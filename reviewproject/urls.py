from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.views.generic import RedirectView

def favicon_view(request):
    # 空のレスポンスを返してfavicon.icoリクエストを処理
    return HttpResponse(status=204)

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',include('reviewpost.urls')),
    path('favicon.ico', favicon_view, name='favicon'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)