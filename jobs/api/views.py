from jobs.models import JobOffer
from rest_framework import status
from jobs.api.serializers import JobSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

class JobsListCreateAPIView(APIView):
    
    def get(self, request):
        jobs =  JobOffer.objects.filter(available=True)
        # jobs =  JobOffer.objects.all
        serializer = JobSerializer(jobs,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = JobSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class JobsDetailCreateAPIView(APIView):
    
    def get_object(self,pk):
        jobs = get_object_or_404(JobOffer,pk=pk)
        try:           
             return jobs
        except jobs.DoesNoxtExist():
             return Http404
        
    
    def get(self,request,pk):
        jobs = self.get_object(pk)
        serializer =  JobSerializer(jobs)
        return Response(serializer.data)
    
    def put(self, request, pk):
        jobs = self.get_object(pk)
        serializer = JobSerializer(jobs,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        jobs = self.get_object(pk);
        jobs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    # ===============================================================
    
# @api_view(["GET","PUT","DELETE"])
# def jobs_detail_api_view(request,pk):
#     try:
#         jobs = JobOffer.objects.get(pk=pk)
#     except JobOffer.DoesNotExist:
#         return Response({"errro":{
#                     "code":404,
#                     "message":"Job not found!"
#                      }},status =status.HTTP_404_NOT_FOUND
#                 )

#     if request.method == "GET":
#          serializer = JobSerializer(jobs)  
#          return Response(serializer.data)
#     elif request.method =="PUT":
#         serializer = JobSerializer(jobs,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         jobs.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)