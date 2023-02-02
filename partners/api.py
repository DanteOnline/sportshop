from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .serializers import PartnerSerializer
from .models import Partner
from rest_framework import mixins, viewsets


# class PartnerListAPIView(ListCreateAPIView):
#     permission_classes = [permissions.AllowAny]
#     pagination_class = None
#     serializer_class = PartnerSerializer
#     queryset = Partner.objects.all()

class PartnerViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = None
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()