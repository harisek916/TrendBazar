# Generated by Django 4.2.6 on 2024-03-14 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_basketitem_basket_alter_basketitem_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basketitem',
            name='total',
        ),
    ]
