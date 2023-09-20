# Generated by Django 4.0.1 on 2022-02-07 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_course_release_date'),
        ('StudyCenter', '0017_alter_semester_semester_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseSemseter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
                ('s_course_semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudyCenter.semester')),
            ],
        ),
    ]
