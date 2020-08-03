from rest_framework.serializers import ModelSerializer
from .models import User
from rest_framework import serializers
class UserSerializer(ModelSerializer):
    # date_joined = serializers.DateTimeField(format("%Y-%m-%d %H:%M:%S"),input_formats=["%Y-%m-%d %H:%M:%S",],required=False)
    # last_login = serializers.DateTimeField(format("%Y-%m-%d %H:%M:%S"),input_formats=["%Y-%m-%d %H:%M:%S",],required=False)
    class Meta:
        model = User
        fields = ['id','password','last_login','username','first_name','last_name','email',\
                  'is_active','date_joined','phone','gender','info',"user_permissions",]

        extra_kwargs = {
            'last_login':{'read_only':True,"required":False},
            'date_joined':{'read_only':True,"required":False},
            'password':{'write_only':True}
        }

    def create(self, validated_data):
        password=validated_data.pop('password')
        User = super().create(validated_data)
        User.set_password(password)
        User.save()
        return User

   #转换
    # def get_gender(self, obj):
    #     if obj.gender == 1:
    #         return "男"
    #     return "女"
    # gender = serializers.SerializerMethodField()

class AddUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        password=validated_data.pop('password')
        User = super().create(validated_data)
        User.set_password(password)
        User.save()
        return User

class UserUpdateSerizalizer(ModelSerializer):
    class Meta:
        model = User
        fields = ['gender','phone','email','info']