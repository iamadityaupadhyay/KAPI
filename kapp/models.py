# authentication/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class FieldUser(AbstractUser):
    mobile_number = models.CharField(max_length=15, unique=True)
    profile_photo = models.ImageField(
        upload_to='profile_photos/', null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    pin_code = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)


class Loan(models.Model):
    BANK_CHOICES = [
        ('Punjab & Sind', 'Punjab & Sind'),
        ('Bank of India', 'Bank of India'),
        ('Union Bank Of India', 'Union Bank Of India'),
        ('Canara Bank', 'Canara Bank'),
        ('SIDBI Bank', 'SIDBI Bank'),
        ('Bank Of Baroda', 'Bank Of Baroda'),
        ('Uco Bank', 'Uco Bank'),
    ]
    
    bank_name = models.CharField(max_length=100, choices=BANK_CHOICES)
    branch_name = models.CharField(max_length=100)
    loan_type = models.CharField(max_length=100)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)

    class Meta:
        abstract = True


class BaseApplicant(models.Model):

    # Residence Verification
    rv_bank_account = models.CharField(max_length=100, blank=True, null=True, verbose_name="Bank Account")
    rv_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Name")
    rv_contact_no = models.CharField(max_length=15, blank=True, null=True, verbose_name="Contact No")
    rv_aadhaar_no = models.CharField(max_length=12, blank=True, null=True, verbose_name="Aadhaar No")
    rv_pan_no = models.CharField(max_length=10, blank=True, null=True, verbose_name="PAN No")
    rv_present_address = models.TextField(blank=True, null=True, verbose_name="Present Address")
    rv_permanent_address = models.TextField(blank=True, null=True, verbose_name="Permanent Address")
    rv_premises_is = models.BooleanField(blank=True, null=True, verbose_name="Premises Is")
    rv_duration_to_stay = models.CharField(max_length=50, blank=True, null=True, verbose_name="Duration to Stay")
    rv_landmark = models.CharField(max_length=100, blank=True, null=True, verbose_name="Landmark")
    rv_OWNERSHIP_PROOF_CHOICES = (
        ('E-Bill/Water Tax', 'E-Bill/Water Tax'),
    )
    rv_ownership_proof_type = models.CharField(max_length=20, choices=rv_OWNERSHIP_PROOF_CHOICES, blank=True, null=True, verbose_name="Ownership Proof Type")
    rv_e_bill_or_water_tax_document = models.FileField(upload_to='rv_e_bill_water_tax_documents/', blank=True, null=True, verbose_name="E-Bill or Water Tax Document")
    rv_area_of_house = models.CharField(max_length=100, blank=True, null=True, verbose_name="Area of House")
    rv_color_of_house = models.CharField(max_length=50, blank=True, null=True, verbose_name="Color of House")
    rv_num_of_persons_living = models.PositiveIntegerField(blank=True, null=True, verbose_name="Number of Persons Living")
    rv_num_of_persons_earning = models.PositiveIntegerField(blank=True, null=True, verbose_name="Number of Persons Earning")
    rv_neighbour_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Neighbour Name")
    rv_neighbour_contact_no = models.CharField(max_length=15, blank=True, null=True, verbose_name="Neighbour Contact No")
    rv_met_person_at_home = models.BooleanField(blank=True, null=True, verbose_name="Met Person at Home")
    rv_relation_with_met_person = models.CharField(max_length=100, blank=True, null=True, verbose_name="Relation of Applicant/Co-Applicant/Guarantor with met person")
    rv_residency_status = models.CharField(max_length=50, blank=True, null=True, verbose_name="Residency Status")
    
    # Employment Verification
    ev_company_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Company Name")
    ev_company_address = models.TextField(blank=True, null=True, verbose_name="Company Address")
    ev_date_of_joining = models.DateField(blank=True, null=True, verbose_name="Date of Joining")
    ev_designation_of_applicant = models.CharField(max_length=100, blank=True, null=True, verbose_name="Designation of Applicant")
    ev_details_confirmed_by = models.CharField(max_length=100, blank=True, null=True, verbose_name="Details Confirmed By")
    ev_staff_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Staff Name")
    ev_staff_designation = models.CharField(max_length=100, blank=True, null=True, verbose_name="Staff Designation")
    ev_staff_contact_no = models.CharField(max_length=15, blank=True, null=True, verbose_name="Staff Contact No")

    # Self-employment/Profession Verification
    sev_occupation = models.CharField(max_length=100, blank=True, null=True, verbose_name="Occupation")
    sev_address = models.TextField(blank=True, null=True, verbose_name="Address")
    sev_details_confirmed_by = models.CharField(max_length=100, blank=True, null=True, verbose_name="Details Confirmed By")
    sev_relation_met_person_with_applicant = models.CharField(max_length=100, blank=True, null=True, verbose_name="Relation Met Person with Applicant")
    
    # Business Verification
    bv_company_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Company Name")
    bv_business_address = models.TextField(blank=True, null=True, verbose_name="Business Address")
    bv_gstin_udyam_others_no = models.CharField(max_length=100, blank=True, null=True, verbose_name="GSTIN/Udyam/Others No")
    bv_num_of_employees = models.PositiveIntegerField(blank=True, null=True, verbose_name="Number of Employees")
    bv_landmark = models.CharField(max_length=100, blank=True, null=True, verbose_name="Landmark")
    bv_nature_of_business = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nature of Business")
    bv_establishment_date = models.DateField(blank=True, null=True, verbose_name="Establishment Date")
    bv_designation_of_applicant = models.CharField(max_length=100, blank=True, null=True, verbose_name="Designation of Applicant")
    bv_met_person_at_business_place = models.BooleanField(blank=True, null=True, verbose_name="Met Person at Business Place")
    bv_relation_met_person_with_applicant = models.CharField(max_length=100, blank=True, null=True, verbose_name="Relation of Met Person with Applicant")
    bv_premises_is = models.BooleanField(blank=True, null=True, verbose_name="Premises Is")
    bv_OWNERSHIP_PROOF_CHOICES = (
        ('E-Bill/Water Tax', 'E-Bill/Water Tax'),
    )  
    bv_ownership_proof_type = models.CharField(max_length=20, choices=bv_OWNERSHIP_PROOF_CHOICES, blank=True, null=True, verbose_name="Ownership Proof Type")
    bv_e_bill_or_water_tax_document = models.FileField(upload_to='bv_e_bill_water_tax_documents/', blank=True, null=True, verbose_name="E-Bill or Water Tax Document")
    
    # Details which are in report but not in it
    rv_constitution_of_buisness = models.CharField(max_length=100, blank=True, null=True, verbose_name="Constitution of Business")
    rv_date_of_visit = models.DateField(blank=True, null=True, verbose_name="Date of Visit")

    class Meta:
        abstract = True


