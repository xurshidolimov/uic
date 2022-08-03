from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import StudentSerializer, MetsenatSerializer, SponsorSerializer
from .models import Metsenat, Student


class AllStudentView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        humans = Student.objects.all().order_by('-created_at')
        search_query = request.GET.get('q', '')
        if search_query:
            humans = humans.filter(username__icontains=search_query)

        paginator = PageNumberPagination()
        page_obj = paginator.paginate_queryset(humans, request)

        serializer = StudentSerializer(page_obj, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FilterStudentView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        humans = Student.objects.all().order_by('-created_at')
        search_student_type = request.GET.get('q', '')
        search_student_otm = request.GET.get('t', '')

        if search_student_type:
            if not search_student_type == 'barchasi':
                humans = humans.filter(student_type=search_student_type)

        if search_student_otm:
            if not search_student_otm == 'barchasi':
                humans = humans.filter(otm=search_student_otm)

        serializer = StudentSerializer(humans, many=True)
        return Response(data=serializer.data)


class DetailStudentView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request, id):
        student = Student.objects.get(id=id)
        student_detail = StudentSerializer(student)

        metsenat = Metsenat.objects.filter(student=student)
        serializer = MetsenatSerializer(metsenat, many=True)

        return Response({
            "student_detail": student_detail.data,
            "data": serializer.data
        })

    def patch(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(instance=student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Talaba muvaffaqqiyatli tahrirlandi"}, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MetsenatView(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, id):
        serializer = MetsenatSerializer(data=request.data)
        if serializer.is_valid():
            # serializer['student_id'] = id
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        pass

