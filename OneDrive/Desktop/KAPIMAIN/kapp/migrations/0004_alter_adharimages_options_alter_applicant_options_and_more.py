# Generated by Django 5.0.3 on 2024-07-09 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kapp', '0003_gstimages_gst_images_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adharimages',
            options={'verbose_name': 'Aadhar Images'},
        ),
        migrations.AlterModelOptions(
            name='applicant',
            options={'verbose_name': 'Applicant', 'verbose_name_plural': 'Applicants'},
        ),
        migrations.AlterModelOptions(
            name='applicantimage',
            options={'verbose_name': 'Applicant Image', 'verbose_name_plural': 'Applicant Images'},
        ),
        migrations.AlterModelOptions(
            name='applicantimagebusiness',
            options={'verbose_name': 'Applicant Business Image', 'verbose_name_plural': 'Applicant Business Images'},
        ),
        migrations.AlterModelOptions(
            name='backgroundverification',
            options={'verbose_name': 'Background Verification', 'verbose_name_plural': 'Background Verifications'},
        ),
        migrations.AlterModelOptions(
            name='balancesheetandplaccount',
            options={'verbose_name': 'Balance Sheet and PL Account', 'verbose_name_plural': 'Balance Sheets and PL Accounts'},
        ),
        migrations.AlterModelOptions(
            name='buyers',
            options={'verbose_name': 'Buyer', 'verbose_name_plural': 'Buyers'},
        ),
        migrations.AlterModelOptions(
            name='coapplicant',
            options={'verbose_name': 'Co-Applicant', 'verbose_name_plural': 'Co-Applicants'},
        ),
        migrations.AlterModelOptions(
            name='coapplicantimage',
            options={'verbose_name': 'Co-Applicant Image', 'verbose_name_plural': 'Co-Applicant Images'},
        ),
        migrations.AlterModelOptions(
            name='coapplicantimagebusiness',
            options={'verbose_name': 'Co-Applicant Business Image', 'verbose_name_plural': 'Co-Applicant Business Images'},
        ),
        migrations.AlterModelOptions(
            name='detailsofassociate',
            options={'verbose_name': 'Detail of Associate', 'verbose_name_plural': 'Details of Associates'},
        ),
        migrations.AlterModelOptions(
            name='guarantor',
            options={'verbose_name': 'Guarantor', 'verbose_name_plural': 'Guarantors'},
        ),
        migrations.AlterModelOptions(
            name='guarantorimage',
            options={'verbose_name': 'Guarantor Image', 'verbose_name_plural': 'Guarantor Images'},
        ),
        migrations.AlterModelOptions(
            name='guarantorimagebusiness',
            options={'verbose_name': 'Guarantor Business Image', 'verbose_name_plural': 'Guarantor Business Images'},
        ),
        migrations.AlterModelOptions(
            name='insurancedetails',
            options={'verbose_name': 'Insurance Detail', 'verbose_name_plural': 'Insurance Details'},
        ),
        migrations.AlterModelOptions(
            name='manufacturingentities',
            options={'verbose_name': 'Manufacturing Entity', 'verbose_name_plural': 'Manufacturing Entities'},
        ),
        migrations.AlterModelOptions(
            name='otherparticulars',
            options={'verbose_name': 'Other Particular', 'verbose_name_plural': 'Other Particulars'},
        ),
        migrations.AlterModelOptions(
            name='personalassetsofproprietor',
            options={'verbose_name': 'Personal Asset of Proprietor', 'verbose_name_plural': 'Personal Assets of Proprietors'},
        ),
        migrations.AlterModelOptions(
            name='suppliers',
            options={'verbose_name': 'Supplier', 'verbose_name_plural': 'Suppliers'},
        ),
    ]
