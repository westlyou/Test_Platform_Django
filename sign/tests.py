from django.test import TestCase
from sign.models import Event, Guest

# Create your tests here.


class ModelTest(TestCase):

    def setUp(self):
        Event.objects.create(id=1, name='oneplus 3 event', status=True, limit=2000, address='shenzhen', \
                             start_time='2016-08-31 02:18:22')
        Guest.objects.create(id=1, event_id=1, realname='Alen', phone='13722221111', email='232', sign=False)

    def test_event_model(self):
        result = Event.objects.get(name='oneplus 3 event')
        self.assertEqual(result.address, 'shenzhen')
        self.assertTrue(result.status)

    def test_guest_model(self):
        result = Guest.objects.get(phone=13722221111)
        self.assertEqual(result.realname, 'Alen')
        self.assertFalse(result.sign)
