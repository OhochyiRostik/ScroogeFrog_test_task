from rest_framework.viewsets import ModelViewSet

from drf_test_task_app.events.models import Event
from drf_test_task_app.events.serializers import EventSerializer


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

