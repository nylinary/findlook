from rest_framework import serializers
from .models import UserSuggested


class UserSuggestedModel:
    def __init__(self, name, email, message) -> None:
        self.name  = name
        self.email = email
        self.message = message

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    message = serializers.CharField(max_length=500, default='')



def encode():
    model = UserSuggestedModel()