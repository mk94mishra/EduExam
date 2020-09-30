# eduExam

Technology
Python 3.8.5
Django 3.1.1
Django Rest Framework 3.12.1
psycopg2 2.8.6
django-cors-headers 3.5.0


------------------------------------------
install following Technology:
pip install djangorestframework
pip install psycopg2
pip install django-cors-headers

----------------------------------
Api Links:

Add Exam
http://127.0.0.1:8000/api/exam-add

    {
            "title":"Exam Name",
            "description":"For Exam 2020",
            "published":"true"
    }
Show All Exam List
http://127.0.0.1:8000/api/exam-list

Add Sub Category
http://127.0.0.1:8000/api/exam-subcat-add

    {
            "title":"Exam Sub Category",
            "description":"For Exam 2020",
            "published":"true",
            "exam_id":"1"
   
    }
Show All Sub Category
http://127.0.0.1:8000/api/exam-subcat-list

Add Subject
http://127.0.0.1:8000/api/exam-sub-add

    {
            "title":"Exam Subject",
            "description":"For Exam 2020",
            "published":"true",
            "exam_id":"1",
            "sub_cat_id":"1"
   
    }

Show All subject List
http://127.0.0.1:8000/api/exam-sub-list

Add Topic
http://127.0.0.1:8000/api/exam-topic-add

    {
            "title":"Exam Topic",
            "description":"For Exam 2020",
            "published":"true",
            "exam_id":"1",
            "sub_cat_id":"1",
            "sub_id":"1"
   
    }

Add Sub Topic
use parent topic id only for sub topics
    {
            "title":"Exam Topic",
            "description":"For Exam 2020",
            "published":"true",
            "exam_id":"1",
            "sub_cat_id":"1",
            "sub_id":"1",
            "parent_topic_id":"1"
   
    }

Show All Topic List
http://127.0.0.1:8000/api/exam-topic-list

Show Single Exam Hierarchy 
http://127.0.0.1:8000/api/exam/1 



