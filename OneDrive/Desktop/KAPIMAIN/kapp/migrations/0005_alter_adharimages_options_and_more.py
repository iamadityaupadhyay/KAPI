# Generated by Django 5.0.3 on 2024-07-09 13:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kapp', '0004_alter_adharimages_options_alter_applicant_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adharimages',
            options={'verbose_name': 'Aadhar Image', 'verbose_name_plural': 'Aadhar Images'},
        ),
        migrations.AlterModelOptions(
            name='balancesheetandplaccount',
            options={'verbose_name': 'Balance Sheet and P&L Account', 'verbose_name_plural': 'Balance Sheets and P&L Accounts'},
        ),
        migrations.AlterModelOptions(
            name='finalconclusion',
            options={'verbose_name': 'Final Conclusion', 'verbose_name_plural': 'Final Conclusions'},
        ),
        migrations.AlterModelOptions(
            name='gstimages',
            options={'verbose_name': 'GST Image', 'verbose_name_plural': 'GST Images'},
        ),
        migrations.AlterModelOptions(
            name='itrverification',
            options={'verbose_name': 'ITR Verification', 'verbose_name_plural': 'ITR Verifications'},
        ),
        migrations.AlterModelOptions(
            name='panimages',
            options={'verbose_name': 'PAN Image', 'verbose_name_plural': 'PAN Images'},
        ),
        migrations.AlterModelOptions(
            name='propertiesproposed',
            options={'verbose_name': 'Proposed Property', 'verbose_name_plural': 'Proposed Properties'},
        ),
        migrations.AddField(
            model_name='adharimages',
            name='Guarantor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adhar_images', to='kapp.guarantor'),
        ),
        migrations.AddField(
            model_name='adharimages',
            name='coapplicant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adhar_images', to='kapp.coapplicant'),
        ),
        migrations.AddField(
            model_name='gstimages',
            name='Guarantor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gst_images', to='kapp.guarantor'),
        ),
        migrations.AddField(
            model_name='gstimages',
            name='coapplicant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gst_images', to='kapp.coapplicant'),
        ),
        migrations.AddField(
            model_name='panimages',
            name='Guarantor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pan_images', to='kapp.guarantor'),
        ),
        migrations.AddField(
            model_name='panimages',
            name='coapplicant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pan_images', to='kapp.coapplicant'),
        ),
        migrations.AlterField(
            model_name='itrverification',
            name='acknowledgement_y1',
            field=models.IntegerField(blank=True, null=True, verbose_name='Acknowledgement Year 1'),
        ),
        migrations.AlterField(
            model_name='itrverification',
            name='acknowledgement_y2',
            field=models.IntegerField(blank=True, null=True, verbose_name='Acknowledgement Year 2'),
        ),
        migrations.AlterField(
            model_name='itrverification',
            name='acknowledgement_y3',
            field=models.IntegerField(blank=True, null=True, verbose_name='Acknowledgement Year 3'),
        ),
        migrations.AlterField(
            model_name='itrverification',
            name='date_of_itr_filling_y1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Date of ITR Filing Year 1'),
        ),
        migrations.AlterField(
            model_name='itrverification',
            name='date_of_itr_filling_y2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Date of ITR Filing Year 2'),
        ),
        migrations.AlterField(
            model_name='itrverification',
            name='date_of_itr_filling_y3',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Date of ITR Filing Year 3'),
        ),
        migrations.AlterField(
            model_name='itrverification',
            name='pan_y1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='PAN Year 1'),
        ),
        migrations.AlterField(
            model_name='itrverification',
            name='pan_y2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='PAN Year 2'),
        ),
        migrations.AlterField(
            model_name='itrverification',
            name='pan_y3',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='PAN Year 3'),
        ),
        migrations.AlterField(
            model_name='itrverification',
            name='total_gross_income_y1',
            field=models.IntegerField(blank=True, null=True, verbose_name='Total Gross Income Year 1'),
        ),
        migrations.AlterField(
            model_name='itrverification',
            name='total_gross_income_y2',
            field=models.IntegerField(blank=True, null=True, verbose_name='Total Gross Income Year 2'),
        ),
        migrations.AlterField(
            model_name='itrverification',
            name='total_gross_income_y3',
            field=models.IntegerField(blank=True, null=True, verbose_name='Total Gross Income Year 3'),
        ),
        migrations.AlterField(
            model_name='itrverification',
            name='total_taxable_income_y1',
            field=models.IntegerField(blank=True, null=True, verbose_name='Total Taxable Income Year 1'),
        ),
        migrations.AlterField(
            model_name='itrverification',
            name='total_taxable_income_y2',
            field=models.IntegerField(blank=True, null=True, verbose_name='Total Taxable Income Year 2'),
        ),
        migrations.AlterField(
            model_name='itrverification',
            name='total_taxable_income_y3',
            field=models.IntegerField(blank=True, null=True, verbose_name='Total Taxable Income Year 3'),
        ),
        migrations.AlterField(
            model_name='itrverification',
            name='whether_itr_filler_properly_y1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ITR Filler Properly Year 1'),
        ),
        migrations.AlterField(
            model_name='itrverification',
            name='whether_itr_filler_properly_y2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ITR Filler Properly Year 2'),
        ),
        migrations.AlterField(
            model_name='itrverification',
            name='whether_itr_filler_properly_y3',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ITR Filler Properly Year 3'),
        ),
        migrations.AlterField(
            model_name='itrverification',
            name='year1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Year 1'),
        ),
        migrations.AlterField(
            model_name='itrverification',
            name='year2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Year 2'),
        ),
        migrations.AlterField(
            model_name='itrverification',
            name='year3',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Year 3'),
        ),
    ]
