from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class MainApiView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        return Response({'key': 'ShattredMine'})