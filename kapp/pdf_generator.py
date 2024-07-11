import os
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer,Image
from reportlab.lib import colors
from reportlab.lib.units import cm 
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from .models import *
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# For Images
def get_image_paths(queryset, base_path):
        image_paths=[os.path.join(base_path, image.image.name) for image in queryset]
        return image_paths if image_paths else None

def get_image_paths_adhar(queryset, base_path):
    return [os.path.join(base_path, str(instance.adhar_images)) for instance in queryset if instance.adhar_images]
def get_image_paths_pan(queryset, base_path):
    return [os.path.join(base_path, str(instance.pan_images)) for instance in queryset if instance.pan_images]
def get_image_paths_gst(queryset, base_path):
    return [os.path.join(base_path, str(instance.gst_images)) for instance in queryset if instance.gst_images]

import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

def add_images(elements, image_paths, title, styles):
    if image_paths:
        elements.append(Paragraph(title, styles['Heading2']))
        
        # Set smaller max dimensions for images
        max_width, max_height = A4[0] / 2, A4[1] / 4

        for img_path in image_paths:
            try:
                img = Image(img_path)
                img.drawWidth, img.drawHeight = adjust_image_size(img, max_width, max_height)
                logging.info(f"Image size for {img_path}: {img.drawWidth} x {img.drawHeight}")
                elements.append(img)
            except Exception as e:
                logging.error(f"Error processing image {img_path}: {e}")
def adjust_image_size(img, max_width, max_height):
    original_width, original_height = img.drawWidth, img.drawHeight
    aspect_ratio = original_width / float(original_height)

    if original_width > max_width:
        img.drawWidth = max_width
        img.drawHeight = max_width / aspect_ratio

    if img.drawHeight > max_height:
        img.drawHeight = max_height
        img.drawWidth = max_height * aspect_ratio

    # Final check to ensure dimensions are within bounds
    img.drawWidth = min(img.drawWidth, max_width)
    img.drawHeight = min(img.drawHeight, max_height)

    return img.drawWidth, img.drawHeight

# Example usage:
# elements = []
# image_paths = ['path/to/image1.jpg', 'path/to
# Business Images

