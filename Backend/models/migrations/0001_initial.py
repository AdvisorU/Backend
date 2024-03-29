# Generated by Django 4.2.1 on 2024-03-06 04:24

import Backend.utils.snowflake
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.BigIntegerField(default=Backend.utils.snowflake.generate_uid, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(blank=True, max_length=75, null=True, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('nickname', models.TextField(default='User')),
                ('icon', models.TextField(blank=True, null=True)),
                ('registration_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigIntegerField(default=Backend.utils.snowflake.generate_uid, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('major', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('credit_hours', models.IntegerField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NUPathAttribute',
            fields=[
                ('id', models.BigIntegerField(default=Backend.utils.snowflake.generate_uid, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('short_name', models.CharField(db_index=True, max_length=255)),
                ('user_code', models.CharField(db_index=True, max_length=255, null=True)),
                ('description', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CoursePreRequisite',
            fields=[
                ('id', models.BigIntegerField(default=Backend.utils.snowflake.generate_uid, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_pre_requisites_course', to='models.course')),
                ('pre_requisite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_pre_requisites_pre_requisite', to='models.course')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CourseNUPathAttribute',
            fields=[
                ('id', models.BigIntegerField(default=Backend.utils.snowflake.generate_uid, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_nu_path_attributes_attribute', to='models.nupathattribute')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_nu_path_attributes_course', to='models.course')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CourseCoRequisite',
            fields=[
                ('id', models.BigIntegerField(default=Backend.utils.snowflake.generate_uid, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('co_requisite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_co_requisites_co_requisite', to='models.course')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_co_requisites_course', to='models.course')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
