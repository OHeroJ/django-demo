# Generated by Django 5.0.3 on 2024-05-11 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("emoticons", "0004_alter_pic_keywords"),
    ]

    operations = [
        migrations.AlterField(
            model_name="topic",
            name="keywords",
            field=models.CharField(
                blank=True, help_text="用于搜索", max_length=100, null=True
            ),
        ),
    ]