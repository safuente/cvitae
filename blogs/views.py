from rest_framework import viewsets
from blogs.models import Blog
from blogs.serializers import BlogSerializer

class BlogViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing blog instances.
    """
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
