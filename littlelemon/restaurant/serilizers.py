from rest_framework import serializers
from .models import Menu, Booking
from django.contrib.auth.models import User

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        
 
class GroupNameField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name
 
        
class UserSerializer(serializers.ModelSerializer):
    groups = GroupNameField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']