def generate_combined_report(applicant_id):
    base_path="media/"
    applicant = Applicant.objects.get(id=applicant_id)
    co_applicant = CoApplicant.objects.filter(applicant=applicant).first()
    guarantor = Guarantor.objects.filter(applicant=applicant).first()
    bg_verification = BackgroundVerification.objects.filter(applicant=applicant).first()
    personal_assets=PersonalAssetsOfProprietor.objects.filter(applicant=applicant).first()
    buyers=Buyers.objects.filter(applicant=applicant).all()
    suppliers=Suppliers.objects.filter(applicant=applicant).all()
    final_conclusion=FinalConclusion.objects.filter(applicant=applicant).first()
   
    try :
       applicant_images = get_image_paths(ApplicantImage.objects.filter(applicant=applicant), base_path)

    except :
        applicant_images=None
    try:
        coapplicant_images = get_image_paths(CoApplicantImage.objects.filter(coapplicant=co_applicant), base_path)

    except :
        coapplicant_images = None
    try:
        guarantor_images = get_image_paths(GuarantorImage.objects.filter(guarantor=guarantor), base_path).first()
    except:
        guarantor_images = None
    # Images Of Applicant
    try:
        adhar_images_applicant = get_image_paths_adhar(AdharImagesOfApplicant.objects.filter(applicant=applicant), base_path)

    except:
        adhar_images_applicant = None
    try:
        pan_images_applicant = get_image_paths_pan(PanImagesOfApplicant.objects.filter(applicant=applicant), base_path)
    except:
        pan_images_applicant = None
    try:
        gst_images_applicant = get_image_paths_gst(GstImagesOfApplicant.objects.filter(applicant=applicant), base_path)
    except:
        gst_images_applicant = None
    
    # Images of CoApplicant
    try:
        adhar_images_coapplicant = get_image_paths_adhar(AdharImagesOfCoApplicant.objects.filter(co_applicant=co_applicant), base_path)
    except:
        adhar_images_coapplicant = None
    try:
        pan_images_coapplicant = get_image_paths_pan(PanImagesOfCoApplicant.objects.filter(co_applicant=co_applicant), base_path)
    except:
        pan_images_coapplicant = None
    try:
        gst_images_coapplicant = get_image_paths_gst(GstImagesOfCoApplicant.objects.filter(co_applicant=co_applicant), base_path)
    except:
        gst_images_coapplicant = None
    
    try:
        adhar_images_guarantor = get_image_paths_adhar(AdharImagesOfGuarantor.objects.filter(guarantor=guarantor), base_path)

    except:
        adhar_images_guarantor = None
    try:
        pan_images_guarantor = get_image_paths_pan(PanImagesOfGuarantor.objects.filter(guarantor=guarantor), base_path)
    except:
        pan_images_guarantor = None
    try:
        gst_images_guarantor = get_image_paths_gst(GstImagesOfGuarantor.objects.filter(guarantor=guarantor), base_path)
    except:
        gst_images_guarantor = None
        
    try :
       applicant_images_business = get_image_paths(ApplicantImageBusiness.objects.filter(applicant=applicant), base_path)
    
    except :
        applicant_images_business=None
    try:
        coapplicant_images_business = get_image_paths(CoApplicantImageBusiness.objects.filter(coapplicant=co_applicant), base_path)
        
    except :
        coapplicant_images_business = None
    try:
        guarantor_images_business = get_image_paths(GuarantorImageBusiness.objects.filter(guarantor=guarantor), base_path)
    except:
        guarantor_images_business = None
        
    details_of_associate=DetailsOfAssociate.objects.filter(applicant=applicant).all()
    insurance_details =InsuranceDetails.objects.filter(applicant=applicant).first()
    manufacturing_entities=ManufacturingEntities.objects.filter(applicant=applicant).first()
    properties_proposed=PropertiesProposed.objects.filter(applicant=applicant).first()
    other_particular =OtherParticulars.objects.filter(applicant=applicant).all()
    itr_verification=ItrVerification.objects.filter(applicant=applicant).first()
    balance_sheet =BalanceSheetAndPLAccount.objects.filter(applicant=applicant).first()
    
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="applicant_{applicant_id}_report.pdf"'
    doc = SimpleDocTemplate(response, pagesize=A4)
    elements = []
     
    styles = getSampleStyleSheet()
    styleH = styles['Heading2']
    styleN = styles['Normal']

    #starting
    width, height = A4
    styles = getSampleStyleSheet()

  
  #logo
    centered_style = ParagraphStyle(name='centered', alignment=1, fontSize=12)
    centered_title_style = ParagraphStyle(name='centered_title', alignment=1, fontSize=15, spaceAfter=12, fontName='Helvetica-Bold')

    ca_india_logo_path = "kapp/header_image/ca_logo.png" 
    second_page_header = "kapp/header_image/Screenshot 2024-07-07 155933.png" 
    elements.append(Image(second_page_header, width=500, height=80))
    elements.append(Spacer(1, 15))

    elements.append(Image(ca_india_logo_path, width=120, height=100))
    elements.append(Spacer(1, 20))
    elements.append(Paragraph("<u>Komandoor & Co. LLP</u>", centered_title_style))
    elements.append(Spacer(1, 20))
    elements.append(Paragraph("<u>Chartered Accountants </u>", centered_title_style))
    elements.append(Spacer(1, 20))
    elements.append(Paragraph("<u>Customer Point Verification</u>", centered_title_style))
    elements.append(Spacer(1, 20))
    
    
    elements.append(Paragraph(f"<u>Applicant: {applicant.rv_name}</u>", centered_style))
    elements.append(Spacer(1, 3))
    elements.append(Paragraph(f"<u>CoApplicant: {co_applicant.rv_name if co_applicant else 'N/A'}</u>", centered_style))
    elements.append(Spacer(1, 3))
    elements.append(Paragraph(f"<u>Guarantor:{guarantor.rv_name if guarantor else 'N/A'}</u>", centered_style))
    elements.append(Spacer(1, 3))
    elements.append(Spacer(1, 20))

    # Bank Report
    elements.append(Paragraph(f"Report to {applicant.bank_name} - {applicant.branch_name}", styles['Normal']))
    elements.append(Spacer(1, 20))

    # Office Address
    elements.append(Paragraph("Office Address: Second Floor, B-43, Techno Tower, Gomti Nagar, CGST and Central", styles['Normal']))
    elements.append(Paragraph("Excise Colony, Vibhuti Khand, Lucknow, U.P-226010.", styles['Normal']))
    elements.append(Spacer(1, 40))

    # Confidential Note
    elements.append(Paragraph("<b>Private & Confidential</b>", styles['Normal']))
    elements.append(Spacer(1, 20))

    # Footer
    footer_text = (
        "Address: Second Floor, B-43, Techno Tower (CGST And Central Excise Colony), Vibhuti Khand, Gomti Nagar LUCKNOW - 226010 U.P.<br/>"
        "Ph.No. 9540778658, 8375849755 & 8299793833<br/>"
        "E-Mail: lucknow@komandoorco.com & manojalsinghkomandoor@gmail.com<br/>"
        "Head office : Flat No. 1-504, Divya Shakti Complex, 7-1-58, Dharma Karan Road, Ameerpet, Hyderabad - 500016<br/>"
        "Ph.No. +91 7207075799 E-Mail: komandoorco@gmail.com & info@komandoorco.com<br/>"
        "BRANCHES: New Delhi, Mumbai, Kolkata, Chennai, Agra, Ahmedabad, Bangalore, Bhubaneshwar, Bhopal, Chandigarh, Coimbatore<br/>"
        "Guwahati, Gurugram, Jaipur, Kohima (Nagaland), Lucknow, Kanpur, NaharLagun (Itanagar)-Arunachal Pradesh<br/>"
        "Patna, Pune, Ranchi, Raipur, Tirupathi, Thiruvananthapuram, Vijayawada and Vishakhapatnam"
    )
    elements.append(Paragraph(footer_text, styles['Normal']))
    elements.append(Spacer(1, 40))
