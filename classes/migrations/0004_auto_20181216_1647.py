# Generated by Django 2.0.6 on 2018-12-16 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0003_auto_20181216_1546'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ('name', 'exam_grade')},
        ),
        migrations.AlterOrderWithRespectTo(
            name='student',
            order_with_respect_to=None,
        ),
    ]