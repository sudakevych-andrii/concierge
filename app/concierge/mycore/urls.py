from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from .views import TenantsView, TenantView, RoomsView, RoomView, RoomFormView, TenantFormView, JournalView, \
    JournalFormView

static_patterns = static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT) + \
                  static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)

app_name = 'mycore'

tenants_patterns = ([
    path('tenants', TenantsView.as_view(), name='tenants'),
    path('tenants/create', TenantFormView.as_view(), name='tenant_form'),
    path('tenants/<pk>/', TenantView.as_view(), name='tenant'),
])

rooms_patterns = ([
    path('rooms', RoomsView.as_view(), name='rooms'),
    path('rooms/create', RoomFormView.as_view(), name='room_form'),
    path('rooms/<pk>/', RoomView.as_view(), name='room'),
])

journal_patterns = ([
    path('journal', JournalView.as_view(), name='journal'),
    path('journal/create', JournalFormView.as_view(), name='journal_form')
])

urlpatterns = tenants_patterns + rooms_patterns + journal_patterns
