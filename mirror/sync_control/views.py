from django.http import Http404

from rest_framework import views
from rest_framework import viewsets
from rest_framework import response
from rest_framework import status

from sync_control.models import UserProfile
from sync_control.models import UserProfileSerializer
from sync_control.models import GenericContent
from sync_control.models import GenericContentSerializer


class UserProfileView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class ContentList(views.APIView):

    def get_content(self, pk):
        try:
            return GenericContent.objects.get(pk=pk)
        except GenericContent.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        contents = GenericContent.objects.all()
        serializer = GenericContentSerializer(contents, many=True)
        return response.Response(serializer.data)

    def put(self, request, pk, format=None):
        content = get_content(pk)
        serializer = GenericContentSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros,
                    status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        content = get_content(pk)
        content.delete()
        return Response(serializer.erros,
                    status=status.HTTP_204_NO_CONTENT)

