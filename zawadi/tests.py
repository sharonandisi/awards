from django.test import TestCase

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user', password='abc123')
        self.image = Project(id=1, image = 'path/to/image',title='test',description='test caption',url='path/to/project',user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.project,Project))
