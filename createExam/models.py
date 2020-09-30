from django.db import models


class Exam(models.Model):
    title = models.CharField(max_length=70, blank=False)
    description = models.CharField(max_length=200,blank=True)
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

class ExamSubCategory(models.Model):
    title = models.CharField(max_length=70, blank=False)
    description = models.CharField(max_length=200,blank=True)
    published = models.BooleanField(default=True)
    exam_id = models.ForeignKey(Exam, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

class ExamSubject(models.Model):
    title = models.CharField(max_length=70, blank=False)
    description = models.CharField(max_length=200,blank=True)
    published = models.BooleanField(default=True)
    exam_id = models.ForeignKey(Exam, on_delete=models.CASCADE)
    sub_cat_id = models.ForeignKey(ExamSubCategory, on_delete=models.CASCADE, default=1)
    created = models.DateTimeField(auto_now_add=True)

class ExamTopic(models.Model):
    title = models.CharField(max_length=70, blank=False)
    description = models.CharField(max_length=200,blank=True)
    published = models.BooleanField(default=True)
    exam_id = models.ForeignKey(Exam, on_delete=models.CASCADE)
    sub_cat_id = models.ForeignKey(ExamSubCategory, on_delete=models.CASCADE, default=1)
    sub_id = models.ForeignKey(ExamSubject, on_delete=models.CASCADE)
    parent_topic_id = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)