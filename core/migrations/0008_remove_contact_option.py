# Generated by Django 4.2.5 on 2023-10-14 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_contact_option'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='option',
        ),
    ]
