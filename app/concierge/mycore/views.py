from django.core import serializers
from django.shortcuts import render

from .models import Tenant
from .serializers import queryset_serializer, object_serializer


def tenants(request):
    data = queryset_serializer(Tenant.objects.all())
    return render(request, 'tenants.html', {'data': data})


def tenant(request, tenant_id):
    obj = Tenant.objects.get(pk=tenant_id)
    data = object_serializer(obj)[0]['fields']
    return render(request, 'tenant.html', {'data': data})

