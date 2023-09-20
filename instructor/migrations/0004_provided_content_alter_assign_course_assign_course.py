# Generated by Django 4.0.1 on 2022-04-23 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0003_rename_year_assign_course_year_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provided_Content',
            fields=[
                ('provided_content_id', models.AutoField(primary_key=True, serialize=False)),
                ('term', models.IntegerField()),
                ('study_center', models.CharField(max_length=3)),
                ('instructor_id', models.CharField(max_length=15)),
                ('assigned_course', models.CharField(max_length=100)),
                ('content_title', models.CharField(max_length=20)),
                ('content_desc', models.CharField(max_length=200)),
                ('content_file', models.FileField(blank=True, default='', null=True, upload_to='content/file')),
            ],
        ),
        migrations.AlterField(
            model_name='assign_course',
            name='assign_course',
            field=models.CharField(max_length=100),
        ),
    ]
