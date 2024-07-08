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

class ApplicantAdmin(admin.ModelAdmin):
    inlines = [ApplicantImageInline]
    list_display = ['rv_name', 'rv_contact_no', 'rv_aadhaar_no', 'rv_pan_no']
    actions = ['generate_pdf_report']

    def generate_pdf_report(self, request, queryset):
        if queryset.count() == 1:
            applicant = queryset.first()
            return generate_combined_report(applicant.id)
        else:
            self.message_user(
                request, "Please select exactly one applicant to generate a PDF report.", level='error')

    generate_pdf_report.short_description = "Generate combined PDF report for selected applicant"

class CoApplicantAdmin(admin.ModelAdmin):
    inlines = [CoApplicantImageInline]

class GuarantorAdmin(admin.ModelAdmin):
    inlines = [GuarantorImageInline]
admin.site.register(FieldUser)
admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(CoApplicant,CoApplicantAdmin)
admin.site.register(Guarantor,GuarantorAdmin)
admin.site.register(BackgroundVerification)
admin.site.register(PersonalAssetsOfProprietor)
admin.site.register(InsuranceDetails)
admin.site.register(Buyers)
admin.site.register(Suppliers)
admin.site.register(DetailsOfAssociate)
admin.site.register(ManufacturingEntities)
admin.site.register(OtherParticulars)
admin.site.register(BalanceSheetAndPLAccount)

admin.site.register(ItrVerification)
admin.site.register(PropertiesProposed)
admin.site.register(FinalConclusion)
admin.site.register(ApplicantImageBusiness)
admin.site.register(CoApplicantImageBusiness)
admin.site.register(GuarantorImageBusiness)
admin.site.register(AdharImages)
admin.site.register(PanImages)
admin.site.register(GstImages)