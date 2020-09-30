from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from createExam.models import Exam
from createExam.serializers import ExamSerializer
from createExam.models import ExamSubCategory
from createExam.serializers import ExamSubCatSerializer
from createExam.models import ExamSubject
from createExam.serializers import ExamSubjectSerializer
from createExam.models import ExamTopic
from createExam.serializers import ExamTopicSerializer
from rest_framework.decorators import api_view

#Add Exam
@api_view(['POST'])
def exam_add(request):
    if request.method == 'POST':
        exam_data = JSONParser().parse(request)
        exam_serializer = ExamSerializer(data=exam_data)
        if exam_serializer.is_valid():
            exam_serializer.save()
            return JsonResponse(exam_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(exam_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Get Exam List
@api_view(['GET'])
def exam_list(request):
    if request.method == 'GET': 
        exam = Exam.objects.all()
        exam_serializer = ExamSerializer(exam, many=True) 
        return JsonResponse(exam_serializer.data, safe=False) 

#Add Exam Sub Category
@api_view(['POST'])
def exam_sub_cat_add(request):
    if request.method == 'POST':
        exam_sub_cat_data = JSONParser().parse(request)
        exam_sub_cat_serializer = ExamSubCatSerializer(data=exam_sub_cat_data)
        if exam_sub_cat_serializer.is_valid():
            exam_sub_cat_serializer.save()
            return JsonResponse(exam_sub_cat_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(exam_sub_cat_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#Get Exam Sub Cat List
@api_view(['GET'])
def exam_sub_cat_list(request):
    if request.method == 'GET': 
        exam_sub_cat = ExamSubCategory.objects.all()
        exam_sub_cat_serializer = ExamSubCatSerializer(exam_sub_cat, many=True) 
        return JsonResponse(exam_sub_cat_serializer.data, safe=False) 

#Add Exam Subject 
@api_view(['POST'])
def exam_sub_add(request):
    if request.method == 'POST':
        exam_sub_data = JSONParser().parse(request)
        exam_sub_serializer = ExamSubjectSerializer(data=exam_sub_data)
        if exam_sub_serializer.is_valid():
            exam_sub_serializer.save()
            return JsonResponse(exam_sub_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(exam_sub_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#Get Exam Subject List
@api_view(['GET'])
def exam_sub_list(request):
    if request.method == 'GET': 
        exam_sub = ExamSubject.objects.all()
        exam_sub_serializer = ExamSubjectSerializer(exam_sub, many=True) 
        return JsonResponse(exam_sub_serializer.data, safe=False) 

#Add Exam Topic 
@api_view(['POST'])
def exam_topic_add(request):
    if request.method == 'POST':
        exam_topic_data = JSONParser().parse(request)
        exam_topic_serializer = ExamTopicSerializer(data=exam_topic_data)
        if exam_topic_serializer.is_valid():
            exam_topic_serializer.save()
            return JsonResponse(exam_topic_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(exam_topic_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#Get Exam Topic List
@api_view(['GET'])
def exam_topic_list(request):
    if request.method == 'GET': 
        exam_topic = ExamTopic.objects.all()
        exam_topic_serializer = ExamTopicSerializer(exam_topic, many=True) 
        return JsonResponse(exam_topic_serializer.data, safe=False) 

@api_view(['GET'])
def exam_details(request, pk):
    try: 
        exam = Exam.objects.filter(id=pk) 
        exam_serializer = ExamSerializer(exam, many=True)

        exam_sub_cat_list = ExamSubCategory.objects.filter(exam_id=pk) 
        exam_sub_cat_serializer = ExamSubCatSerializer(exam_sub_cat_list, many=True)

        exam_sub_list = ExamSubject.objects.filter(exam_id=pk) 
        exam_sub_serializer = ExamSubjectSerializer(exam_sub_list, many=True)

        exam_topic_list = ExamTopic.objects.filter(exam_id=pk) 
        exam_topic_serializer = ExamTopicSerializer(exam_topic_list, many=True)

        exam_data = {"exam":exam_serializer.data, "subcategory":exam_sub_cat_serializer.data, "subject":exam_sub_serializer.data, "topic":exam_topic_serializer.data}
        return JsonResponse(exam_data, safe=False)

    except Exam.DoesNotExist: 
        return JsonResponse({'message': 'The exam does not exist'}, status=status.HTTP_404_NOT_FOUND) 

  
    
        