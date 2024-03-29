# Generated by Django 2.2.7 on 2019-11-23 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data_Dump',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Data_Dump_Date_Of_Data_Dump_Created', models.DateTimeField(auto_now_add=True)),
                ('Data_Dump_Route_Code', models.CharField(max_length=264)),
                ('Data_Dump_Daily_AM', models.IntegerField(blank=True)),
                ('Data_Dump_Monthly_AM', models.IntegerField(blank=True)),
                ('Data_Dump_Daily_PM', models.IntegerField(blank=True)),
                ('Data_Dump_Monthly_PM', models.IntegerField(blank=True)),
                ('Data_Dump_Total', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Routes_Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Routes_Master_Route_Ends_From', models.CharField(blank=True, max_length=264)),
                ('Routes_Master_Route_Starts_From', models.CharField(blank=True, max_length=264)),
                ('Routes_Master_Duty', models.CharField(blank=True, max_length=264)),
                ('Routes_Master_Bus_No', models.CharField(blank=True, max_length=264)),
                ('Routes_Master_Seating_Capacity', models.IntegerField(blank=True)),
                ('Routes_Master_Manufacturing_Company', models.CharField(blank=True, max_length=264)),
                ('Routes_Master_Km', models.IntegerField(blank=True)),
                ('Routes_Master_Costing', models.IntegerField(blank=True)),
                ('Routes_Master_Bus_Vendor', models.CharField(blank=True, max_length=264)),
                ('Routes_Master_Route_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gokruze_revenue_tool_app.Data_Dump')),
            ],
        ),
    ]
