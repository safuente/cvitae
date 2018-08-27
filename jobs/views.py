from rest_framework import viewsets
from jobs.models import Job
from jobs.serializers import JobSerializer

class JobViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing job instances.
    """
    serializer_class = JobSerializer
    queryset = Job.objects.all()
