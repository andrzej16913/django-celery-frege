from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions

from fregepoc.repositories.models import Repository, RepositoryFile
from fregepoc.repositories.serializers import RepositorySerializer, RepositoryFileSerializer


class RepositoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer
    permission_classes = [DjangoModelPermissions]
    filterset_fields = ['analyzed']


class RepositoryFileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RepositoryFile.objects.all()
    serializer_class = RepositoryFileSerializer
    permission_classes = [DjangoModelPermissions]
    filterset_fields = ['repository', 'analyzed', 'language']