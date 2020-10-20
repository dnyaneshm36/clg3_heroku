from django.contrib.auth.models import User
from rest_framework import serializers
from friend.models import Myfrienddetail
class UserSerializer(serializers.ModelSerializer):
  #  snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Myfrienddetail.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username','email','first_name','last_name']