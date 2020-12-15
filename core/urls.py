from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from personal.views import home_screen_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_page, name='home'),
    path('account/', include('account.urls'), name='account'),
    path('blog/', include('blog.urls', namespace='blog')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)