#Starting
    
    elements.append(Image(second_page_header, width=500, height=80))
    elements.append(Spacer(1, 15))

    header = [
        Paragraph("To,", styles['Normal']),
        Paragraph("Branch Manager, Punjab & Sind Bank", styles['Normal']),
        Paragraph("Kailash Colony Branch", styles['Normal']),
        Paragraph("Delhi.", styles['Normal']),
        Spacer(1, 0.2 * inch),
        Paragraph("Subject: DUE DILIGENCE REPORT OF M/S. S R SOLUTIONS (GST EASE LOAN OF RS. 2.5 CRORES)", styles['Normal']),
        Spacer(1, 0.2 * inch),
        Paragraph("Dear Sir/Madam,", styles['Normal']),
        Spacer(1, 0.2 * inch),
        Paragraph("As per Information Provided By bank, we have conducted Due Diligence of the captioned account. We submit here with Due Diligence Report of the same for your kind perusal and record.", styles['Normal']),
        Spacer(1, 0.5 * inch),
    ]

    
    elements.extend(header)

    # Table data
    data = [
        ['Particulars', 'Summary of Findings'],
        ['Identity verification', final_conclusion.identity if final_conclusion else "N/A"],
        ['Address verification', final_conclusion.address if final_conclusion else "N/A"],
        ['Financial verification',final_conclusion.financial if final_conclusion else "N/A"]
    ]

    
    table = Table(data, colWidths=[4*cm,13*cm])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  
        ('VALIGN', (1, 1), (1, -1), 'TOP'), 
        ('WRAP', (1, 1), (1, -1), 1), 
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
    ]))
    elements.append(Spacer(1, 20))
    elements.append(Spacer(2, 20))
 
    elements.append(table)
    elements.append(Spacer(1, 20))
    elements.append(Spacer(2, 20))
    elements.append(Spacer(3, 20))
    elements.append(Spacer(1, 20))
    elements.append(Spacer(2, 20))
    elements.append(Spacer(3, 20))
    elements.append(Spacer(1, 20))
    elements.append(Spacer(2, 20))
    elements.append(Spacer(3, 20))
    elements.append(Spacer(1, 20))
    elements.append(Spacer(3, 20))
    elements.append(Spacer(1, 20))
    title = Paragraph("DUE DILIGENCE REPORT FOR MSME PROPOSALS", centered_title_style)
    elements.append(title)
    elements.append(Spacer(1, 0.5 * cm))
    header_data = [
        
        ["Date of Visit", applicant.rv_date_of_visit],
       
        ["Persons Met",applicant.bv_met_person_at_business_place],
        
        ["Amount of loan", f"Rs {applicant.loan_amount}"],
    ]
    header_table = Table(header_data, colWidths=[6 * cm, 10 * cm])

    header_table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ]))
    elements.append(header_table)
    elements.append(Spacer(1, 0.5 * cm))
#Starting2
    data_table = [
        ["Name", "Designation", "Years of Business"],
        
        [applicant.rv_name, "Applicant",f"Since {applicant.rv_duration_to_stay}" ],
        [co_applicant.rv_name if co_applicant else 'N/A', "Co-Applicant",f"Since {co_applicant.rv_duration_to_stay}" if co_applicant else 'N/A'],
        [guarantor.rv_name if guarantor else 'N/A', "Guarantor", f"Since{guarantor.rv_duration_to_stay}" if guarantor else 'N/A']
    ]
    data_table_style = Table(data_table, colWidths=[6 * cm, 5 * cm])
    data_table_style.setStyle(TableStyle([
      ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ]))
    elements.append(data_table_style)
    elements.append(Spacer(1, 0.5 * cm))
