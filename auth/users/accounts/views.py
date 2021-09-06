from .serializers import *
from .models import User as User_infor
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import response, schemas


@api_view(["POST"])
@permission_classes([AllowAny])  # 인증 필요없다
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
@swagger_auto_schema(request_body=UserCreateSerializer)
def signup(request):
    serializer = UserCreateSerializer(data=request.data)
    if request.method == "POST":
        if serializer.is_valid(raise_exception=True):
            serializer.save()  # DB 저장
            return Response(serializer.data, status=201)


@api_view(["POST"])
@permission_classes([AllowAny])
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
@swagger_auto_schema(request_body=UserLoginSerializer)
def login(request):
    if request.method == "POST":
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response(
                {"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT
            )
        if serializer.validated_data["email"] == "None":  # email required
            return Response({"message": "fail"}, status=status.HTTP_200_OK)

        response = {
            "success": True,
            "token": serializer.data["token"],  # 시리얼라이저에서 받은 토큰 전달
        }
        return Response(response, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([AllowAny])
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def update(request):
    user = User_infor.objects.get(email=request.data["email"])
    if user is None:
        return Response("회원정보 없음", status=404)
    serializer = UserCreateSerializer(user, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()  # DB 저장
        return Response("회원정보수정 성공", status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([AllowAny])
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def delete(request):
    user = User_infor.objects.get(
        email=request.data["email"], nickname=request.data["nickname"]
    )
    if user is None:
        return Response("탈퇴 불가", status=404)
    else:
        user.objects.delete()
        return Response("탈퇴", status=status.HTTP_200_OK)
