from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import tenants, tenant

static_patterns = static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT) + \
                  static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)

app_name = 'mycore'

urlpatterns = [
    path('', tenants, name='tenants'),
    path('<int:tenant_id>/', tenant, name='tenant'),
]