#Borrower Data
    # title = Paragraph("1.BORROWER'S DETAILS", styleN)
    # elements.append(title)
    # elements.append(Spacer(1, 0.5 * cm))
    borrower_data = [
        ["1.BORROWER'S DETAILS",""],
        ["Applicant’s Name", applicant.rv_name if applicant else "N/A"],
        ["Present Address", applicant.rv_present_address if applicant else "N/A"],
        ["Premises Status", applicant.rv_premises_is if applicant else "N/A"],
        ["Duration of Stay", f"Since {applicant.rv_duration_to_stay}" if applicant else "N/A" ],
        ["Area of House",applicant.rv_area_of_house if applicant else "N/A" ],
        ["Color of House",applicant.rv_color_of_house if applicant else "N/A" ],
        ["No of Person Living",applicant.rv_num_of_persons_living if applicant else "N/A" ],
        ["No of Person Earning",applicant.rv_num_of_persons_earning if applicant else "N/A" ],
        ["Neighbour Name",applicant.rv_neighbour_name if applicant else "N/A" ],
        ["Neighbour Contact",applicant.rv_neighbour_contact_no if applicant else "N/A" ],
        ["Met Person at home",applicant.rv_met_person_at_home if applicant else "N/A" ],
        ["Relation of Applicant with met person ",applicant.rv_relation_with_met_person if applicant else "N/A" ],
        ["Telephone (Residence/Office)", applicant.rv_contact_no if applicant else "N/A"],
        ["Business Electricity No", applicant.rv_e_bill_or_water_tax_document if applicant else "N/A"],
        ["Other site(s) of the borrower/ site(s)", applicant.rv_landmark if applicant else "N/A"],
        ["Trade License/UDYAM/GSTIN", applicant.bv_gstin_udyam_others_no if applicant else "N/A" ],
        ["Constitution of the Business",applicant.rv_constitution_of_buisness if applicant else "N/A"],
        
        ["Informations of Co-Applicant \nand Guarantor",""],
        
        ["Name of the Co-Applicant", co_applicant.rv_name if co_applicant else "N/A"],
        ["Parmanent Address of Co-Applicant",co_applicant.rv_permanent_address if co_applicant else "N/A" ],
        ["Present Address of Co-Applicant",co_applicant.rv_present_address if co_applicant else "N/A" ],
        ["Aadhar No of Co-Applicant", co_applicant.rv_aadhaar_no if co_applicant else "N/A" ],
        ["Pan No of Co-Applicant", co_applicant.rv_pan_no if co_applicant else "N/A" ],
        ["Premises Status", co_applicant.rv_premises_is if co_applicant else "N/A" ],
        ["Duration of Stay", f"Since {co_applicant.rv_duration_to_stay}" if co_applicant else "N/A" ],
        ["Area of House",co_applicant.rv_area_of_house if co_applicant else "N/A" ],
        ["Color of House",co_applicant.rv_color_of_house if co_applicant else "N/A" ],
        ["No of Person Living",co_applicant.rv_num_of_persons_living if co_applicant else "N/A" ],
        ["No of Person Earning",co_applicant.rv_num_of_persons_earning if co_applicant else "N/A" ],
        ["Neighbour Name",co_applicant.rv_neighbour_name if co_applicant else "N/A" ],
        ["Neighbour Contact",co_applicant.rv_neighbour_contact_no if co_applicant else "N/A" ],
        ["Met Person at home",co_applicant.rv_met_person_at_home if co_applicant else "N/A" ],
        ["Relation of Co-Applicant\n with met person ",co_applicant.rv_relation_with_met_person if co_applicant else "N/A" ],
        
        
   
 
        # Guarantor
        ["Name of Guarantor", guarantor.rv_name if guarantor else 'N/A'],
        ["Address of Guarantor", guarantor.rv_permanent_address if guarantor else "N/A"],
        ["Aadhar No of Guarantor", guarantor.rv_aadhaar_no if guarantor else 'N/A'],
        ["Pan No of Guarantor", guarantor.rv_pan_no if guarantor else 'N/A'],
        ["Premises Status", guarantor.rv_premises_is if guarantor else "N/A" ],
        ["Duration of Stay", f"Since {guarantor.rv_duration_to_stay}" if guarantor else "N/A" ],
        ["Area of House",guarantor.rv_area_of_house if guarantor else "N/A" ],
        ["Color of House",guarantor.rv_color_of_house if guarantor else "N/A" ],
        ["No of Person Living",guarantor.rv_num_of_persons_living if guarantor else "N/A" ],
        ["No of Person Earning",guarantor.rv_num_of_persons_earning if guarantor else "N/A" ],
        ["Neighbour Name",guarantor.rv_neighbour_name if guarantor else "N/A" ],
        ["Neighbour Contact",guarantor.rv_neighbour_contact_no if guarantor else "N/A" ],
        ["Met Person at home",guarantor.rv_met_person_at_home if guarantor else "N/A" ],
        ["Relation of Co-Applicant\n with met person ",guarantor.rv_relation_with_met_person if guarantor else "N/A" ],
    
        
    ]
    borrower_table = Table(borrower_data, colWidths=[6 * cm, 10 * cm])
    borrower_table.setStyle(TableStyle([
      ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ]))
    elements.append(borrower_table)
    elements.append(Spacer(1, 0.5 * cm))
    
