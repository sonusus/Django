# Generated by Django 4.2.1 on 2023-07-12 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CounsellingApp', '0003_question_rename_request_requestuser_requests_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frm', models.CharField(max_length=100)),
                ('to', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('filetype', models.CharField(max_length=100)),
                ('file', models.CharField(max_length=300)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=100),
        ),
    ]
