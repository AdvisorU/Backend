# Generated by Django 4.2.1 on 2024-03-08 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0004_courseprerequisite_minimum_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseprerequisite',
            name='parent_pre_requisite',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_pre_requisites_parent_pre_requisite', to='models.courseprerequisite'),
        ),
        migrations.AlterField(
            model_name='courseprerequisite',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_pre_requisites_course', to='models.course'),
        ),
        migrations.AlterField(
            model_name='courseprerequisite',
            name='pre_requisite',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_pre_requisites_pre_requisite', to='models.course'),
        ),
    ]