#Background Verfication
    # title = Paragraph("2.BACKGROUND VERIFICATION", styleN)
    # elements.append(title)
    # elements.append(Spacer(1, 0.5 * cm))
    ev_verification_applicant=[
    ["Employment Verification\n of Applicant",""],
        ["Company Name", applicant.ev_company_name if applicant else "N/A" ],
        ["Company Address", applicant.ev_company_address if applicant else "N/A" ],
        ["Date of Joining", applicant.ev_date_of_joining if applicant else "N/A" ],
        ["Designation", applicant.ev_designation_of_applicant if applicant else "N/A" ],
        ["Staff Name ", applicant.ev_staff_name if applicant else "N/A" ],
        ["Designation of Staff ", applicant.ev_staff_designation if applicant else "N/A"],
        ["Contact No of Staff", applicant.ev_staff_contact_no if applicant else "N/A"],]
    table = Table(ev_verification_applicant, colWidths=[6 * cm, 10 * cm])
    table.setStyle(TableStyle([
         ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),]))
    elements.append(table)
    elements.append(Spacer(1, 0.5 * cm))
    ev_verification_co_applicant=[
    ["Employment Verification\n of Co-Applicant",""],
        ["Company Name", co_applicant.ev_company_name if co_applicant else "N/A" ],
        ["Company Address", co_applicant.ev_company_address if co_applicant else "N/A" ],
        ["Date of Joining", co_applicant.ev_date_of_joining if co_applicant else "N/A" ],
        ["Designation", co_applicant.ev_designation_of_applicant if co_applicant else "N/A" ],
        ["Staff Name ", co_applicant.ev_staff_name if co_applicant else "N/A" ],
        ["Designation of Staff ", co_applicant.ev_staff_designation if co_applicant else "N/A"],
        ["Contact No of Staff", co_applicant.ev_staff_contact_no if co_applicant else "N/A"],]
    table = Table(ev_verification_co_applicant, colWidths=[6 * cm, 10 * cm])
    table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ]))

    elements.append(table)
    elements.append(Spacer(1, 0.5 * cm))
    ev_verification_guarantor=[
    ["Employment Verification\n of Guarantor",""],
        ["Company Name", guarantor.ev_company_name if guarantor  else "N/A" ],
        ["Company Address", guarantor.ev_company_address if guarantor  else "N/A" ],
        ["Date of Joining", guarantor.ev_date_of_joining if guarantor else "N/A" ],
        ["Designation", guarantor.ev_designation_of_applicant if guarantor  else "N/A" ],
        ["Staff Name ", guarantor.ev_staff_name if guarantor  else "N/A" ],
        ["Designation of Staff ", guarantor.ev_staff_designation if guarantor  else "N/A"],
        ["Contact No of Staff", guarantor.ev_staff_contact_no if guarantor  else "N/A"],]
    table = Table(ev_verification_guarantor, colWidths=[6 * cm, 10 * cm])
    table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 0.5 * cm))
    table=[
        ["Self Employement \nVerification of Applicant",""],
        ["Occupation",applicant.sev_occupation if applicant else "N/A"],
        ["Address",applicant.sev_address if applicant else "N/A"],
        ["Details Confirmed By",applicant.sev_details_confirmed_by if applicant else "N/A"],
        ["Relation of Applicant",applicant.sev_relation_met_person_with_applicant if applicant else "N/A"],
    ]
    table = Table(table, colWidths=[6 * cm, 10 * cm])
    table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 0.5 * cm))
    table=[
        ["Self Employement \nVerification of Co-Applicant",""],
        ["Occupation",co_applicant.sev_occupation if co_applicant else "N/A"],
        ["Address",co_applicant.sev_address if co_applicant else "N/A"],
        ["Details Confirmed By",co_applicant.sev_details_confirmed_by if co_applicant else "N/A"],
        ["Relation of Applicant",co_applicant.sev_relation_met_person_with_applicant if co_applicant else "N/A"],
    ]
    table = Table(table, colWidths=[6 * cm, 10 * cm])
    table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 0.5 * cm))
    table=[
        ["Self Employement\n Verification of Guarantor",""],
        ["Occupation",guarantor .sev_occupation if guarantor else "N/A"],
        ["Address",guarantor .sev_address if guarantor  else "N/A"],
        ["Details Confirmed By",guarantor .sev_details_confirmed_by if guarantor  else "N/A"],
        ["Relation of Applicant",guarantor .sev_relation_met_person_with_applicant if guarantor  else "N/A"],
    ]
    table = Table(table, colWidths=[6 * cm, 10 * cm])
    table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 0.5 * cm))
    
    bg_verification = [
    ["2.BACKGROUND VERIFICATION",""],
    ["Year of Establishment",bg_verification.year_of_establishment  if bg_verification else "N/A" ],  
    ["Registrations/Affiliations\n(Any GST is at L-79, Jaitpur Extension,\nBadarpur, South Delhi, Delhi, 110044.)", bg_verification.registration if bg_verification else "N/A"],  
    ["Change in promoters' \nregistrations/affiliations", bg_verification.change_in_affiliations if bg_verification else "N/A"],
    ["Any Awards won", bg_verification.award_won if bg_verification else "N/A"],
    ["Any change in Registered Office", bg_verification.any_change_in_reg_office if bg_verification else "N/A"],
]
    table = Table(bg_verification, colWidths=[6 * cm, 10 * cm])
    table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ]))
    
    elements.append(table)
    elements.append(Spacer(1, 0.5 * cm))
    
    #3. PERSONAL ASSETS OF THE PROPRIETOR / PARTNERS / DIRECTORS
    title = Paragraph("3. PERSONAL ASSETS OF THE PROPRIETOR / PARTNERS / DIRECTORS", styleN)
    elements.append(title)
    elements.append(Spacer(1, 0.5 * cm))
    data =[
        ["3. PERSONAL ASSETS",""],
        ["Name", personal_assets.name_personal_assets if personal_assets else "N/A"],  
    ["Description of the Assets \n owned by them.", personal_assets.description_of_assets_owned if personal_assets else "N/A"],  
    ["Amount (Rs. in lakh)", personal_assets.amount_in_rs if personal_assets else "N/A"],
    ["Whether offered as Security", personal_assets.whether_any_security if personal_assets else "N/A"],
    ]
    table = Table(data, colWidths=[6 * cm, 10 * cm])
    table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ]))
 
    elements.append(table)
    elements.append(Spacer(1, 0.5 * cm))
    
    title = Paragraph("4.NAME OF BUYERS", styleN)
    elements.append(title)
    elements.append(Spacer(1, 0.5 * cm))
    data=[
        ["SL.No","Name of Buyers"],
        ]
    if buyers:
      for idx, buyer in enumerate(buyers, start=1):
        data.append([idx, buyer.name_of_buyers])
        
    
    table = Table(data, colWidths=[6 * cm, 10 * cm])
    table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ]))
 
    elements.append(table)
    elements.append(Spacer(1, 0.5 * cm))
    title = Paragraph("5.DETAILS OF SUPPLIERS", styleN)
    elements.append(title)
    elements.append(Spacer(1, 0.5 * cm))
    data=[
        ["SL.NO","Details Of Suppliers"],
          ]
    if suppliers:
      for idx, supplier in enumerate(suppliers, start=1):
        data.append([idx, supplier.name_of_suppliers])
    table = Table(data, colWidths=[2* cm, 14 * cm])
    table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ]))

    elements.append(table)
    elements.append(Spacer(1, 0.5 * cm))
    # 6.DETAILS OF ASSOCIATE / GROUP CONCERNS 
    title = Paragraph("6.DETAILS OF ASSOCIATE / GROUP CONCERNS ", styleN)
    elements.append(title)
    elements.append(Spacer(1, 0.5 * cm))
    
    data_table = [
        ["Sl.No.", " Name of the Associate \n/Group Concerns ", "Nature of Activity"],
    ]
    if details_of_associate:
     for idx, details in enumerate(details_of_associate, start=1):
        data_table.append([idx, details.name_of_buyers , details.nature_of_activity])
    data_table_style = Table(data_table, colWidths=[2 * cm, 8 * cm,6*cm])
    data_table_style.setStyle(TableStyle([
      ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ]))
    elements.append(data_table_style)
    elements.append(Spacer(1, 0.5 * cm))
    # 7. INSURANCE DETAILS
    title = Paragraph("7.INSURANCE DETAILS ", styleN)
    elements.append(title)
    elements.append(Spacer(1, 0.5 * cm))
    data_table = [
       ["Unit’s \nAssets covered ","Policy No./CoverNote", "Validity", "Sum Assured", "Risk Covered"],  
    ]
    if insurance_details:
        data_table.append([insurance_details.unit_assets,insurance_details.policy_number,insurance_details.validity,insurance_details.sum_assured,insurance_details.risk_covered])
    
    data_table_style = Table(data_table, colWidths=[3*cm,4*cm,3*cm,3* cm,3*cm])
    data_table_style.setStyle(TableStyle([
      ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ]))
    elements.append(data_table_style)
    elements.append(Spacer(1, 0.5 * cm))
    # 8. ACIVITY LEVELS AT THE TIME OF VISIT 
    title = Paragraph("8.ACIVITY LEVELS AT THE TIME OF VISIT ", styleN)
    elements.append(title)
    elements.append(Spacer(1, 0.5 * cm))
    data_table = [
        ["Number of Employees observed", applicant.bv_num_of_employees if applicant else "N/A"],
        ["Level of Activity \n (description of production / \n Delivery / Customers)","Production"]
       
    ]
    data_table_style = Table(data_table, colWidths=[8 * cm, 8 * cm])
    data_table_style.setStyle(TableStyle([
      ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ]))
    elements.append(data_table_style)
    elements.append(Spacer(1, 0.5 * cm))
   
   # 9. FOR MANUFACTURING ENTITIES / FACTORY SITE (S) 
    title = Paragraph("9.FOR MANUFACTURING ENTITIES / FACTORY SITE (S)", styleN)
    elements.append(title)
    elements.append(Spacer(1, 0.5 * cm))
    data_table = [
        ["Location of Plot, accessibility,\n proximity to other units", manufacturing_entities.location_of_plot_accessibility_proximity_to_other_units if manufacturing_entities else "N/A"],
        ["Principal raw material(s) \nand sources", manufacturing_entities.principal_raw_materials_and_sources if manufacturing_entities else "N/A"],
        ["Manufacturing Process", manufacturing_entities.manufacturing_process if manufacturing_entities else "N/A"],
        ["Major branded and \nimported machines, installed", manufacturing_entities.major_branded_and_imported_machines_installed if manufacturing_entities else "N/A"],
        ["Pollution Control: Any pollutants\n being generated and their \ndisposal. Permission obtained from\n Pollution Control Board.", manufacturing_entities.pollution_control if manufacturing_entities else "N/A"],
        ["Power: Connected load and back up availability", manufacturing_entities.power_connected_load_and_backup_availability if manufacturing_entities else "N/A"],
        ["Inventory / WIP / Finished Goods at the site", manufacturing_entities.inventory_wip_finished_goods_at_the_site if manufacturing_entities else "N/A"],
        ["Storage / Security / \nPerishability / Susceptibility\n to fire and weather", ""],
        ["Quality Certification", manufacturing_entities.quality_certification if manufacturing_entities else "N/A"],
        ["Workers / Split of Temporary\n and permanent / any unions", manufacturing_entities.workers_split_of_temporary_and_permanent_any_unions if manufacturing_entities else "N/A"],
        ["History of any strikes \n/ any child labour /\n working conditions", manufacturing_entities.history_of_any_strikes_any_child_labour_working_condition if manufacturing_entities else "N/A"]
    ]   
    data_table_style = Table(data_table, colWidths=[8 * cm, 8 * cm])
    data_table_style.setStyle(TableStyle([
      ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ]))
    elements.append(data_table_style)
    elements.append(Spacer(1, 0.5 * cm))

    # 10. OTHER PARTICULARS
    title = Paragraph("10. OTHER PARTICULARS", styleN)
    elements.append(title)
    elements.append(Spacer(1, 0.5 * cm))
    data_table = [
        
        ["Months(during the current year)", "Purchases", "Sales"],
        
          ]
    if other_particular:
     for month, other in enumerate(other_particular, start=1):
        data_table.append([month, other.purchases, other.sales])
        
    data_table_style = Table(data_table, colWidths=[6 * cm,5*cm, 5 * cm])
    data_table_style.setStyle(TableStyle([
      ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ]))
    elements.append(data_table_style)
    elements.append(Spacer(1, 0.5 * cm)) 
    # 11.  FIGURES OF THE BALANCE SHEET & P/L ACCOUNT
    title = Paragraph("11.FIGURES OF THE BALANCE SHEET & P/L ACCOUNT", styleN)
    elements.append(title)
    elements.append(Spacer(1, 0.5 * cm))
    data_table = [
        ["Name of the Applicant", " Year ", " Net Income "],
        [applicant.rv_name if applicant else "N/A",balance_sheet.year1 if balance_sheet else "N/A",balance_sheet.net_income1 if balance_sheet else "N/A"],
        [applicant.rv_name if applicant else "N/A",balance_sheet.year2 if balance_sheet else "N/A",balance_sheet.net_income2 if balance_sheet else "N/A"],
        [applicant.rv_name if applicant else "N/A",balance_sheet.year3 if balance_sheet else "N/A",balance_sheet.net_income3 if balance_sheet else "N/A"],   
    ]
    
    data_table_style = Table(data_table, colWidths=[6 * cm,5*cm, 5 * cm])
    data_table_style.setStyle(TableStyle([
      ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ]))
    elements.append(data_table_style)
    elements.append(Spacer(1, 0.5 * cm)) 
    if applicant.rv_name:
        name=applicant.rv_name.upper()
    else :
        name="N/A"
    #  12. LATEST ITR VERIFICATION REPORT OF: MR. ROHIT KUMAR SINH 
    title = Paragraph(f"12. LATEST ITR VERIFICATION REPORT OF:{name} ", styleN)
    elements.append(title)
    elements.append(Spacer(1, 0.5 * cm))
    data_table =[
        ["Particulars", itr_verification.year1 if itr_verification else "N/A", itr_verification.year2 if itr_verification else "N/A", itr_verification.year2 if itr_verification else "N/A"],
        ["Pan No", itr_verification.pan_y1 if itr_verification else "N/A",itr_verification.pan_y2 if itr_verification else "N/A",itr_verification.pan_y3 if itr_verification else "N/A"],
        ["Acknowledgement No.", itr_verification.acknowledgement_y1 if itr_verification else "N/A", itr_verification.acknowledgement_y2 if itr_verification else "N/A", itr_verification.acknowledgement_y3 if itr_verification else "N/A"],
        ["Whether ITR Filled Properly", itr_verification.whether_itr_filler_properly_y1 if itr_verification else "N/A", itr_verification.whether_itr_filler_properly_y2 if itr_verification else "N/A", itr_verification.whether_itr_filler_properly_y3 if itr_verification else "N/A"],
        ["Date Of Filling", itr_verification.date_of_itr_filling_y1 if itr_verification else "N/A", itr_verification.date_of_itr_filling_y2 if itr_verification else "N/A", itr_verification.date_of_itr_filling_y3 if itr_verification else "N/A"],
        ["Total Gross Income", itr_verification.total_gross_income_y1 if itr_verification else "N/A", itr_verification.total_gross_income_y2 if itr_verification else "N/A",itr_verification.total_gross_income_y3 if itr_verification else "N/A"],
        ["Total Taxable Income", itr_verification.total_taxable_income_y1 if itr_verification else "N/A", itr_verification.total_taxable_income_y2 if itr_verification else "N/A", itr_verification.total_taxable_income_y3 if itr_verification else "N/A"],

    ]
    data_table_style = Table(data_table, colWidths=[5 * cm,4 * cm,4*cm,3*cm])
    data_table_style.setStyle(TableStyle([
      ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ]))
   
    elements.append(data_table_style)
    elements.append(Spacer(1, 0.5 * cm)) 

    # 13. LATEST ITR VERIFICATION REPORT OF: MRS. VIDYA DEVI 
    # if co_applicant:
    #         title = Paragraph(f"13. LATEST ITR VERIFICATION REPORT OF:{(co_applicant.rv_name)}", styleN)
    # else : title = Paragraph(f"13. LATEST ITR VERIFICATION REPORT OF:N/A", styleN)
        
    # elements.append(title)
    # elements.append(Spacer(1, 0.5 * cm))
    # data_table =[
    #     ["Particulars", "","",""],
    #     ["Pan No", "", "", ""],
    #     ["Acknowledgement No.", "", "", ""],
    #     ["Whether Pan Is Valid", "", "", ""],
    #     ["Whether ITR Filled Properly", "", "", ""],
    #     ["Date Of Filling", "", "", ""],
    #     ["Total Gross Income", "", "", ""],
    #     ["Total Taxable Income", "", "", ""],
    #     ["Status", "", "", ""]
    # ]
    # data_table_style = Table(data_table, colWidths=[5 * cm,4 * cm,4*cm,3*cm])
    # data_table_style.setStyle(TableStyle([
    #   ('GRID', (0, 0), (-1, -1), 1, colors.black),
    #     ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
    #     ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
    #     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    #     ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    #     ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    # ]))
    # elements.append(data_table_style)
    # elements.append(Spacer(1, 0.5 * cm)) 
    
    # 14. PROPERTIES PROPOSED TO BE MORTGAGE 
    title = Paragraph(" 14.PROPERTIES PROPOSED TO BE MORTGAGE ", styleN)
    elements.append(title)
    elements.append(Spacer(1, 0.5 * cm))
    data_table = [
            ["A", "Name of the person,\n who has identified the property",properties_proposed.name_of_property_identifier if properties_proposed else "N/A"],
            ["B", "Name Of Property-1 Owner", properties_proposed.name_of_property_1_owner if properties_proposed else "N/A" ],
            ["B.1", "Name Of Property-2 & 3 Owner", properties_proposed.name_of_property_2_or_3_owner if properties_proposed else "N/A"],
            ["C", "Address of Property-1", properties_proposed.address_property_1 if properties_proposed else "N/A"],
            ["D", "Address of Property-2", properties_proposed.address_property_2_or_3 if properties_proposed else "N/A"],
            ["E", "Date of visit", applicant.rv_date_of_visit if applicant else "N/A"],
            ["F", "Whether original Title Deeds/\n Tax Receipt Received", properties_proposed.whether_original_title_deeds if properties_proposed else "N/A"],
            ["G", "Type of Documents", properties_proposed.types_of_documents if properties_proposed else "N/A"]
        ]
    data_table_style = Table(data_table, colWidths=[2*cm, 7 * cm, 7 * cm])
    data_table_style.setStyle(TableStyle([
      ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ]))
    elements.append(data_table_style)
    elements.append(Spacer(1, 0.5 * cm))
    

    data_table = [
            ["15. DETAILS OF BANK ACCOUNT OF APPLICANT",""],
            [ "Name of Applicant", applicant.rv_name if applicant else "N/A"],
            [ "Bank A/C No.", applicant.rv_bank_account],
            [ "Name of the Bank", applicant.bank_name],
            [ "Remark if Any", ""],  
        ]
    data_table_style = Table(data_table, colWidths=[9 * cm, 7 * cm])
    data_table_style.setStyle(TableStyle([
      ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ]))
    elements.append(data_table_style)
    elements.append(Spacer(1, 0.5 * cm))
    

    data_table = [
            ["16. DETAILS OF BANK ACCOUNT OF GUARANTOR",""],
            ["Name of Guarantor", guarantor.rv_name if guarantor else "N/A"],
            ["Bank A/C No.", guarantor.rv_bank_account if guarantor else "N/A"],
 
        ]
    data_table_style = Table(data_table, colWidths=[9 * cm, 7 * cm])
    data_table_style.setStyle(TableStyle([
      ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ]))
    elements.append(data_table_style)
    elements.append(Spacer(1, 0.5 * cm))
    data_table = [
            ["17. DETAILS OF BANK ACCOUNT OF COAPPLICANT",""],
            ["Name of Guarantor", co_applicant.rv_name if co_applicant else "N/A"],
            ["Bank A/C No.", co_applicant.rv_bank_account if co_applicant else "N/A"],
            
 
        ]
    data_table_style = Table(data_table, colWidths=[9 * cm, 7 * cm])
    data_table_style.setStyle(TableStyle([
      ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ]))
    elements.append(data_table_style)
    elements.append(Spacer(1, 1))


    # Adding images
    add_images(elements, applicant_images, "Applicant Images", styles)
    elements.append(Spacer(1, 1))
    add_images(elements, coapplicant_images, "Coapplicant Images", styles)
    elements.append(Spacer(1, 1))
    add_images(elements, guarantor_images, "Guarantor Images", styles)
    elements.append(Spacer(1, 1))
    add_images(elements, guarantor_images_business, "<u>Guarantor Business Verification Images</u>", styles)
    elements.append(Spacer(1, 1))
    add_images(elements, coapplicant_images_business, "<u>Co-Applicant Business Verification Images</u>", styles)
    elements.append(Spacer(1, 1))
    add_images(elements, applicant_images_business, "<u>Applicant Business Verification Images</u>", styles)
    elements.append(Spacer(1, 1))
    add_images(elements, adhar_images_applicant, "Aadhar Images of Applicant", styles)
    elements.append(Spacer(1, 1))
    add_images(elements, adhar_images_coapplicant, "Aadhar Images of Co-Applicant", styles)
    elements.append(Spacer(1, 1))
    add_images(elements, adhar_images_guarantor, "Aadhar Images of Guarantor", styles)
    elements.append(Spacer(1, 1))

    add_images(elements, pan_images_applicant, "Pan Images of Applicant", styles)
    elements.append(Spacer(1,1))
    add_images(elements, pan_images_coapplicant, "Pan Images of Co-Applicant", styles)
    elements.append(Spacer(1, 1))
    add_images(elements, pan_images_guarantor, "Pan Images of Guarantor", styles)
    elements.append(Spacer(1, 1))
  
    add_images(elements, gst_images_applicant, "GST Images of Applicant", styles)
    elements.append(Spacer(1, 1))
    add_images(elements, gst_images_coapplicant, "GST Images of CoApplicant", styles)
    elements.append(Spacer(1, 1))
    add_images(elements, gst_images_guarantor, "GST Images of Guarantor", styles)
    doc.build(elements)
    return response
