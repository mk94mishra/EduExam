from django.conf.urls import url 
from createExam import views 
 
urlpatterns = [ 
    url(r'^api/exam-add$', views.exam_add),
    url(r'^api/exam-list$', views.exam_list),
    url(r'^api/exam-subcat-add$', views.exam_sub_cat_add),
    url(r'^api/exam-subcat-list$', views.exam_sub_cat_list),
    url(r'^api/exam-sub-add$', views.exam_sub_add),
    url(r'^api/exam-sub-list$', views.exam_sub_list),
    url(r'^api/exam-topic-add$', views.exam_topic_add),
    url(r'^api/exam-topic-list$', views.exam_topic_list),
    url(r'^api/exam/(?P<pk>[0-9]+)$', views.exam_details)
]