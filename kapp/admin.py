# authentication/admin.py
from django.contrib import admin
from .models import *
from .pdf_generator import generate_combined_report





# admin.site.register(Guarantor)
# admin.site.register(CoApplicantImage)
# admin.site.register(GuarantorImage)

# Adding images also in the same form of coapplicant , guarantor 
from django.contrib import admin
from .models import CoApplicant, Guarantor, CoApplicantImage, GuarantorImage

class CoApplicantImageInline(admin.TabularInline):
    model = CoApplicantImage
    extra = 1 

class GuarantorImageInline(admin.TabularInline):
    model = GuarantorImage
    extra = 1  
    
class ApplicantImageInline(admin.TabularInline):
    model = ApplicantImage
    extra=1
class AdharImagesOfApplicantInline(admin.TabularInline):
    model = AdharImagesOfApplicant
    extra = 1

class AdharImagesOfCoApplicantInline(admin.TabularInline):
    model = AdharImagesOfCoApplicant
    extra = 1

class AdharImagesOfGuarantorInline(admin.TabularInline):
    model = AdharImagesOfGuarantor
    extra = 1

class PanImagesOfApplicantInline(admin.TabularInline):
    model = PanImagesOfApplicant
    extra = 1

class PanImagesOfCoApplicantInline(admin.TabularInline):
    model = PanImagesOfCoApplicant
    extra = 1

class PanImagesOfGuarantorInline(admin.TabularInline):
    model = PanImagesOfGuarantor
    extra = 1

class GstImagesOfApplicantInline(admin.TabularInline):
    model = GstImagesOfApplicant
    extra = 1

class GstImagesOfCoApplicantInline(admin.TabularInline):
    model = GstImagesOfCoApplicant
    extra = 1

class GstImagesOfGuarantorInline(admin.TabularInline):
    model = GstImagesOfGuarantor
    extra = 1

class ApplicantImageBusinessInline(admin.TabularInline):
    model = ApplicantImageBusiness
    extra = 1
class CoApplicantImageBusinessInline(admin.TabularInline):
    model = CoApplicantImageBusiness
    extra = 1
class GuarantorImageBusinessInline(admin.TabularInline):
    model = GuarantorImageBusiness
    extra = 1
class InsuranceDetailsInline(admin.TabularInline):
    model = InsuranceDetails
    extra = 1

class BalanceSheetAndPLAccountInline(admin.TabularInline):
    model = BalanceSheetAndPLAccount
    extra = 1
class BackgroundVerificationInline(admin.TabularInline):
    model = BackgroundVerification
    extra = 1
class ItrVerificationInline(admin.TabularInline):
    model = ItrVerification
    extra = 1
class ApplicantAdmin(admin.ModelAdmin):
    inlines = [
        ApplicantImageInline,
        AdharImagesOfApplicantInline,
        PanImagesOfApplicantInline,
        GstImagesOfApplicantInline,
        ItrVerificationInline,
        ApplicantImageBusinessInline,
        InsuranceDetailsInline,
        BalanceSheetAndPLAccountInline
    ]
    list_display = ['rv_name', 'rv_contact_no', 'rv_aadhaar_no', 'rv_pan_no']
    actions = ['generate_pdf_report']
    search_fields=["rv_name"]

    def generate_pdf_report(self, request, queryset):
        if queryset.count() == 1:
            applicant = queryset.first()
            return generate_combined_report(applicant.id)
        else:
            self.message_user(
                request, "Please select exactly one applicant to generate a PDF report.", level='error')

    generate_pdf_report.short_description = "Generate combined PDF report for selected applicant"

class CoApplicantAdmin(admin.ModelAdmin):
    inlines = [
        CoApplicantImageInline,
        AdharImagesOfCoApplicantInline,
        PanImagesOfCoApplicantInline,
        GstImagesOfCoApplicantInline,
        CoApplicantImageBusinessInline,
    ]

class GuarantorAdmin(admin.ModelAdmin):
    inlines = [
        GuarantorImageInline,
        AdharImagesOfGuarantorInline,
        PanImagesOfGuarantorInline,
        GstImagesOfGuarantorInline,
        GuarantorImageBusinessInline,
    ]
    
# Registering
admin.site.register(FieldUser)
admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(CoApplicant,CoApplicantAdmin)
admin.site.register(Guarantor,GuarantorAdmin)
admin.site.register(PersonalAssetsOfProprietor)
admin.site.register(Buyers)
admin.site.register(Suppliers)
admin.site.register(DetailsOfAssociate)
admin.site.register(ManufacturingEntities)
admin.site.register(OtherParticulars)

admin.site.register(PropertiesProposed)
admin.site.register(FinalConclusion)




    