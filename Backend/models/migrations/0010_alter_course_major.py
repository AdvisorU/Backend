# Generated by Django 4.2.1 on 2024-03-16 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0009_chat_chatcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_major', to='models.major'),
        ),
    ]
