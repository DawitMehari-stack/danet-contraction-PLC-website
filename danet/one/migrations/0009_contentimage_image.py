# Generated by Django 4.1.3 on 2022-12-22 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("one", "0008_alter_projectimage_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="contentimage",
            name="image",
            field=models.ImageField(default="Null", upload_to="images/"),
        ),
    ]
