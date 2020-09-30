from rest_framework import serializers 
from createExam.models import Exam
from createExam.models import ExamSubCategory
from createExam.models import ExamSubject
from createExam.models import ExamTopic
 
 
class ExamSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Exam
        fields = ('id',
                  'title',
                  'description',
                  'published',
                  'created')

class ExamSubCatSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = ExamSubCategory
        fields = ('id',
                  'title',
                  'description',
                  'published',
                  'exam_id',
                  'created')

class ExamSubjectSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = ExamSubject
        fields = ('id',
                  'title',
                  'description',
                  'published',
                  'exam_id',
                  'sub_cat_id',
                  'created')

class ExamTopicSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = ExamTopic
        fields = ('id',
                  'title',
                  'description',
                  'published',
                  'exam_id',
                  'sub_cat_id',
                  'sub_id',
                  'parent_topic_id',
                  'created')
