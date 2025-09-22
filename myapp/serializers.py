from rest_framework import serializers
from .models import CustomUser, Note

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['username','email','phone_number','role','password']

    def create(shelf, validate_data):
        user = CustomUser(
            username = validate_data['username'],
            email = validate_data['email'],
            phone_number = validate_data.get('phone_number'),
            role = validate_data.get('role','user'),
        )
        user.set_password(validate_data['password'])
        user.save()
        return user
    

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'