# Generated by Django 5.1.dev20231208084611 on 2024-01-03 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0007_customer_user_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]