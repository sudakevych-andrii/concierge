from django.views.generic import FormView, ListView, DetailView

from .models import Tenant, Room, Journal
from .forms import TenantForm, RoomForm, JournalForm
from .serializers import queryset_serializer


class TenantsView(ListView):
    model = Tenant
    data = queryset_serializer(Tenant.objects.all())
    template_name = 'tenants.html'

    def get_tenants(self):
        return self.data

    def get_context_data(self, **kwargs):
        context = super(TenantsView, self).get_context_data(**kwargs)
        context['form'] = TenantForm
        return context


class TenantView(DetailView):
    model = Tenant
    data = queryset_serializer(Tenant.objects.all())
    template_name = 'tenant.html'

    def get_tenant(self, tenant_id):
        return self.data[tenant_id]


class TenantFormView(FormView):
    template_name = 'forms/tenant_form.html'
    form_class = TenantForm
    success_url = '/core/tenants'

    def form_valid(self, form):
        form.save_tenant()
        return super(TenantFormView, self).form_valid(form)


class RoomsView(ListView):
    model = Room
    data = queryset_serializer(Room.objects.all())
    template_name = 'rooms.html'

    def get_rooms(self):
        return self.data

    def get_context_data(self, **kwargs):
        context = super(RoomsView, self).get_context_data(**kwargs)
        context['form'] = RoomForm
        return context


class RoomView(DetailView):
    model = Room
    data = queryset_serializer(Room.objects.all())
    template_name = 'room.html'

    def get_room(self, room_id):
        return self.data[room_id]


class RoomFormView(FormView):
    template_name = 'forms/room_form.html'
    form_class = RoomForm
    success_url = '/core/rooms'

    def form_valid(self, form):
        form.save_room()
        return super(RoomFormView, self).form_valid(form)


class JournalView(ListView):
    model = Journal
    data = queryset_serializer(Journal.objects.all())
    template_name = 'journal.html'

    def get_journal(self):
        return self.data

    def get_context_data(self, **kwargs):
        context = super(JournalView, self).get_context_data(**kwargs)
        context['tenants'] = Tenant.objects.all()
        context['rooms'] = Room.objects.all()
        return context


class JournalFormView(FormView):
    template_name = 'forms/journal_form.html'
    form_class = JournalForm
    success_url = 'core/journal'

    def form_valid(self, form):
        form.save_journal()
        return super(JournalFormView, self).form_valid(form)
