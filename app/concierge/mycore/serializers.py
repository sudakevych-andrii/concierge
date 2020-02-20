import json

from django.core import serializers


def queryset_serializer(model):
    return json.loads(serializers.serialize('json', model))


def object_serializer(model):
    return json.loads(serializers.serialize('json', [model], ensure_ascii=False))
