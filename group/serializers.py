from rest_framework import serializers
from EMSUser.models import User
from django.contrib.auth.models import Group, Permission


class GroupAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id','name','permissions','user_set']
        extra_kwargs = {
            'permissions':{'required':False},
            'user_set':{'required':False}
        }


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id','name']
        ref_name = 'permissions'


class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True,read_only=True)
    #user_set = serializers.SlugRelatedField(many=True,slug_field='username')
    class Meta:
        model = Group
        fields = ['id','name','permissions','user_set']


    # def create(self, validated_data):
    #     permissions = validated_data.pop('permissions')
    #     group = super().create(validated_data)
    #
    #     return group