class Applicant(Loan, BaseApplicant):
    def __str__(self):
        return f"{self.rv_name}"
    class Meta:
        verbose_name = "Applicant"
        verbose_name_plural = "Applicants"

class CoApplicant(BaseApplicant):
    applicant = models.ForeignKey(Applicant, related_name='coapplicants', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.rv_name}"
    class Meta:
        verbose_name = "Co-Applicant"
        verbose_name_plural = "Co-Applicants"
    
class Guarantor(BaseApplicant):
    applicant = models.ForeignKey(Applicant, related_name='guarantors', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.rv_name}"
    class Meta:
        verbose_name = "Guarantor"
        verbose_name_plural = "Guarantors"


class ApplicantImage(models.Model):
    applicant = models.ForeignKey(Applicant, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='applicant_images/')
    class Meta:
        verbose_name = "Applicant Image"
        verbose_name_plural = "Applicant Images"

class CoApplicantImage(models.Model):
    coapplicant = models.ForeignKey(CoApplicant, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='coapplicant_images/')
    class Meta:
        verbose_name = "Co-Applicant Image"
        verbose_name_plural = "Co-Applicant Images"
class GuarantorImage(models.Model):
    guarantor = models.ForeignKey(Guarantor, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='guarantor_images/')
    class Meta:
        verbose_name = "Guarantor Image"
        verbose_name_plural = "Guarantor Images"
class CoApplicantImageBusiness(models.Model):
    coapplicant = models.ForeignKey(CoApplicant, related_name='businessimages', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='coapplicant_images_business/')
    class Meta:
        verbose_name = "Co-Applicant Business Image"
        verbose_name_plural = "Co-Applicant Business Images"
class GuarantorImageBusiness(models.Model):
    guarantor = models.ForeignKey(Guarantor, related_name='businessimages', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='guarantor_images_business/')
    class Meta:
        verbose_name = "Guarantor Business Image"
        verbose_name_plural = "Guarantor Business Images"
