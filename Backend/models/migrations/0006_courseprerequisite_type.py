# Generated by Django 4.2.1 on 2024-03-08 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0005_courseprerequisite_parent_pre_requisite_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseprerequisite',
            name='type',
            field=models.CharField(db_index=True, default='course', max_length=255),
        ),
    ]
