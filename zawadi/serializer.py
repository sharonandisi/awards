from rest_framework import serializers
from .models import Profile, Image

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'profile_pic', 'bio','email')

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('title', 'description', 'image', 'url', 'user', 'pub_date')
