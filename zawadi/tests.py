from django.test import TestCase

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user', password='abc123')
        self.image = Image(id=1, image = 'path/to/image',title='test',description='test caption',url='path/to/image',user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.project,Project))

class ReviewTestClass(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='user', password='abc123')
        self.profile = Profile(profile_pic='images/pic', bio='eat pray love', contacts='+254720570175', user = self.user)
        self.profile.save()
        self.image = Image(id=1, image = 'path/to/image',title='test',description='test caption',url='path/to/image',user=self.user)
        self.project.save()
        self.review = Review(id=1,image=self.image,design=1,usability=1,content=1,average=1,user=self.user)
