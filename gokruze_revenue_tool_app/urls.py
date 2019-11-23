from django.urls import include, path, re_path
from django.contrib import admin
from gokruze_revenue_tool_app import views

app_name = 'gokruze_revenue_tool_app'

urlpatterns = [
    #Data_dump_api_dataview_url
    path('data/dump',views.Data_dump_api_dataview,name='data_dump'),

    #Data_dump_routes_master_form url
    path('data/routes/form',views.Data_dump_routes_master_form_view,name='data_routes_form'),

    #Data_dump_routes_master_form_submit url
    path('data/routes/form/submit',views.Data_dump_routes_master_form_submit_view,name='data_routes_form_submit'),

    #Data_dump_routes_master_list_view url
    path('data/routes/list',views.Data_dump_routes_master_list_view,name='data_dump_routes_master_list'),

    #Data_dump_routes_report url
    path('data/routes/report',views.Data_dump_routes_report_view,name='data_dump_routes_report'),

    #Data_dump_routes_summary
    path('data/routes/summary',views.Data_dump_routes_summary_view,name='data_dump_routes_summary'),





    





    
]
