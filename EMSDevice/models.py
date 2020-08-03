from django.db import models

# Create your models here.


class EMSDevice(models.Model):
    '''
    @brief:     设备表
    @created_at:2020.7.20
    @created_by:0918170220
    '''
    device_id = models.CharField(primary_key=True, default=0, verbose_name='设备序列号', max_length=30)
    device_name = models.CharField(default='', verbose_name='设备名称', max_length=30,null=True)
    device_passwd = models.CharField(default='', verbose_name='设备密码', max_length=30)
    device_mac = models.CharField(default='', verbose_name='设备mac地址', max_length=30,null=True)
    device_location = models.CharField(default='0,0', verbose_name='设备地址', max_length=30,null=True)
    is_active = models.BooleanField(default=False, verbose_name='是否激活',null=True)

    pm25_t = models.FloatField(default=0, verbose_name='PM25阈值', max_length=30,null=True)
    pm10_t = models.FloatField(default=0, verbose_name='PM10阈值', max_length=30,null=True)
    so2_t = models.FloatField(default=0, verbose_name='SO2阈值', max_length=30,null=True)
    no2_t = models.FloatField(default=0, verbose_name='NO2阈值', max_length=30,null=True)
    co_t = models.FloatField(default=0, verbose_name='CO阈值', max_length=30,null=True)
    o3_t = models.FloatField(default=0, verbose_name='O3阈值', max_length=30,null=True)
    do_t = models.FloatField(default=0, verbose_name='DO阈值', max_length=30,null=True)
    cod_t = models.FloatField(default=0, verbose_name='COD阈值', max_length=30,null=True)
    bod_t = models.FloatField(default=0, verbose_name='BOD阈值', max_length=30,null=True)
    freq = models.FloatField(default=0, verbose_name='信号频率',null=True)
    update_status = models.BooleanField(default=0, verbose_name="设备同步状态",null=True)
    update_time = models.CharField(default='', verbose_name='更新时间', max_length=30,null=True)
    device_update_time = models.DateTimeField(auto_now=True, verbose_name="设备同步时间", null=True)

    last_login_time = models.DateTimeField(auto_now_add=True,verbose_name="设备最后上线时间",null=True)
    last_logout_time = models.DateTimeField(auto_now_add=True,verbose_name="设备最后下线时间",null=True)


class EMSDeviceConf(models.Model):
    '''
    @brief:     设备配置表
    @created_at:2020.7.21
    @created_by:0918170220
    '''
    Device = models.OneToOneField(EMSDevice, on_delete=models.PROTECT)

    pm25_t = models.FloatField(default=0, verbose_name='PM25阈值', max_length=30)
    pm10_t = models.FloatField(default=0, verbose_name='PM10阈值', max_length=30)
    so2_t = models.FloatField(default=0, verbose_name='SO2阈值', max_length=30)
    no2_t = models.FloatField(default=0, verbose_name='NO2阈值', max_length=30)
    co_t = models.FloatField(default=0, verbose_name='CO阈值', max_length=30)
    o3_t = models.FloatField(default=0, verbose_name='O3阈值', max_length=30)
    do_t = models.FloatField(default=0, verbose_name='DO阈值', max_length=30)
    cod_t = models.FloatField(default=0, verbose_name='COD阈值', max_length=30)
    bod_t = models.FloatField(default=0, verbose_name='BOD阈值', max_length=30)
    freq = models.FloatField(default=0, verbose_name='信号频率')
    update_status = models.BooleanField(default=0, verbose_name="设备同步状态")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间", null=True)
    device_update_time = models.DateTimeField(auto_now=True, verbose_name="设备同步时间", null=True)


class DeviceData(models.Model):
    device = models.OneToOneField(EMSDevice, on_delete=models.PROTECT)

    pm25 = models.FloatField(default=0, verbose_name='PM2.5浓度')
    pm10 = models.FloatField(default=0, verbose_name='PM10浓度')
    so2 = models.FloatField(default=0, verbose_name='SO2浓度')
    no2 = models.FloatField(default=0, verbose_name='NO2浓度')
    co = models.FloatField(default=0, verbose_name='CO浓度')
    o3 = models.FloatField(default=0, verbose_name='O3浓度')

    air_temp = models.FloatField(default=0, verbose_name='空气温度')
    humidity = models.FloatField(default=0, verbose_name='空气湿度')
    wind_dir = models.CharField(default='', verbose_name='风向', max_length=4)
    wind_speed = models.FloatField(default=0, verbose_name='风速')
    pressure = models.FloatField(default=0, verbose_name='大气压')

    water_temp = models.FloatField(default=0, verbose_name='水体温度')
    ph = models.FloatField(default=0, verbose_name='水体PH')
    do_d = models.FloatField(default=0, verbose_name='水体DO')
    cod = models.FloatField(default=0, verbose_name='水体COD')
    bod = models.FloatField(default=0, verbose_name='水体BOD')

    time = models.DateTimeField(verbose_name='记录时间', auto_now_add=True, null=True)


class DeviceHistoryData(models.Model):
    device = models.ForeignKey(EMSDevice, on_delete=models.PROTECT)

    pm25 = models.FloatField(default=0, verbose_name='PM2.5浓度')
    pm10 = models.FloatField(default=0, verbose_name='PM10浓度')
    so2 = models.FloatField(default=0, verbose_name='SO2浓度')
    no2 = models.FloatField(default=0, verbose_name='NO2浓度')
    co = models.FloatField(default=0, verbose_name='CO浓度')
    o3 = models.FloatField(default=0, verbose_name='O3浓度')

    air_temp = models.FloatField(default=0, verbose_name='空气温度')
    humidity = models.FloatField(default=0, verbose_name='空气湿度')
    wind_dir = models.CharField(default='', verbose_name='风向', max_length=4)
    wind_speed = models.FloatField(default=0, verbose_name='风速')
    pressure = models.FloatField(default=0, verbose_name='大气压')

    water_temp = models.FloatField(default=0, verbose_name='水体温度')
    ph = models.FloatField(default=0, verbose_name='水体PH')
    do_d = models.FloatField(default=0, verbose_name='水体DO')
    cod = models.FloatField(default=0, verbose_name='水体COD')
    bod = models.FloatField(default=0, verbose_name='水体BOD')

    time = models.DateTimeField(verbose_name='记录时间', auto_now_add=True, null=True)
