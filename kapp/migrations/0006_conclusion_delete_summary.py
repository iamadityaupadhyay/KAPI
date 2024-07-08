# Generated by Django 5.0.3 on 2024-07-07 12:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kapp', '0005_rename_acknowledgement_itrverification_acknowledgement_y1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conclusion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('financial', models.CharField(blank=True, max_length=200, null=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='summary', to='kapp.applicant')),
            ],
        ),
        migrations.DeleteModel(
            name='Summary',
        ),
    ]
