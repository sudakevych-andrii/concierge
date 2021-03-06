from django.forms import Form, CharField, DateField, IntegerField
from django.utils import timezone

from .models import Tenant, Room, Journal


class TenantForm(Form):
    first_name = CharField()
    last_name = CharField()
    date_of_birth = CharField()
    phone = CharField()

    def save_tenant(self):
        tenant = Tenant(
            first_name=self.data['first_name'],
            last_name=self.data['last_name'],
            date_of_birth=self.data['date_of_birth'],
            phone=self.data['phone']
        )
        tenant.save()


class RoomForm(Form):
    number = IntegerField()
    max_tenants = IntegerField()

    def save_room(self):
        room = Room(
            number=self.data['number'],
            max_tenants=self.data['max_tenants']
        )
        room.save()


class JournalForm(Form):
    tenant_id = IntegerField()
    room_id = IntegerField()

    def save_journal(self):
        tenant = Tenant.objects.get(id=int(self.data['tenant_id']))
        room = Room.objects.get(id=int(self.data['room_id']))
        tenants_count = int(self.data['tenants_count'])
        journal = Journal(room=room, tenant=tenant, check_in_date=timezone.now(), tenants_count=tenants_count)
        journal.save()
