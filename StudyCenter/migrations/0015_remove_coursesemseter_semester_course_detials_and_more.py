# Generated by Django 4.0.1 on 2022-02-07 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudyCenter', '0014_alter_coursesemseter_semester_course_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursesemseter',
            name='semester_course_detials',
        ),
        migrations.RemoveField(
            model_name='coursesemseter',
            name='semester_course_name',
        ),
    ]
