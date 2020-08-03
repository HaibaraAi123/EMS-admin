import datetime
from django.db.models import Avg
from rest_framework import views, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from EMSDevice import models, serializers

from EMSDevice.utils import getAQI

'''
'''


# Create your views here.
class SelfPagination(PageNumberPagination):
    '''
    '''
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class DeviceModelViewSet(ModelViewSet):
    queryset = models.EMSDevice.objects.all().order_by('device_id')
    pagination_class = SelfPagination

    filterset_fields = ('device_id', 'device_name')
    search_fields = ('device_id', 'device_name')

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.CreateDeviceSerializer
        elif self.action == 'update' or self.action == '':
            return serializers.DeviceConfSerializer
        elif self.action == 'list' or self.action == 'delete':
            return serializers.DeviceSerializer
        else:
            return serializers.DeviceConfSerializer

    def list(self, request, *args, **kwargs):
        '''
            显示设备列表

            #### 参数:
            | 字段名称 | 描述 | 必须 | 类型 |
            | -- | -- | -- | -- |
            | page | 第几页 | 非必传 | int |
            | page_size | 每页条数 | 非必传 | int |
            | device_id | 设备编号  | int |
            | devicename | 设备名 | str |

            #### 响应说明：
            | 字段名称 | 描述 | 类型 |
            | -- | -- | -- |
            | count| 总条数 | int |
            | next | 下一页地址 | str |
            | previous | 上一页地址  | str |
            | results | 数据列表 | list |
            | device_id | 设备编号  | int |
            | devicename | 设备名 | str |
            | mac_add | mac地址 | str |
            | location | 设备位置 | str |
            | is_active | 是否上线 | bool |

            #### 响应消息：
            | Http响应码 | 原因 | 响应模型 |
            | -- | -- | -- |
            |200|请求成功|返回json数据
            |400| 请求失败 |
            #### 注意说明：
            无
        '''
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        '''
            获取设备详情

            #### 响应说明
            | 字段名称 | 描述 | 类型 |
            | -- | -- | -- |
            | results | 数据列表 | list |
            | device_id | 设备id | str |
            | device_passwd | 设备密码 | str |
            | device_name | 设备名称 | str |
            | mac | mac地址 | str |
            | location | 设备位置 | str |
            | freq | 发送频率 | int |
            | is_active | 是否上线 | bool |
            | pm25 | pm25阈值 | int |
            | pm10 | pm10阈值 | int |
            | so2 | so2阈值 | int |
            | no2 | no2阈值 | int |
            | co | co阈值 | int |
            | o3 | o3阈值 | int |
            | do | do阈值 | int |
            | cod | cod阈值 | int |
            | bod | bod阈值 | int |
            #### 注意说明：
            无

            #### 响应消息：
            | Http响应码 | 原因 | 响应模型 |
            | -- | -- | -- |
            |200|请求成功||
            |400|参数格式错误||
            |500|请求失败|服务器内部错误|
        '''
        return super().retrieve(request, *args, *kwargs)

    def create(self, request, *args, **kwargs):
        '''
            增加设备

            #### 参数：
            | 字段名称 | 描述 | 类型 |
            | -- | -- | -- |
            | device_id | 设备id | str |
            | device_passwd | 设备密码 | str |
            | device_name | 设备名称 | str |
            | mac | mac地址 | str |
            | location | 设备位置 | str |
            | freq | 发送频率 | int |
            | is_active | 是否上线 | bool |
            | pm25 | pm25阈值 | int |
            | pm10 | pm10阈值 | int |
            | so2 | so2阈值 | int |
            | no2 | no2阈值 | int |
            | co | co阈值 | int |
            | o3 | o3阈值 | int |
            | do | do阈值 | int |
            | cod | cod阈值 | int |
            | bod | bod阈值 | int |
            #### 响应消息：
            | Http响应码 | 原因 | 响应模型 |
            | -- | -- | -- |
            | code | 状态码 | int |
            | msg | 返回信息 | str |
            #### 注意说明：
            无
        '''
        #UserPermission = request.user.get_all_permissions()
        #if 'EMSUser.management_' not in UserPermission:
            #return Response(data={'msg': '权限不足', 'code': 403}, status=status.HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        '''
            设备信息更新（整体）

            #### 参数说明
            | 字段名称 | 描述 | 类型 |
            | -- | -- | -- |
            | device_id | 设备id | str |
            | device_passwd | 设备密码 | str |
            | device_name | 设备名称 | str |
            | mac | mac地址 | str |
            | location | 设备位置 | str |
            | freq | 发送频率 | int |
            | is_active | 是否上线 | bool |
            | pm25 | pm25阈值 | int |
            | pm10 | pm10阈值 | int |
            | so2 | so2阈值 | int |
            | no2 | no2阈值 | int |
            | co | co阈值 | int |
            | o3 | o3阈值 | int |
            | do | do阈值 | int |
            | cod | cod阈值 | int |
            | bod | bod阈值 | int |
            #### 响应消息：
            | Http响应码 | 原因 | 响应模型 |
            | -- | -- | -- |
            | code | 状态码 | int |
            | msg | 返回信息 | str |
            #### 注意说明：
            无
        '''
        #UserPermission = request.user.get_all_permissions()
        #if 'EMSUser.management_' not in UserPermission:
            #return Response(data={'msg': '权限不足', 'code': 403}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, *kwargs)

    def partial_update(self, request, *args, **kwargs):
        '''
            设备信息修改(部分)

             #### 参数说明
            | 字段名称 | 描述 | 类型 |
            | -- | -- | -- |
            | device_id | 设备id | str |
            | device_passwd | 设备密码 | str |
            | device_name | 设备名称 | str |
            | mac | mac地址 | str |
            | location | 设备位置 | str |
            | freq | 发送频率 | int |
            | is_active | 是否上线 | bool |
            | pm25 | pm25阈值 | int |
            | pm10 | pm10阈值 | int |
            | so2 | so2阈值 | int |
            | no2 | no2阈值 | int |
            | co | co阈值 | int |
            | o3 | o3阈值 | int |
            | do | do阈值 | int |
            | cod | cod阈值 | int |
            | bod | bod阈值 | int |
            #### 响应消息：
            | Http响应码 | 原因 | 响应模型 |
            | -- | -- | -- |
            | code | 状态码 | int |
            | msg | 返回信息 | str |
            #### 注意说明：
            无
        '''
        #UserPermission = request.user.get_all_permissions()
        #if 'EMSUser.management_' not in UserPermission:
            #return Response(data={'msg': '权限不足', 'code': 403}, status=status.HTTP_403_FORBIDDEN)
        return super.partial_updata(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        '''
            设备删除error

            #### 参数说明
            | 字段名称 | 描述 | 类型 |
            | -- | -- | -- |
            | device_id | 设备id | str |
            #### 响应消息：
            | Http响应码 | 原因 | 响应模型 |
            | -- | -- | -- |
            | code | 状态码 | int |
            | msg | 返回信息 | str |
            #### 注意说明：
        '''
        #UserPermission = request.user.get_all_permissions()
        #if 'EMSUser.management_' not in UserPermission:
            #return Response(data={'msg': '权限不足', 'code': 403}, status=status.HTTP_403_FORBIDDEN)
        return super().delete(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        '''
            冻结设备

            #### 参数说明
            | 字段名称 | 描述 | 类型 |
            | -- | -- | -- |
            | device_id | 设备id | str |
            #### 响应消息：
            | Http响应码 | 原因 | 响应模型 |
            | -- | -- | -- |
            | code | 状态码 | int |
            | msg | 返回信息 | str |
            #### 注意说明：
            此功能实现错误
        '''
        #UserPermission = request.user.get_all_permissions()
        #if 'EMSUser.management_' not in UserPermission:
            #return Response(data={'msg': '权限不足', 'code': 403}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)


class GetDataView(views.APIView):
    def get(self, request, *args, **kwargs):
        '''
            获取设备数据（设备描述信息，实时数据，历史数据）

            #### 参数说明
            | 字段名称 | 描述 | 类型 |
            | -- | -- | -- |
            |device_id|设备id|str|
            |type|数据类型{brief, data, history_data}|str|
            #### 响应消息：
            | Http响应码 | 原因 | 响应模型 |
            | -- | -- | -- |
            | code | 状态码 | int |
            | msg | 返回信息 | str |
            #### 注意说明：
        '''
        device_id = kwargs['device_id']
        DataType = kwargs['type']
        if DataType == 'brief':
            device = models.EMSDevice.objects.filter(device_id=device_id).first()
            if device is None:
                return Response(data={'msg': '未找到设备', "code": 400}, status=status.HTTP_400_BAD_REQUEST)
            else:
                data = {'device_name': device.device_name, 'location': device.device_location,
                        'is_active': device.is_active}
                return Response(data={"results": data}, status=status.HTTP_200_OK)
        elif DataType == 'data':
            data = models.DeviceData.objects.filter(device_id=device_id).values()
            return Response(data={"results": data}, status=status.HTTP_200_OK)
        elif DataType == 'history_data':
            data = models.DeviceHistoryData.objects.filter(device_id=device_id).values()
            return Response(data={"results": data}, status=status.HTTP_200_OK)

        else:
            return Response(data={'msg': '类型错误', "code": 400}, status=status.HTTP_400_BAD_REQUEST)


class GetAllCurrentView(views.APIView):
    def get(self, request, *args, **kwargs):
        '''
            获取所有设备的实时监控数据

            #### 参数说明
            无参数
            #### 响应消息：
            | Http响应码 | 原因 | 响应模型 |
            | -- | -- | -- |
            | code | 状态码 | int |
            | msg | 返回信息 | str |
            #### 注意说明：
        '''
        try:
            all_data = models.DeviceData.objects.all().values()
            return Response(data={'msg': "请求成功", "code": 200, 'results': all_data}, status=status.HTTP_200_OK)

        except Exception:
            return Response(data={'msg': '请求错误', 'code': 400}, status=status.HTTP_400_BAD_REQUEST)


class GetAQIView(views.APIView):
    def get(self, request, *args, **kwargs):
        '''
            获取AQI(近一小时)

            #### 参数说明
            无参数
            #### 响应消息：
            | Http响应码 | 原因 | 响应模型 |
            | -- | -- | -- |
            | code | 状态码 | int |
            | msg | 返回信息 | str |
        '''
        # 获取一小时的数据
        end_time = datetime.datetime.now()
        start_time = datetime.datetime.now() - datetime.timedelta(hours=1)
        data = models.DeviceHistoryData.objects.filter(time__gte=start_time, time__lte=end_time) \
            .values('device_id').annotate(pm25=Avg('pm25'), pm10=Avg('pm10'), so2=Avg('so2'), no2=Avg('no2'),
                                          co=Avg('co'), o3=Avg('o3')) \
            .values('device_id', 'pm25', 'pm10', 'so2', 'no2', 'co', 'o3')

        # 计算AQI
        for d in data:
            # print(d)
            d["IAQIPM25"] = int(getAQI(d["pm25"], "pm25"))
            d["IAQIPM10"] = int(getAQI(d["pm10"], "pm10"))
            d["IAQISO2"] = int(getAQI(d["so2"], "so2"))
            d["IAQINO2"] = int(getAQI(d["no2"], "no2"))
            d["IAQICO"] = int(getAQI(d["co"], "co"))
            d["IAQIO3"] = int(getAQI(d["o3"], "o3"))

            # 计算最大AQI
            AQIlist = [d["IAQIPM25"], d["IAQIPM10"], d["IAQISO2"], d["IAQINO2"], d["IAQICO"], d["IAQIO3"]]
            index = AQIlist.index(max(AQIlist))
            d["AQI"] = AQIlist[index]

            # 添加描述
            type_list = ['pm25', 'pm10', 'so2', 'no2', 'co', 'o3']
            d['desc'] = "{} 为主要污染物。".format(type_list[index])

        # 计算排名
        data = sorted(data, key=lambda d: d['AQI'], reverse=True)
        for i in range(0, len(data)):
            data[i]["rank"] = i + 1

        return Response(data={'msg': "请求成功", "code": 200, "data": data}, status=status.HTTP_200_OK)
