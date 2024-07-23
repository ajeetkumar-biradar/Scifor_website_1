
from django.urls import path
from . import views

urlpatterns = [
    path('carrer/', views.carrer, name='carrer'),

    path('alljobs/', views.main, name='jobs'),
    path('job/', views.getJob.as_view(), name='get-job'),
    path('jobs/', views.jobsPgae, name='job-page'),
    path('getAllJobs/', views.getAllJobs.as_view(), name='getAllJobs'),
    path('application/', views.ApplicationView.as_view(), name='ApplicationView'),

    path('', views.home, name='home'),
    path('submit-form/', views.submit_form, name='submit_form'),
    path('inquiry-form/', views.inquiry_form, name='inquiry_form'),
    path('services/', views.web_service, name='services'),
    path('case_study/', views.case_study, name='case_study'),

    path('community/', views.community_engagement_page, name='community_engagement_page'),
    path('article/<int:id>/', views.article_detail, name='article_detail'),


    path('company-name/', views.company_name, name='company_name'),
    path('about-company/', views.about_company, name='about_company'),
    path('team-profiles/', views.team_profiles, name='team_profiles'),
    path('who-are-we/', views.who_are_we, name='who_are_we'),
    path('achievements/', views.achievements, name='achievements'),
    path('get-in-touch/', views.get_in_touch, name='get_in_touch'),
    path('about-us/', views.about_us_page, name='about_us_page'),

    path('software-development/', views.software_development, name='software_development'),
    path('devops-services/', views.devops_services, name='devops_services'),
    path('game-development/', views.game_development, name='game_development'),
    path('ui-ux-design/', views.ui_ux_design, name='ui_ux_design'),

]
