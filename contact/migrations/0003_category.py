# Generated by Django 5.2.1 on 2025-05-19 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_picture_contact_show_alter_contact_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
