from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.http import JsonResponse
from django_filters import rest_framework
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .permissions import AdminOnly
from .serializers import CustomUserSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'
    permission_classes = [IsAuthenticated, AdminOnly]
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_fields = ['username', ]

    @action(detail=False, methods=['get', 'patch'], permission_classes=[IsAuthenticated])
    def me(self, request):
        user = self.request.user
        if request.method == 'GET':
            serializer = CustomUserSerializer(user)
            return Response(serializer.data)
        else:
            serializer = CustomUserSerializer(
                user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def get_confirmation_mail(request):
    if request.method == 'POST':
        email = request.data.get('email')
        user = User.objects.get(email=email)
        token = default_token_generator.make_token(user)
        send_mail(
            'Подтверждение регистрации Yamdb',
            f'token: {token}',
            'Yamdb.ru <admin@yamdb.ru>',
            [email],
            fail_silently=False
        )
        return Response(request.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def reset_token(request):
    token = request.data.get('confirmation_code')
    email = request.data.get('email')
    user = User.objects.get(email=email)
    if default_token_generator.check_token(user, token):
        refresh = RefreshToken.for_user(user)
        return JsonResponse({'refresh': str(refresh),
                             'access': str(refresh.access_token)})
    else:
        return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
