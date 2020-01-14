from django.core.exceptions import ValidationError
from django.db.models import Model, CASCADE, IntegerField, CharField, ForeignKey, BooleanField, DateTimeField, \
    TextField, SET_NULL

MAX_NAME_LENGTH = 80


class Tenant(Model):
    first_name = CharField(max_length=MAX_NAME_LENGTH)
    last_name = CharField(max_length=MAX_NAME_LENGTH)

    def full_name(self):
        vals = ' '.join([self.first_name or '', self.last_name or ''])
        if vals.strip():
            return vals
        return self.pk

    def __str__(self):
        return self.full_name()


class Room(Model):
    number = IntegerField()
    max_tenants = IntegerField('Maximum guests')
    tenant = ForeignKey(Tenant, null=True, blank=True, on_delete=SET_NULL)
    is_free = BooleanField(default=True)

    def __str__(self):
        return f'{self.number}'


class Journal(Model):
    room = ForeignKey(Room, on_delete=CASCADE)
    tenant = ForeignKey(Tenant, on_delete=CASCADE)
    tenants_count = IntegerField(null=True, blank=True)
    check_in_date = DateTimeField(null=True, blank=True, db_index=True)
    check_out_date = DateTimeField(null=True, blank=True, db_index=True)
    notes = TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.room}, {self.tenant}, {self.tenants_count}, {self.check_in_date}, {self.check_out_date}'

    def take_room(self):
        self.room.is_free = False
        self.room.tenant = self.tenant
        self.room.save()

    def free_room(self):
        self.room.is_free = True
        self.room.tenant = None
        self.room.save()

    def save(self, *args, **kwargs):
        if self.check_out_date:
            self.free_room()
        else:
            if self.tenants_count <= self.room.max_tenants:
                self.take_room()
            else:
                raise ValidationError(f'Maximum count of guests {self.room.max_tenants}')
        super().save(*args, **kwargs)
