import datetime, random
from rest_framework import serializers
from rest_framework.exceptions import APIException
#from utils.sendData import updateConfigCmd, activeCmd
from EMSDevice import models


'''
@brief:     设备接口初始化
@created_at:2020.7.20
@created_by:0918170220
'''


class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'


class CreateDeviceSerializer(serializers.ModelSerializer):
    device_passwd = serializers.CharField(write_only=True)
    device_id = serializers.CharField()

    class Meta:
        model = models.EMSDevice
        fields = ['device_id', 'device_name', 'device_mac', 'device_passwd', 'device_location', 'is_active']
        read_only_fields = ['device_passwd']

    def validate(self, attrs):
        '''
        '''
        device_id = attrs.pop('device_id')
        device_passwd = attrs.pop('device_passwd')
        device = models.EMSDevice.objects.get(device_id=device_id)
        if device is None:
            raise serializers.ValidationError('设备ID错误')
        if device.device_passwd != device_passwd:
            raise serializers.ValidationError('设备密钥匹配错误')
        attrs['device'] = device
        return attrs

    def create(self, validate_data):
        '''
        '''
        device = validate_data.pop('device')
        device.device_name = validate_data.get('device_name', "")
        device.device_mac = validate_data.get('device_mac')
        device.device_location = validate_data.get('device_location')
        device.is_active = validate_data.get('is_active')
        device.save()
        return device


class DeviceConfSerializer(serializers.ModelSerializer):
    '''
    '''
    class Meta:
        model = models.EMSDevice
        fields = ['device_id', 'device_name', 'device_mac', 'device_location', 'freq', 'is_active',
                  'pm25_t', 'pm10_t', 'so2_t', 'no2_t', 'co_t', 'o3_t', 'do_t', 'cod_t', 'bod_t',
                  'update_status', 'update_time', 'device_update_time']
        read_only_fields = ['device_id', 'update_status', 'update_time', 'device_update_time']
        depth = 5

    def update(self, instance, validate_data):
        object = super().update(instance, validate_data)
        object.update_status = False
        object.update_time = datetime.datetime.now()

        object.save()
        return object


class DeviceHistoryDataSerialzer(serializers.Serializer):

    datafield = serializers.CharField(max_length=10)
    start_time = serializers.DateTimeField(input_formats=["%Y-%m-%d %H:%M:%S"],
                                           required=False)
    end_time = serializers.DateTimeField(input_formats=["%Y-%m-%d %H:%M:%S"],
                                         required=False)


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EMSDevice
        fields = ['device_id', 'device_name', 'device_mac', 'device_location', 'freq', 'is_active',
                  'pm25_t', 'pm10_t', 'so2_t', 'no2_t', 'co_t', 'o3_t', 'do_t', 'cod_t', 'bod_t',
                  'update_status', 'update_time', 'device_update_time']