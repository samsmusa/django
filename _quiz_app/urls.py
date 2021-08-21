
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quizes.urls', namespace='quizes')),
    path('account/', include('users.urls', namespace='users')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
