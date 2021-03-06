from django.shortcuts import render
from rest_framework import generics
from group.serializers import GroupSerializer,GroupAddSerializer
from django.contrib.auth.models import Group
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from permission.permissions import ModelPermission
# Create your views here.


class GroupListView(generics.ListCreateAPIView):
    '''
    角色列表
    '''
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class =GroupSerializer
    queryset = Group.objects.all().order_by('id')

    def get_model_perms_conf(self):
        if self.request.method == "POST":
            print("BBBBBBB")
            return ('user.management_',)
        else:
            print("AAAAAAAAA")
            return ()

    def get_permissions(self):
        if self.request.method == 'POST':
            return (permissions.IsAuthenticated(),ModelPermission())
        else:
            return (permissions.IsAuthenticated(),)


    def get_serializer_class(self):
        if self.request.method == 'GTE':
            return GroupSerializer
        else:
            return GroupAddSerializer

    # def check_permissions(self, request):
    #     pass

    def list(self, request, *args, **kwargs):
        #request.user.get_all_permissions()
        if not request.user.has_perm('user.add_user'):
            return Response({"msg":"权限验证失败","code":403},status=status.HTTP_403_FORBIDDEN)

        return super().list(request,*args,**kwargs)

