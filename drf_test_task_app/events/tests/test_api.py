import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from events.models import Event
from events.serializers import EventSerializer
from users.models import User


class EventsApiTestCase(APITestCase):
    def setUp(self):
        self.organizer_user = User.objects.create(
            email='admin@gmail.com',
            password='admin',
        )
        self.event_1 = Event.objects.create(
            name='event 1',
            description='description 1',
            date='2024-05-04',
            location='location 1',
            organizer=self.organizer_user,
        )
        self.event_2 = Event.objects.create(
            name='event 2',
            description='description 2 event 1',
            date='2024-05-04',
            location='location 2',
            organizer=self.organizer_user,
        )
        self.event_3 = Event.objects.create(
            name='event 2',
            description='description 3',
            date='2024-05-04',
            location='location 3',
            organizer=self.organizer_user,
        )

    def test_get(self):
        url = reverse('event-list')
        response = self.client.get(url)
        serializer_data = EventSerializer([self.event_1, self.event_2, self.event_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_filter(self):
        url = reverse('event-list')
        response = self.client.get(url, data={'name': 'event 2'})
        serializer_data = EventSerializer([self.event_2, self.event_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_search(self):
        url = reverse('event-list')
        response = self.client.get(url, data={'search': 'event 1'})
        serializer_data = EventSerializer([self.event_1, self.event_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_ordering(self):
        url = reverse('event-list')
        response = self.client.get(url, data={'ordering': '-description'})
        setializer_data = EventSerializer([self.event_3, self.event_2, self.event_1],many=True).data
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(setializer_data, response.data)

    def test_create(self):
        self.assertEqual(3, Event.objects.all().count())
        url = reverse('event-list')
        data = {
            "name": "Event 1",
            "description": "Description Event 1",
            "date": "2024-05-04",
            "location": "Location 1",
            "organizer": 1
        }
        json_data = json.dumps(data)
        self.client.force_login(self.organizer_user)
        response = self.client.post(url,
                                    data=json_data,
                                    content_type='application/json'
                                    )
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(4, Event.objects.all().count())

    def test_update(self):
        url = reverse('event-detail', args=(self.event_1.id, ))
        data = {
            "name": self.event_1.name,
            "description": "Description",
            "date": self.event_1.date,
            "location": self.event_1.location,
            "organizer": self.organizer_user.id
        }
        json_data = json.dumps(data)
        self.client.force_login(self.organizer_user)
        response = self.client.put(url,
                                   data=json_data,
                                   content_type='application/json'
                                   )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        # self.event_1 = Event.objects.get(id=self.event_1.id)
        self.event_1.refresh_from_db()
        self.assertEqual("Description", self.event_1.description)

    def test_delete(self):
        self.assertEquals(3, Event.objects.all().count())
        url = reverse('event-detail', args=(self.event_1.id, ))

        self.client.force_login(self.organizer_user)
        response = self.client.delete(url)

        self.assertEquals(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEquals(2, Event.objects.all().count())