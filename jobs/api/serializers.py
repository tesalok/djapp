from rest_framework import serializers
from jobs.models import JobOffer

class JobSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JobOffer
        fields='__all__'
        
    def validate_job_title(self, value):
        if len(value) < 10:
            raise serializers.ValidationError('Title must be atleast 10 characters long')
        return value    

    def validate(self, attrs):
        if attrs["job_title"] == attrs["job_description"]:
            raise serializers.ValidationError("Job Title and Job Description must be different")
        return attrs