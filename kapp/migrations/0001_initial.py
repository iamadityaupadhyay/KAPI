# Generated by Django 5.0.3 on 2024-05-05 16:21

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(choices=[('Punjab & Sind', 'Punjab & Sind'), ('Bank of India', 'Bank of India'), ('Union Bank Of India', 'Union Bank Of India'), ('Canara Bank', 'Canara Bank'), ('SIDBI Bank', 'SIDBI Bank'), ('Bank Of Baroda', 'Bank Of Baroda'), ('Uco Bank', 'Uco Bank')], max_length=100)),
                ('branch_name', models.CharField(max_length=100)),
                ('loan_type', models.CharField(max_length=100)),
                ('loan_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rv_name', models.CharField(blank=True, max_length=100, null=True)),
                ('rv_contact_no', models.CharField(blank=True, max_length=15, null=True)),
                ('rv_aadhaar_no', models.CharField(blank=True, max_length=12, null=True)),
                ('rv_pan_no', models.CharField(blank=True, max_length=10, null=True)),
                ('rv_present_address', models.TextField(blank=True, null=True)),
                ('rv_permanent_address', models.TextField(blank=True, null=True)),
                ('rv_ownership_proof_type', models.CharField(blank=True, choices=[('E-Bill/Water Tax', 'E-Bill/Water Tax')], max_length=20, null=True)),
                ('rv_e_bill_or_water_tax_document', models.FileField(blank=True, null=True, upload_to='rv_e_bill_water_tax_documents/')),
                ('rv_premises_is', models.BooleanField(blank=True, null=True)),
                ('rv_residency_status', models.CharField(blank=True, max_length=50, null=True)),
                ('rv_duration_to_stay', models.CharField(blank=True, max_length=50, null=True)),
                ('rv_landmark', models.CharField(blank=True, max_length=100, null=True)),
                ('rv_area_of_house', models.CharField(blank=True, max_length=100, null=True)),
                ('rv_color_of_house', models.CharField(blank=True, max_length=50, null=True)),
                ('rv_num_of_persons_living', models.PositiveIntegerField(blank=True, null=True)),
                ('rv_num_of_persons_earning', models.PositiveIntegerField(blank=True, null=True)),
                ('rv_neighbour_name', models.CharField(blank=True, max_length=100, null=True)),
                ('rv_neighbour_contact_no', models.CharField(blank=True, max_length=15, null=True)),
                ('rv_met_person_at_home', models.BooleanField(blank=True, null=True)),
                ('rv_relation_with_met_person', models.CharField(blank=True, max_length=100, null=True)),
                ('ev_company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('ev_company_address', models.TextField(blank=True, null=True)),
                ('ev_date_of_joining', models.DateField(blank=True, null=True)),
                ('ev_designation_of_applicant', models.CharField(blank=True, max_length=100, null=True)),
                ('ev_details_confirmed_by', models.CharField(blank=True, max_length=100, null=True)),
                ('ev_staff_name', models.CharField(blank=True, max_length=100, null=True)),
                ('ev_staff_designation', models.CharField(blank=True, max_length=100, null=True)),
                ('ev_staff_contact_no', models.CharField(blank=True, max_length=15, null=True)),
                ('sev_occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('sev_address', models.TextField(blank=True, null=True)),
                ('sev_details_confirmed_by', models.CharField(blank=True, max_length=100, null=True)),
                ('sev_relation_met_person_with_applicant', models.CharField(blank=True, max_length=100, null=True)),
                ('bv_company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('bv_business_address', models.TextField(blank=True, null=True)),
                ('bv_gstin_udyam_others_no', models.CharField(blank=True, max_length=100, null=True)),
                ('bv_num_of_employees', models.PositiveIntegerField(blank=True, null=True)),
                ('bv_landmark', models.CharField(blank=True, max_length=100, null=True)),
                ('bv_nature_of_business', models.CharField(blank=True, max_length=100, null=True)),
                ('bv_establishment_date', models.DateField(blank=True, null=True)),
                ('bv_designation_of_applicant', models.CharField(blank=True, max_length=100, null=True)),
                ('bv_met_person_at_business_place', models.BooleanField(blank=True, null=True)),
                ('bv_relation_met_person_with_applicant', models.CharField(blank=True, max_length=100, null=True)),
                ('bv_premises_is', models.BooleanField(blank=True, null=True)),
                ('bv_ownership_proof_type', models.CharField(blank=True, choices=[('E-Bill/Water Tax', 'E-Bill/Water Tax')], max_length=20, null=True)),
                ('bv_e_bill_or_water_tax_document', models.FileField(blank=True, null=True, upload_to='bv_e_bill_water_tax_documents/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FieldUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('mobile_number', models.CharField(max_length=15, unique=True)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='profile_photos/')),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('pin_code', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CoApplicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rv_name', models.CharField(blank=True, max_length=100, null=True)),
                ('rv_contact_no', models.CharField(blank=True, max_length=15, null=True)),
                ('rv_aadhaar_no', models.CharField(blank=True, max_length=12, null=True)),
                ('rv_pan_no', models.CharField(blank=True, max_length=10, null=True)),
                ('rv_present_address', models.TextField(blank=True, null=True)),
                ('rv_permanent_address', models.TextField(blank=True, null=True)),
                ('rv_ownership_proof_type', models.CharField(blank=True, choices=[('E-Bill/Water Tax', 'E-Bill/Water Tax')], max_length=20, null=True)),
                ('rv_e_bill_or_water_tax_document', models.FileField(blank=True, null=True, upload_to='rv_e_bill_water_tax_documents/')),
                ('rv_premises_is', models.BooleanField(blank=True, null=True)),
                ('rv_residency_status', models.CharField(blank=True, max_length=50, null=True)),
                ('rv_duration_to_stay', models.CharField(blank=True, max_length=50, null=True)),
                ('rv_landmark', models.CharField(blank=True, max_length=100, null=True)),
                ('rv_area_of_house', models.CharField(blank=True, max_length=100, null=True)),
                ('rv_color_of_house', models.CharField(blank=True, max_length=50, null=True)),
                ('rv_num_of_persons_living', models.PositiveIntegerField(blank=True, null=True)),
                ('rv_num_of_persons_earning', models.PositiveIntegerField(blank=True, null=True)),
                ('rv_neighbour_name', models.CharField(blank=True, max_length=100, null=True)),
                ('rv_neighbour_contact_no', models.CharField(blank=True, max_length=15, null=True)),
                ('rv_met_person_at_home', models.BooleanField(blank=True, null=True)),
                ('rv_relation_with_met_person', models.CharField(blank=True, max_length=100, null=True)),
                ('ev_company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('ev_company_address', models.TextField(blank=True, null=True)),
                ('ev_date_of_joining', models.DateField(blank=True, null=True)),
                ('ev_designation_of_applicant', models.CharField(blank=True, max_length=100, null=True)),
                ('ev_details_confirmed_by', models.CharField(blank=True, max_length=100, null=True)),
                ('ev_staff_name', models.CharField(blank=True, max_length=100, null=True)),
                ('ev_staff_designation', models.CharField(blank=True, max_length=100, null=True)),
                ('ev_staff_contact_no', models.CharField(blank=True, max_length=15, null=True)),
                ('sev_occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('sev_address', models.TextField(blank=True, null=True)),
                ('sev_details_confirmed_by', models.CharField(blank=True, max_length=100, null=True)),
                ('sev_relation_met_person_with_applicant', models.CharField(blank=True, max_length=100, null=True)),
                ('bv_company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('bv_business_address', models.TextField(blank=True, null=True)),
                ('bv_gstin_udyam_others_no', models.CharField(blank=True, max_length=100, null=True)),
                ('bv_num_of_employees', models.PositiveIntegerField(blank=True, null=True)),
                ('bv_landmark', models.CharField(blank=True, max_length=100, null=True)),
                ('bv_nature_of_business', models.CharField(blank=True, max_length=100, null=True)),
                ('bv_establishment_date', models.DateField(blank=True, null=True)),
                ('bv_designation_of_applicant', models.CharField(blank=True, max_length=100, null=True)),
                ('bv_met_person_at_business_place', models.BooleanField(blank=True, null=True)),
                ('bv_relation_met_person_with_applicant', models.CharField(blank=True, max_length=100, null=True)),
                ('bv_premises_is', models.BooleanField(blank=True, null=True)),
                ('bv_ownership_proof_type', models.CharField(blank=True, choices=[('E-Bill/Water Tax', 'E-Bill/Water Tax')], max_length=20, null=True)),
                ('bv_e_bill_or_water_tax_document', models.FileField(blank=True, null=True, upload_to='bv_e_bill_water_tax_documents/')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kapp.applicant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Guarantor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rv_name', models.CharField(blank=True, max_length=100, null=True)),
                ('rv_contact_no', models.CharField(blank=True, max_length=15, null=True)),
                ('rv_aadhaar_no', models.CharField(blank=True, max_length=12, null=True)),
                ('rv_pan_no', models.CharField(blank=True, max_length=10, null=True)),
                ('rv_present_address', models.TextField(blank=True, null=True)),
                ('rv_permanent_address', models.TextField(blank=True, null=True)),
                ('rv_ownership_proof_type', models.CharField(blank=True, choices=[('E-Bill/Water Tax', 'E-Bill/Water Tax')], max_length=20, null=True)),
                ('rv_e_bill_or_water_tax_document', models.FileField(blank=True, null=True, upload_to='rv_e_bill_water_tax_documents/')),
                ('rv_premises_is', models.BooleanField(blank=True, null=True)),
                ('rv_residency_status', models.CharField(blank=True, max_length=50, null=True)),
                ('rv_duration_to_stay', models.CharField(blank=True, max_length=50, null=True)),
                ('rv_landmark', models.CharField(blank=True, max_length=100, null=True)),
                ('rv_area_of_house', models.CharField(blank=True, max_length=100, null=True)),
                ('rv_color_of_house', models.CharField(blank=True, max_length=50, null=True)),
                ('rv_num_of_persons_living', models.PositiveIntegerField(blank=True, null=True)),
                ('rv_num_of_persons_earning', models.PositiveIntegerField(blank=True, null=True)),
                ('rv_neighbour_name', models.CharField(blank=True, max_length=100, null=True)),
                ('rv_neighbour_contact_no', models.CharField(blank=True, max_length=15, null=True)),
                ('rv_met_person_at_home', models.BooleanField(blank=True, null=True)),
                ('rv_relation_with_met_person', models.CharField(blank=True, max_length=100, null=True)),
                ('ev_company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('ev_company_address', models.TextField(blank=True, null=True)),
                ('ev_date_of_joining', models.DateField(blank=True, null=True)),
                ('ev_designation_of_applicant', models.CharField(blank=True, max_length=100, null=True)),
                ('ev_details_confirmed_by', models.CharField(blank=True, max_length=100, null=True)),
                ('ev_staff_name', models.CharField(blank=True, max_length=100, null=True)),
                ('ev_staff_designation', models.CharField(blank=True, max_length=100, null=True)),
                ('ev_staff_contact_no', models.CharField(blank=True, max_length=15, null=True)),
                ('sev_occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('sev_address', models.TextField(blank=True, null=True)),
                ('sev_details_confirmed_by', models.CharField(blank=True, max_length=100, null=True)),
                ('sev_relation_met_person_with_applicant', models.CharField(blank=True, max_length=100, null=True)),
                ('bv_company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('bv_business_address', models.TextField(blank=True, null=True)),
                ('bv_gstin_udyam_others_no', models.CharField(blank=True, max_length=100, null=True)),
                ('bv_num_of_employees', models.PositiveIntegerField(blank=True, null=True)),
                ('bv_landmark', models.CharField(blank=True, max_length=100, null=True)),
                ('bv_nature_of_business', models.CharField(blank=True, max_length=100, null=True)),
                ('bv_establishment_date', models.DateField(blank=True, null=True)),
                ('bv_designation_of_applicant', models.CharField(blank=True, max_length=100, null=True)),
                ('bv_met_person_at_business_place', models.BooleanField(blank=True, null=True)),
                ('bv_relation_met_person_with_applicant', models.CharField(blank=True, max_length=100, null=True)),
                ('bv_premises_is', models.BooleanField(blank=True, null=True)),
                ('bv_ownership_proof_type', models.CharField(blank=True, choices=[('E-Bill/Water Tax', 'E-Bill/Water Tax')], max_length=20, null=True)),
                ('bv_e_bill_or_water_tax_document', models.FileField(blank=True, null=True, upload_to='bv_e_bill_water_tax_documents/')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kapp.applicant')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
