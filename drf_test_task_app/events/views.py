from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from events.models import Event, Registration
from events.serializers import EventSerializer, RegistrationSerializer


class EventViewSet(ModelViewSet):
    """
    The class provides CRUD operations for events, search, filtering, and ordering.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'description']


class RegisterEvent(UpdateModelMixin, GenericViewSet):
    """
    The class allows users to register for events.
    """
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'event'

    def get_object(self):
        """
        Gets the registration object for the current user and event.

        :return: Object of registration
        """
        obj, _ = Registration.objects.get_or_create(user=self.request.user,
                                                    event_id=self.kwargs['event'])
        return obj
