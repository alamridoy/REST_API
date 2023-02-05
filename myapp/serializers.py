from myapp.models import *
from rest_framework import serializers


# class ContactSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=20)
#     address = serializers.CharField(max_length=100)

#     def create(self, validated_data):
        
#         return Contact.objects.create(
#           validated_data)
      
      
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.email = validated_data.get('email', instance.email)
#         instance.address = validated_data.get('address', instance.address)
        
#         instance.save()
#         return instance


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Contact
        fields = ['name','title','email','url','onwer']