class ApplicantImageBusiness(models.Model):
    applicant = models.ForeignKey(Applicant, related_name='businessimages', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='applicant_images_business/')
    class Meta:
        verbose_name = "Applicant Business Image"
        verbose_name_plural = "Applicant Business Images"

    
class BackgroundVerification(models.Model):
    applicant = models.ForeignKey(Applicant, related_name='bg_verification', on_delete=models.CASCADE)
    change_in_affiliations=models.CharField(max_length=100, blank=True, null=True)
    year_of_establishment = models.CharField(max_length=100, blank=True, null=True)
    registration= models.CharField(max_length=100, blank=True, null=True)
    award_won = models.BooleanField(blank=True, null=True)
    any_change_in_reg_office = models.BooleanField(blank=True, null=True)
    class Meta:
        verbose_name = "Background Verification"
        verbose_name_plural = "Background Verifications"
class PersonalAssetsOfProprietor(models.Model):
    applicant = models.ForeignKey(Applicant, related_name='personal_assets', on_delete=models.CASCADE)
    name_personal_assets= models.CharField(max_length=100, blank=True, null=True)
    description_of_assets_owned= models.CharField(max_length=100, blank=True, null=True)
    amount_in_rs=models.CharField(max_length=100, blank=True, null=True)
    whether_any_security=models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        verbose_name = "Personal Asset of Proprietor"
        verbose_name_plural = "Personal Assets of Proprietors"
class Buyers(models.Model):
    applicant=models.ForeignKey(Applicant, related_name='buyers', on_delete=models.CASCADE)
    name_of_buyers=models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        verbose_name = "Buyer"
        verbose_name_plural = "Buyers"
class Suppliers(models.Model):
    applicant=models.ForeignKey(Applicant, related_name='suppliers', on_delete=models.CASCADE)
    name_of_suppliers=models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"
class DetailsOfAssociate(models.Model):
    applicant=models.ForeignKey(Applicant, related_name='details_of_associates', on_delete=models.CASCADE)
    slno=models.IntegerField(blank=True, null=True)
    name_of_buyers=models.CharField(max_length=100, blank=True, null=True)
    nature_of_activity=models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        verbose_name = "Detail of Associate"
        verbose_name_plural = "Details of Associates"

class InsuranceDetails(models.Model):
    applicant=models.ForeignKey(Applicant, related_name='insurance_details', on_delete=models.CASCADE)
    unit_assets=models.IntegerField( blank=True, null=True)
    policy_number=models.IntegerField( blank=True, null=True)
    validity=models.CharField(max_length=100, blank=True, null=True)
    sum_assured=models.IntegerField( blank=True, null=True)
    risk_covered=models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        verbose_name = "Insurance Detail"
        verbose_name_plural = "Insurance Details"
class ManufacturingEntities(models.Model):
    applicant=models.ForeignKey(Applicant, related_name='manufacturing_entities', on_delete=models.CASCADE)
    location_of_plot_accessibility_proximity_to_other_units=models.CharField(max_length=100,null=True,blank=True)
    principal_raw_materials_and_sources=models.CharField(max_length=100,null=True,blank=True)
    manufacturing_process=models.CharField(max_length=100,null=True,blank=True)
    major_branded_and_imported_machines_installed=models.CharField(max_length=100,null=True,blank=True)
    pollution_control=models.CharField(max_length=100,null=True,blank=True)
    power_connected_load_and_backup_availability=models.CharField(max_length=100,null=True,blank=True)
    inventory_wip_finished_goods_at_the_site=models.CharField(max_length=100,null=True,blank=True)
    storage_security_perishability_susceptibility_to_fire_and_weather=models.CharField(max_length=100,null=True,blank=True)
    quality_certification=models.CharField(max_length=100,null=True,blank=True)
    workers_split_of_temporary_and_permanent_any_unions=models.CharField(max_length=100,null=True,blank=True)
    
    history_of_any_strikes_any_child_labour_working_condition=models.CharField(max_length=100,null=True,blank=True)
    class Meta:
        verbose_name = "Manufacturing Entity"
        verbose_name_plural = "Manufacturing Entities"
