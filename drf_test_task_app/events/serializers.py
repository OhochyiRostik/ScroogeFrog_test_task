from rest_framework.serializers import ModelSerializer

from events.models import Event, Registration


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class RegistrationSerializer(ModelSerializer):
    class Meta:
        model = Registration
        fields = ('event', 'registration')
