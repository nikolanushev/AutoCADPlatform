# Generated by Django 4.1 on 2022-09-03 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutoCadApp', '0007_link_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='answer',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='optionA',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='optionB',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='optionC',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
