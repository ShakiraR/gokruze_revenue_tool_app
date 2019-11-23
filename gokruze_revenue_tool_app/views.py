from django.shortcuts import render
from gokruze_revenue_tool_app import views

# Create your views here.
#Data_dump_api_dataview
def Data_dump_api_dataview(request):
    data = { }
    return render(request, 'gokruze_revenue_tool_app/data_dump.html', data)

#Data_dump_routes_master_form_view
def Data_dump_routes_master_form_view(request):
    data = { }
    return render(request, 'gokruze_revenue_tool_app/data_routes_form.html', data) 

#Data_dump_routes_master_form_submit_view
def Data_dump_routes_master_form_submit_view(request):
    data = { }
    return render(request, 'gokruze_revenue_tool_app/data_routes_form_submit.html', data) 

#Data_dump_routes_master_list_view
def Data_dump_routes_master_list_view(request):
    data = { }
    return render(request, 'gokruze_revenue_tool_app/data_dump_routes_master_list.html', data) 

#Data_dump_routes_report_view
def Data_dump_routes_report_view(request):
    data = { }
    return render(request, 'gokruze_revenue_tool_app/data_dump_routes_report.html', data) 

#Data_dump_routes_summary_view
def Data_dump_routes_summary_view(request):
    data = { }
    return render(request, 'gokruze_revenue_tool_app/data_dump_routes_summary.html', data)      






