from django.contrib import admin
from gokruze_revenue_tool_app.models import Data_Dump,Routes_Master



# Register your models here.
class Data_DumpAdmin(admin.ModelAdmin):
    list_filter = ["Data_Dump_Date_Of_Data_Dump_Created"]
    list_display = [
        "Data_Dump_Date_Of_Data_Dump_Created",
        "Data_Dump_Route_Code",
        "Data_Dump_Daily_AM",
        "Data_Dump_Monthly_AM",
        "Data_Dump_Daily_PM",
        "Data_Dump_Monthly_PM",
        "Data_Dump_Total",
        ]

class Route_MasterAdmin(admin.ModelAdmin):
    search_fields = ["Routes_Master_Route_Starts_From","Routes_Master_Route_Ends_From"]
    list_filter = ["Routes_Master_Bus_Vendor"]
    list_display = [
        "Routes_Master_Route_Code",
        "Routes_Master_Route_Starts_From",
        "Routes_Master_Route_Ends_From",
        "Routes_Master_Duty",
        "Routes_Master_Bus_No",
        "Routes_Master_Seating_Capacity",
        "Routes_Master_Manufacturing_Company",
        "Routes_Master_Km",
        "Routes_Master_Costing",
        "Routes_Master_Bus_Vendor",
    ]
admin.site.register(Data_Dump, Data_DumpAdmin)
admin.site.register(Routes_Master, Route_MasterAdmin)