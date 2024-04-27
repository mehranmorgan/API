from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ads.models import Ad
from ads.permissions import IsOwnerOrReadOnly
from ads.serializer import AdSerializer


# Create your views here.
class AdView(APIView):
    serializer_class = AdSerializer

    def get(self, request):
        paginator = PageNumberPagination()
        instance = Ad.objects.all()
        result = paginator.paginate_queryset(queryset=instance, request=request)
        ser = AdSerializer(instance=result, many=True, context={'request': request})
        return Response(ser.data, status=status.HTTP_200_OK)


class CreateAd(APIView):
    serializer_class = AdSerializer
    parser_classes = (MultiPartParser,)

    def post(self, request):
        ser = AdSerializer(data=request.data)
        if ser.is_valid():
            ser.validated_data['publisher'] = request.user
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        return Response(ser.errors)


class AdDetailView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = AdSerializer
    parser_classes = (MultiPartParser,)

    def get_obj(self):
        obj = get_object_or_404(Ad.objects.all(), id=self.kwargs['pk'])
        self.check_object_permissions(request=self.request, obj=obj)
        return obj

    def get(self, request, pk):
        obj = self.get_obj()
        ser = AdSerializer(instance=obj)
        return Response(ser.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        obj = self.get_obj()
        ser = AdSerializer(data=request.data, instance=obj)
        if ser.is_valid():
            ser.save()
            return Response({'message': 'ok'})
        return Response(ser.errors)

    def delete(self, request, pk):
        obj = self.get_obj()
        obj.delete()
        return Response({'message': 'delete'})


class AdSearchView(APIView):
    serializer_class = AdSerializer

    def get(self, request):
        q = request.GET.get('q')
        print(q)
        obj = Ad.objects.filter(Q(title__icontains=q) | Q(caption__icontains=q))
        pagination = PageNumberPagination()
        result = pagination.paginate_queryset(queryset=obj, request=request)
        ser = AdSerializer(instance=result, many=True)
        return Response(ser.data)
