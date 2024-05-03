from rest_framework.serializers import ModelSerializer

from drf_test_task_app.events.models import Event


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
