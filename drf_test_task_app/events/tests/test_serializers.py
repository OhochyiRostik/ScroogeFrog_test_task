from django.test import TestCase

from events.models import Event
from events.serializers import EventSerializer
from users.models import User


class EventSerializerTestCase(TestCase):
    def test_serializer(self):
        organizer_user = User.objects.create(
            email='admin@gmail.com',
            password='admin',
        )
        event_1 = Event.objects.create(
            name='event 1',
            description='description 1',
            date='2024-05-04',
            location='location 1',
            organizer=organizer_user,
        )
        event_2 = Event.objects.create(
            name='event 2',
            description='description 2',
            date='2024-05-04',
            location='location 2',
            organizer=organizer_user,
        )
        data = EventSerializer([event_1, event_2], many=True).data
        expected_data = [
            {
                'id': event_1.id,
                'name': 'event 1',
                'description': 'description 1',
                'date': '2024-05-04',
                'location': 'location 1',
                'organizer': event_1.organizer.id,
            },
            {
                'id': event_2.id,
                'name': 'event 2',
                'description': 'description 2',
                'date': '2024-05-04',
                'location': 'location 2',
                'organizer': event_2.organizer.id,
            },
        ]
        self.assertEqual(expected_data, data)
