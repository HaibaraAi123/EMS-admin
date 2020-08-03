from .models import EMSLogConfig

# log_id = models.AutoField(primary_key=True, verbose_name='ID')
# log_addtime = models.DateTimeField(default=datetime.datetime.now, verbose_name="添加时间")
# log_content = models.CharField(max_length=255, verbose_name='内容')
# log_user = models.CharField(max_length=255, verbose_name='操作人')


def addlog(request,log_type,log_content):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        # username = "Anonymous"
        username = "匿名用户"

    EMSLogConfig.objects.create(log_user=username,log_content=log_content)

