from rest_framework import generics

from .serializers import PostProductSerializer
from .models import PostProduct


class ProductListView(generics.ListAPIView):
    """
    Retrieves a list of all Products.
    This view is accessible to all users for browsing Products.
    """
    permission_classes = ()
    authentication_classes = ()

    queryset = PostProduct.objects.all()
    serializer_class = PostProductSerializer

