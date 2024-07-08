from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
# from .models import FieldUser, Applicant, CoApplicant, Guarantor,ApplicantImage, CoApplicantImage, GuarantorImage
from .models import *

class VerificationMobileSerializer(serializers.Serializer):
    mobile_number = serializers.CharField(max_length=15)


class FieldUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'mobile_number',
                  'profile_photo', 'address', 'pin_code', 'city', 'state']

    profile_photo = serializers.ImageField(
        required=False)

    def update(self, instance, validated_data):
        validated_data.pop('profile_photo', None)

        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.mobile_number = validated_data.get(
            'mobile_number', instance.mobile_number)
        instance.address = validated_data.get('address', instance.address)
        instance.pin_code = validated_data.get('pin_code', instance.pin_code)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)

        instance.save()
        return instance


class ApplicantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantImage
        fields = ['id', 'image']
class AdharImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdharImages
        fields = ['id', 'image']
class PanImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PanImages
        fields = ['id', 'image']
class GstImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GstImages
        fields = ['id', 'image']
class CoApplicantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoApplicantImage
        fields = ['id', 'image']


class GuarantorImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuarantorImage
        fields = ['id', 'image']

# Business Serializer#
class GuarantorImageBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuarantorImageBusiness
        fields = ['id', 'businessimage']
class ApplicantImageBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantImageBusiness
        fields = ['id', 'businessimage']
class CoApplicantImageBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoApplicantImageBusiness
        fields = ['id', 'businessimage']

class CoApplicantSerializer(serializers.ModelSerializer):
    images = CoApplicantImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = CoApplicant
        fields = '__all__'

class GuarantorSerializer(serializers.ModelSerializer):
    images = GuarantorImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Guarantor
        fields = '__all__'

class ApplicantSerializer(serializers.ModelSerializer):
    coapplicants = CoApplicantSerializer(many=True, read_only=True)
    guarantors = GuarantorSerializer(many=True, read_only=True)
    images = ApplicantImageSerializer(many=True, read_only=True)

    class Meta:
        model = Applicant
        fields = '__all__'
        
class BackgroundVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model:BackgroundVerification
        fields='__all__'

class PersonalAssetsOfProprietorSerializer(serializers.ModelSerializer):
    class Meta:
        model:PersonalAssetsOfProprietor
        fields='__all__'
    
class BuyersSerializer(serializers.ModelSerializer):
    class Meta:
        model:PersonalAssetsOfProprietor
        fields='__all__'
   
class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model:PersonalAssetsOfProprietor
        fields='__all__'
 
class DetailsOfAssociateSerializer(serializers.ModelSerializer):
    class Meta:
        model:DetailsOfAssociate
        fields='__all__'
    
class InsuranceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model:InsuranceDetails
        fields='__all__'
   
class ManufacturingEntitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model:ManufacturingEntities
        fields='__all__'
   
class OtherParticularsSerializer(serializers.ModelSerializer):
    class Meta:
        model:OtherParticulars
        fields='__all__'
    
class BalanceSheetAndPLAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model:BalanceSheetAndPLAccount
        fields='__all__'
    
class ItrVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model:ItrVerification
        fields='__all__'
    
class PropertiesProposedSerializer(serializers.ModelSerializer):
    class Meta:
        model:PropertiesProposed
        fields='__all__'
