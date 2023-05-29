
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from rest_framework import status
from rest_framework.response import Response

from account.serializers.spaceserializers import SpaceListSerializer, InputSpaceAccessSerializer
from account.serializers.commonserializers import SpaceSerializer
from account.services import spaceservices

class ChangeCurrentSpaceViewSet(APIView):
    def post(self, request, space_id):
        result = spaceservices.change_current_space(request.user, space_id)
        if result.success:
            return Response({'message': result.message})
        else:
            return Response({'message': result.message}, status=status.HTTP_400_BAD_REQUEST)
        

class SpaceAccessAPI(APIView):
    serializer_class = InputSpaceAccessSerializer
    def post(self, request, space_id):
        serializer = InputSpaceAccessSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result =  spaceservices.add_user_to_space(space_id, request.user, **serializer.validated_data)
        if result.success:
            return Response({'message': result.message})
        else:
            return Response({'message': result.message}, status=status.HTTP_400_BAD_REQUEST)
        

class SpaceViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.action in ('create', 'update'):
            return SpaceSerializer   
        else:
            return SpaceListSerializer
    def get_queryset(self):
        current_user = self.request.user
        if current_user.spaces is not None:
            return current_user.spaces.all()

class SpaceLeaveUserAPI(APIView):
    def post(self, request, space_id):
        result = spaceservices.leave_user_space(space_id, request.user)
        if result.success:
            return Response({'message': result.message})
        else:
            return Response({'message': result.message}, status=status.HTTP_400_BAD_REQUEST)
