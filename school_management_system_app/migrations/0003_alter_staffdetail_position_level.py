# Generated by Django 4.1.2 on 2022-10-20 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management_system_app', '0002_studentdetail_proctor_master'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffdetail',
            name='position_level',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
