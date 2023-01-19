from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
# from rest_framework import authentication, permissions
from sport_equipment.models import Category
from .serializers import CategorySerializer


class ListCategoryAPIView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all categories.
        """
        usernames = [str(category) for category in Category.objects.all()]
        return Response(usernames)


    def post(self, request, format=None):
        """
        Return a list of all categories.
        """
        usernames = [str(category) for category in Category.objects.all()]
        return Response(usernames)


class ListCategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CreateCategoryView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListCreateCategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FilterListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        # через параметры в адресе
        name_part = self.kwargs['name_part']
        queryset = super().get_queryset().filter(name__contains=name_part)
        # через параметры запроса
        max_rating = self.request.query_params.get('rating')
        if max_rating:
            queryset = queryset.filter(rating__lte=max_rating)
        return queryset