class OtherParticulars(models.Model):
    applicant=models.ForeignKey(Applicant, related_name='other_particulars', on_delete=models.CASCADE)
    months_during_the_current_year=models.CharField(max_length=100,null=True,blank=True)
    purchases=models.CharField(max_length=100,null=True,blank=True)
    sales=models.CharField(max_length=100,null=True,blank=True)
    class Meta:
        verbose_name = "Other Particular"
        verbose_name_plural = "Other Particulars"
class BalanceSheetAndPLAccount(models.Model):
    
    applicant=models.ForeignKey(Applicant, related_name='balance_sheet', on_delete=models.CASCADE)
    year1=models.CharField(max_length=100,null=True,blank=True)
    net_income1 =models.IntegerField(null=True,blank=True)
    year2=models.CharField(max_length=100,null=True,blank=True)
    net_income2 =models.IntegerField(null=True,blank=True)
    year3=models.CharField(max_length=100,null=True,blank=True)
    net_income3 =models.IntegerField(null=True,blank=True)
    class Meta:
        verbose_name = "Balance Sheet and P&L Account"
        verbose_name_plural = "Balance Sheets and P&L Accounts"
class ItrVerification(models.Model):
    applicant=models.ForeignKey(Applicant, related_name='itr_verification', on_delete=models.CASCADE)
    year1 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Year 1")
    year2 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Year 2")
    year3 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Year 3")
    pan_y1 = models.CharField(max_length=100, null=True, blank=True, verbose_name="PAN Year 1")
    pan_y2 = models.CharField(max_length=100, null=True, blank=True, verbose_name="PAN Year 2")
    pan_y3 = models.CharField(max_length=100, null=True, blank=True, verbose_name="PAN Year 3")
    whether_itr_filler_properly_y1 = models.CharField(max_length=100, null=True, blank=True, verbose_name="ITR Filler Properly Year 1")
    whether_itr_filler_properly_y2 = models.CharField(max_length=100, null=True, blank=True, verbose_name="ITR Filler Properly Year 2")
    whether_itr_filler_properly_y3 = models.CharField(max_length=100, null=True, blank=True, verbose_name="ITR Filler Properly Year 3")
    date_of_itr_filling_y1 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Date of ITR Filing Year 1")
    date_of_itr_filling_y2 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Date of ITR Filing Year 2")
    date_of_itr_filling_y3 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Date of ITR Filing Year 3")
    acknowledgement_y1 = models.IntegerField(null=True, blank=True, verbose_name="Acknowledgement Year 1")
    acknowledgement_y2 = models.IntegerField(null=True, blank=True, verbose_name="Acknowledgement Year 2")
    acknowledgement_y3 = models.IntegerField(null=True, blank=True, verbose_name="Acknowledgement Year 3")
    total_gross_income_y1 = models.IntegerField(null=True, blank=True, verbose_name="Total Gross Income Year 1")
    total_gross_income_y2 = models.IntegerField(null=True, blank=True, verbose_name="Total Gross Income Year 2")
    total_gross_income_y3 = models.IntegerField(null=True, blank=True, verbose_name="Total Gross Income Year 3")
    total_taxable_income_y1 = models.IntegerField(null=True, blank=True, verbose_name="Total Taxable Income Year 1")
    total_taxable_income_y2 = models.IntegerField(null=True, blank=True, verbose_name="Total Taxable Income Year 2")
    total_taxable_income_y3 = models.IntegerField(null=True, blank=True, verbose_name="Total Taxable Income Year 3")
    class Meta:
        verbose_name = "ITR Verification"
        verbose_name_plural = "ITR Verifications"
class PropertiesProposed(models.Model):
    applicant=models.ForeignKey(Applicant, related_name='properties_proposed', on_delete=models.CASCADE)
    name_of_property_identifier =models.CharField(max_length=100,null=True,blank=True)
    name_of_property_1_owner=models.CharField(max_length=100,null=True,blank=True)
    name_of_property_2_or_3_owner =models.CharField(max_length=100,null=True,blank=True)
    address_property_1=models.CharField(max_length=100,null=True,blank=True)
    address_property_2_or_3=models.CharField(max_length=100,null=True,blank=True)
    date_of_visit= models.DateField(null=True,blank=True)
    whether_original_title_deeds=models.BooleanField(null=True,blank=True)
    types_of_documents=models.CharField(max_length=100,null=True,blank=True)
    class Meta:
        verbose_name = "Proposed Property"
        verbose_name_plural = "Proposed Properties"
