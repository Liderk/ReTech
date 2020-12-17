from django.contrib.auth import authenticate, get_user_model, login, logout
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TaskSerializer
from todo.models import Task


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        user = self.request.user
        company = user.account.company_access
        queryset = Task.objects.filter(company_id__name=company)
        return queryset


@api_view(['POST'])
def signin(request):
    user_email = request.data.get('email')
    company_access = request.data.get('company')
    password = request.data.get('password')

    User = get_user_model()

    if User.objects.filter(email=user_email).exists():
        user = User.objects.get(email=user_email)

        username = user.username

        user_auth = authenticate(username=username, password=password)

        if user_auth is not None:

            if user.account.companies.filter(
                    name=company_access).exists():
                user.account.company_access = company_access
                user.account.save()

                login(request, user)
                return Response({'message': 'login successful'}, status=200)

            else:
                return Response(
                    {'message': "You don't have access to this company"},
                    status=403)

        return Response({'message': 'The password is incorrect'}, status=403)
    return Response({'message': 'The user does not exist'}, status=400)


@api_view(['GET'])
def signout(request):
    logout(request)
    return Response({'message': 'The user is logged out'}, status=200)
