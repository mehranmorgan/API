from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from account.permissions import UserPermission
from account.serializer import UserSerializer
from rest_framework.pagination import PageNumberPagination


class UserView(APIView):
    permission_classes = [UserPermission]
    serializer_class = UserSerializer

    def get(self, request):
        paginator = PageNumberPagination()
        instance = User.objects.all()
        result=paginator.paginate_queryset(queryset=instance,request=request)
        ser = UserSerializer(instance=result, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