class FinalConclusion(models.Model):
    applicant=models.ForeignKey(Applicant, related_name='final_conclusion', on_delete=models.CASCADE)
    financial=models.CharField(max_length=200,null=True,blank=True)
    address=models.CharField(max_length=200,null=True,blank=True)
    identity=models.CharField(max_length=200,null=True,blank=True)
    class Meta:
        verbose_name = "Final Conclusion"
        verbose_name_plural = "Final Conclusions"
class AdharImagesOfCoApplicant(models.Model):
    coapplicant=models.ForeignKey(CoApplicant, related_name='adhar_images', on_delete=models.CASCADE)
    adhar_images = models.ImageField(upload_to='adhar_images/', null=True, blank=True)
    def __str__(self):
        return f"Adhar Image for {self.coapplicant}"
    class Meta:
        verbose_name = "Aadhar Image"
        verbose_name_plural = "Aadhar Images"
class AdharImagesOfGuarantor(models.Model):
    guarantor=models.ForeignKey(Guarantor, related_name='adhar_images', on_delete=models.CASCADE)
    adhar_images = models.ImageField(upload_to='adhar_images/', null=True, blank=True)
    def __str__(self):
        return f"Adhar Image for {self.guarantor}"
    class Meta:
        verbose_name = "Aadhar Image"
        verbose_name_plural = "Aadhar Images"
class AdharImagesOfApplicant(models.Model):
    
    applicant=models.ForeignKey(Applicant, related_name='adhar_images', on_delete=models.CASCADE)
    adhar_images = models.ImageField(upload_to='adhar_images/', null=True, blank=True)
    def __str__(self):
        return f"Adhar Image for {self.applicant}"
    class Meta:
        verbose_name = "Aadhar Image"
        verbose_name_plural = "Aadhar Images"
                
class PanImagesOfApplicant(models.Model):
    applicant = models.ForeignKey(Applicant, related_name='pan_images', on_delete=models.CASCADE)
    pan_images = models.ImageField(upload_to='pan_images/', null=True, blank=True)  
    def __str__(self):
        return f"PAN Image for {self.applicant}"
    class Meta:
        verbose_name = "PAN Image"
        verbose_name_plural = "PAN Images"

class PanImagesOfCoApplicant(models.Model):
    coapplicant = models.ForeignKey(CoApplicant, related_name='pan_images', on_delete=models.CASCADE)
    pan_images = models.ImageField(upload_to='pan_images/', null=True, blank=True)  
    def __str__(self):
        return f"PAN Image for {self.coapplicant}"
    class Meta:
        verbose_name = "PAN Image"
        verbose_name_plural = "PAN Images"

class PanImagesOfGuarantor(models.Model):
    guarantor = models.ForeignKey(Guarantor, related_name='pan_images', on_delete=models.CASCADE)
    pan_images = models.ImageField(upload_to='pan_images/', null=True, blank=True)  
    def __str__(self):
        return f"PAN Image for {self.guarantor}"
    class Meta:
        verbose_name = "PAN Image"
        verbose_name_plural = "PAN Images"
        

class GstImagesOfApplicant(models.Model):
    applicant=models.ForeignKey(Applicant, related_name='gst_images', on_delete=models.CASCADE)
    gst_images=models.ImageField(upload_to='gst_images/', null=True, blank=True)  
    def __str__(self):
        return f"GST Image for {self.applicant}"
    class Meta:
        verbose_name = "GST Image"
        verbose_name_plural = "GST Images"
class GstImagesOfCoApplicant(models.Model):
    coapplicant=models.ForeignKey(CoApplicant, related_name='gst_images', on_delete=models.CASCADE)
    gst_images=models.ImageField(upload_to='gst_images/', null=True, blank=True)  
    def __str__(self):
        return f"GST Image for {self.coapplicant}"
    class Meta:
        verbose_name = "GST Image"
        verbose_name_plural = "GST Images"
class GstImagesOfGuarantor(models.Model):
    guarantor=models.ForeignKey(Guarantor, related_name='gst_images', on_delete=models.CASCADE)
    gst_images=models.ImageField(upload_to='gst_images/', null=True, blank=True)  
    def __str__(self):
        return f"GST Image for {self.guarantor}"
    class Meta:
        verbose_name = "GST Image"
        verbose_name_plural = "GST Images"
    