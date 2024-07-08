# Generated by Django 5.0.3 on 2024-07-08 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kapp', '0011_finalconclusion'),
    ]

    operations = [
        migrations.AddField(
            model_name='itrverification',
            name='pan_y1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='itrverification',
            name='pan_y2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='itrverification',
            name='pan_y3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='itrverification',
            name='year1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='itrverification',
            name='year2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='itrverification',
            name='year3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='rv_date_of_visit',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coapplicant',
            name='rv_date_of_visit',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='guarantor',
            name='rv_date_of_visit',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='propertiesproposed',
            name='date_of_visit',
            field=models.DateField(blank=True, null=True),
        ),
    ]
