from django.http import JsonResponse
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser

from blog.models import Sponsor
from blog.serializers import SponsorSerializer
from students.models import Student


class AplicationSponsorView(APIView):
    def post(self, request):
        serializer = SponsorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response({"message": "Ma'lumotlar tekshirish uchun yuborildi"}, status=status.HTTP_201_CREATED, )
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DashboardView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        students = Student.objects.all().order_by('created_at')
        sponsors = Sponsor.objects.all().order_by('created_at')

        student_dictionary = {}
        tolanishi_kerak_summa = 0
        for student in students:
            for month in range(13):
                if month == student.created_at.month:
                    tolanishi_kerak_summa = tolanishi_kerak_summa + student.kontrakt
                    student_dictionary[month] = tolanishi_kerak_summa

        sponsor_dictionary = {}
        jami_tolangan_summa = 0
        for sponsor in sponsors:
            for month in range(13):
                if month == sponsor.created_at.month:
                    jami_tolangan_summa = jami_tolangan_summa + sponsor.summa
                    sponsor_dictionary[month] = jami_tolangan_summa

        byekt = {}
        byekt['tolanishi_kerak_summa'] = tolanishi_kerak_summa
        byekt['jami_tolangan_summa'] = jami_tolangan_summa
        byekt['sponsor'] = sponsor_dictionary
        byekt['student'] = student_dictionary
        return JsonResponse(byekt)


class DetailSponsorView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request, id):
        humans = Sponsor.objects.get(id=id)
        serializer = SponsorSerializer(humans)
        return Response(data=serializer.data)

    def patch(self, request, id):
        sponsor = Sponsor.objects.get(id=id)
        serializer = SponsorSerializer(instance=sponsor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AllSponsorView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        humans = Sponsor.objects.all().order_by('-created_at')
        search_query = request.GET.get('q', '')
        if search_query:
            humans = humans.filter(username__icontains=search_query)

        paginator = PageNumberPagination()
        page_obj = paginator.paginate_queryset(humans, request)

        serializer = SponsorSerializer(page_obj, many=True)
        return paginator.get_paginated_response(serializer.data)


class FilterSponsorView(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request):
        humans = Sponsor.objects.all().order_by('-created_at')
        search_summa = request.GET.get('q', '')
        search_holati = request.GET.get('t', '')
        if search_summa:
            if not search_summa=='barchasi':
                humans = humans.filter(summa=search_summa)

        if search_holati:
            if not search_holati=='barchasi':
                humans = humans.filter(holati=search_holati)

        serializer = SponsorSerializer(humans, many=True)
        return Response(data=serializer.data)













