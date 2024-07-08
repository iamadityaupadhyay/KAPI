from .serializers import ApplicantSerializer, CoApplicantSerializer, GuarantorSerializer,ApplicantImageSerializer, CoApplicantImageSerializer, GuarantorImageSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import *
from rest_framework import generics
import json


@method_decorator(csrf_exempt, name='dispatch')
class VerifyMobileAPIView(APIView):
    def post(self, request):
        serializer = VerificationMobileSerializer(data=request.data)
        if serializer.is_valid():
            mobilenumber = serializer.validated_data['mobile_number']
            queryset = FieldUser.objects.filter(mobile_number=mobilenumber)
            if queryset.exists():
                user_serializer = FieldUserSerializer(queryset, many=True)
                return Response({
                    'detail': 'Verification successful. Login successful.',
                    'users': user_serializer.data
                }, status=status.HTTP_200_OK)
            return Response({'detail': 'Invalid mobile number'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUserProfileAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            user = get_object_or_404(FieldUser, pk=pk)
            serializer = FieldUserSerializer(user)
            return Response(serializer.data)
        else:
            user = request.user
            serializer = FieldUserSerializer(user)
            return Response(serializer.data)
@method_decorator(csrf_exempt, name='dispatch')
class UserProfileUpdateAPIView(generics.UpdateAPIView):
    queryset = FieldUser.objects.all()
    serializer_class = FieldUserSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        #Applicant
        if 'applicant_images' in request.FILES:
            applicant_images = request.FILES.getlist('applicant_images')
            applicant_instance =request.images.all().delete()
            for image in applicant_images:
                ApplicantImage.objects.create(applicant=applicant_instance, image=image)
        
            else:
                return Response(coapplicant_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

        #coapplicant
        if 'coapplicant' in request.data:
            coapplicant_data = request.data.get('coapplicant')
            for coapp_data in coapplicant_data:
                coapplicant_instance = CoApplicant.objects.get(id=coapp_data['id'])
                coapplicant_serializer = CoApplicantSerializer(coapplicant_instance, data=coapp_data, partial=partial)
                if coapplicant_serializer.is_valid():
                    coapplicant_serializer.save()
                    if 'coapplicant_images' in request.FILES:
                        coapplicant_images = request.FILES.getlist('coapplicant_images')
                        coapplicant_instance.images.all().delete()
                        for image in coapplicant_images:
                            CoApplicantImage.objects.create(coapplicant=coapplicant_instance, image=image)
                else:
                    return Response(coapplicant_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        #guarantor
        if 'guarantors' in request.data:
            guarantor_data = request.data.get('guarantors')
            for guar_data in guarantor_data:
                guarantor_instance = Guarantor.objects.get(id=guar_data['id'])
                guarantor_serializer = GuarantorSerializer(guarantor_instance, data=guar_data, partial=partial)
                if guarantor_serializer.is_valid():
                    guarantor_serializer.save()
                    if 'guarantor_images' in request.FILES:
                        guarantor_images = request.FILES.getlist('guarantor_images')
                        guarantor_instance.images.all().delete()
                        for image in guarantor_images:
                            GuarantorImage.objects.create(guarantor=guarantor_instance, image=image)
                else:
                    return Response(guarantor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data)



@method_decorator(csrf_exempt, name='dispatch')
class ApplicantSubmissionView(APIView):
    def post(self, request):
        json_string = request.data.get('request', '{}')
        try:
            data = json.loads(json_string)
        except json.JSONDecodeError:
            return Response({"error": "Invalid JSON format"}, status=status.HTTP_400_BAD_REQUEST)

        applicant_serializer = ApplicantSerializer(data=data)
        if applicant_serializer.is_valid():
            applicant = applicant_serializer.save()
            applicant_images = request.FILES.getlist('applicant_images')
            
            for image in applicant_images:
                ApplicantImage.objects.create(applicant=applicant, image=image)
            # Business Changes 
            applicant_images_business= request.FILES.getlist('applicant_images_business')
            for image in applicant_images_business:
                ApplicantImageBusiness.objects.create(applicant=applicant, image=image)
            
            coapplicant_data = data.get('coapplicant', [])
            serialized_coapplicants = []
            for coapp_data in coapplicant_data:
                coapp_data['applicant'] = applicant.id
                coapplicant_serializer = CoApplicantSerializer(data=coapp_data)
                if coapplicant_serializer.is_valid():
                    coapplicant = coapplicant_serializer.save()
                    serialized_coapplicants.append(coapplicant_serializer.data)
                    coapplicant_images = request.FILES.getlist('coapplicant_images')
                    for image in coapplicant_images:
                        CoApplicantImage.objects.create(coapplicant=coapplicant, image=image)
                    coapplicant_images_business = request.FILES.getlist('coapplicant_images_business')
                    # Business Changes
                    for image in coapplicant_images_business:
                        CoApplicantImageBusiness.objects.create(coapplicant=coapplicant, image=image)
                else:
                    return Response(coapplicant_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            guarantor_data = data.get('guarantor', [])
            serialized_guarantors = []
            for guar_data in guarantor_data:
                guar_data['applicant'] = applicant.id
                guarantor_serializer = GuarantorSerializer(data=guar_data)
                if guarantor_serializer.is_valid():
                    guarantor = guarantor_serializer.save()
                    serialized_guarantors.append(guarantor_serializer.data)
                    guarantor_images = request.FILES.getlist('guarantor_images')
                    for image in guarantor_images:
                        GuarantorImage.objects.create(guarantor=guarantor, image=image)
                    # Business changes
                    guarantor_images_business= request.FILES.getlist('guarantor_images_business')
                    for image in guarantor_images_business:
                        GuarantorImageBusiness.objects.create(guarantor=guarantor, image=image)
                else:
                    return Response(guarantor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            applicant.refresh_from_db() 
            serialized_applicant = ApplicantSerializer(applicant).data

            response_data = {
                "applicant": serialized_applicant
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(applicant_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class ApplicantListView(generics.ListAPIView):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)