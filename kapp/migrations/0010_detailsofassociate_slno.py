# Generated by Django 5.0.3 on 2024-07-07 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kapp', '0009_rename_net_income_balancesheetandplaccount_net_income1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailsofassociate',
            name='slno',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]