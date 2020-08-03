from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView,ListAPIView,DestroyAPIView
from .serializers import UserSerializer,AddUserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

# Create your views here.


class MyPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 2


'''
class AddUserView(APIView):
    def post(self, request):
        serizalizer = AddUserSerializer(data=request.data)
        if serizalizer.is_valid():
            serizalizer.save()
            return Response(data={"msg": "添加成功"}, status=status.HTTP_201_CREATED)
        return Response(data=serizalizer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        users = User.objects.all()
        serizalizer = UserSerializer(users, many=True)
        return Response(serizalizer.data, status=status.HTTP_200_OK)


class Add2UserView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class DeleteUserView(DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

'''


class UserModelViewSet(ModelViewSet):

    pagination_class = MyPagination
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('id')
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('gender', 'is_active')
    search_fields = ('username', 'info')

    def create(self, request, *args, **kwargs):
        """
        新增用户

        #### 参数说明
        | 字段名称 | 描述 | 必须 | 类型 |
        | -- | -- | -- | -- |
        | username | 用户名 | True | str |
        | password | 密码 | True | str |
        | last_name | 昵称 | True | str|
        | email | 邮箱 | True | str |
        | phone | 电话 | True | str |
        | num | 工号 | True | str |
        | sex | 性别(1男 2女) | True | int |
        | info | 备注信息 | False | int |
        | is_active | 账户状态(1 冻结 2 激活）| False |int|



        #### 响应消息：
        | Http响应码 | 原因 | 响应模型 |
        | -- | -- | -- |
        | 201 | 添加成功 | 返回数据 |
        | 400 | 参数格式错误 | 参数格式错误 |
        | 500 | 请求失败 | 服务器内部错误 |
        """
        return super().create(request,*args,**kwargs)

    def destroy(self, request, *args, **kwargs):
        """
           冻结用户

           #### 参数说明
           | 字段名称 | 描述 | 必须 | 类型 |
           | -- | -- | -- | -- |
           | id| 用户id | True | int |

           #### 响应字段说明
           | 字段名称 | 描述 | 类型 |
           | -- | -- | -- |
           | msg| 提示信息 | string |
           | code | 状态码 | int |


           #### 注意说明：
           无

           #### 响应消息：
           | Http响应码 | 原因 | 响应模型 |
           | -- | -- | -- |
           | 200 | 冻结成功 | -- |
           | 400 | 参数格式错误 | 参数格式错误 |
           | 500 | 请求失败 | 服务器内部错误 |
           """

        user = self.get_object()
        user.is_active = False
        user.save()
        return Response(data={'msg': "成功冻结", "code":200}, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        """
            修改用户信息

            #### 参数说明
            | 字段名称 | 描述 | 必须 | 类型 |
            | -- | -- | -- | -- |
            | id | 模型id | True | int |
            | last_name | 昵称 | True | str|
            | email | 邮箱 | True | str |
            | tel | 电话 | True | str |
            | num | 工号 | True | str |
            | gender | 性别(1男 2女) | True | int |
            | info | 备注信息 | True | int |
            | is_active | 账户状态(0 冻结 1 激活）| True |int|


            #### 响应消息：
            | Http响应码 | 原因 | 响应模型 |
            | -- | -- | -- |
            | 200 | 修改成功 |修改成功|
            | 404 | 未找到 | 未找到|
            | 500 | 请求失败 | 服务器内部错误 |
            """

        return super().update(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
            用户详情

            #### 参数说明
            | 字段名称 | 描述 | 必须 | 类型 |
            | -- | -- | -- | -- |
            | id | 模型id | True | int |


            #### 响应字段说明
            | 字段名称 | 描述 | 类型 |
            | -- | -- | -- |
            | id| 用户ID | -- | int |
            | username | 用户名 | -- | str |
            | last_name | 昵称 | string |
            | last_login| 最后登录时间 | Y-%m-%d %H:%M:%S |
            | date_joined | 创建时间 | Y-%m-%d %H:%M:%S |
            | is_superuser | 是否是超级用户 | int |
            | is_active| 是否冻结 | int |
            | email | 邮箱 | str|
            | tel| 电话 | str |
            | num | 工号 |  str |
            | gender | 性别 |  str |
            | info| 备注 |  int |

            #### 注意说明：
            无

            #### 响应消息：
            | Http响应码 | 原因 | 响应模型 |
            | -- | -- | -- |
            | 200 | 请求成功 | 返回数据 |
            | 400 | 参数格式错误 | 参数格式错误 |
            | 500 | 请求失败 | 服务器内部错误 |
            """

        return super().retrieve(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
            修改用户信息(部分更新)

            #### 参数说明
            | 字段名称 | 描述 | 必须 | 类型 |
            | -- | -- | -- | -- |
            | id | 模型id | True | int |
            | last_name | 昵称 | False | str|
            | email | 邮箱 | False | str |
            | tel | 电话 | False | str |
            | num | 工号 | False | str |
            | gender | 性别(1男 2女) | False | int |
            | info | 备注信息 | False | int |
            | is_active | 账户状态(0 冻结 1 激活）| False |int|


            #### 响应消息：
            | Http响应码 | 原因 | 响应模型 |
            | -- | -- | -- |
            | 200 | 修改成功 |修改成功|
            | 404 | 未找到 | 未找到|
            | 500 | 请求失败 | 服务器内部错误 |
            """
        return super().partial_update(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """
            用户列表

            #### 参数说明
            | 字段名称 | 描述 | 必须 | 类型 |
            | -- | -- | -- | -- |
            | page | 分页页码 | False | int |
            | page_size | 分页大小 | False | int |
            | gender |过滤条件：性别 (1男,2女) |False|int|
            | is_active |过滤条件：是否激活 (true激活,false冻结) |False|int|
            | search|模糊匹配，匹配字段('username','email','num','info')| False|str|



            #### 响应字段说明
            | 字段名称 | 描述 | 类型 |
            | -- | -- | -- |
            | id| 用户ID | -- | int |
            | username | 用户名 | -- | str |
            | last_name | 昵称 | string |
            | last_login| 最后登录时间 | Y-%m-%d %H:%M:%S |
            | date_joined | 创建时间 | Y-%m-%d %H:%M:%S |
            | is_superuser | 是否是超级用户 | int |
            | is_active| 是否冻结 | int |
            | email | 邮箱 | str|
            | tel| 电话 | str |
            | num | 工号 |  str |
            | gender | 性别 |  str |
            | info| 备注 |  int |

            #### 注意说明：
            无

            #### 响应消息：
            | Http响应码 | 原因 | 响应模型 |
            | -- | -- | -- |
            | 200 | 请求成功 | 返回数据 |
            | 400 | 参数格式错误 | 参数格式错误 |
            | 500 | 请求失败 | 服务器内部错误 |
            """
        # if not request.user.has_perm('user.viwe_user'):
        #     return Response({"msg":"权限验证失败","code":403},status=status.HTTP_403_FORBIDDEN)
        return super().list(request, *args, **kwargs)


class LoginView(APIView):
    '''
        用户登录

        #### 参数说明
        | 字段名称 | 描述 | 类型 |
        | -- | -- | -- |
        | username | 用户名 | str |
        | passwd | 密码 | str |
        #### 响应消息：
        | Http响应码 | 原因 | 响应模型 |
        | -- | -- | -- |
        | code | 状态码 | int |
        | msg | 返回信息 | str |
        #### 实例说明
        /api/login/{"username":"aaaaa", "password":"bbbbb"}
    '''
    '''
    def get(self, request):
        params = request.query_params
        username = params['username']
        user = User.objects.filter(username=username).first()
        data = user.password
        return Response(data={'password': data}, status=status.HTTP_200_OK)
    '''
    def post(self, request, *args, **kwargs):
        try:
            params = request.data
            username = params['username']
            password = params['password']
        except Exception:
            return Response(data={'msg': '参数格式错误', 'code': 400}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(username=username).first()
        if user is None:
            return Response(data={'msg': '登录失败,用户名错误', 'code': 410}, status=status.HTTP_410_GONE)
        elif user.check_password(password):
            return Response(data={'msg': '登录成功', 'code': 200}, status=status.HTTP_200_OK)
        else:
            return Response(data={'msg': '登录失败,密码错误', 'code': 410}, status=status.HTTP_410_GONE)
