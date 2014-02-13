from django.test import TestCase
from tepresto.api.models import User, Community

# Create your tests here.
class UserTest(TestCase):

    def setUp(self):
        Community.objects.create(name="Jungle")
        Community.objects.create(name="Felines")
        User.objects.create(name="Lion")

    def test_userWithManyCommunities(self):
        lion = User.objects.get(name="Lion")
        jungle = Community.objects.get(name="Jungle")
        felines = Community.objects.get(name="Felines")
        lion.community.add(jungle)
        lion.community.add(felines)
        self.assertEqual(lion.community.count(), 2)
        


