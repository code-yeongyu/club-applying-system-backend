from rest_framework import status
from custom_user.serializers import ProfileSerializer
from custom_user.forms import RegisterForm
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from custom_user.models import Profile
from rest_framework.views import APIView


class ProfileAPIView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=user)
            return Response(ProfileSerializer(profile).data,
                            status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request):
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=user)
            serializer = ProfileSerializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors,
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
            
@api_view(['POST'])
def register(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        profile = Profile.objects.create(user=user)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        Profile.objects.get(user=user).delete()
        return Response(serializer.errors,
                        status=status.HTTP_406_NOT_ACCEPTABLE)
    return Response(form.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
            
