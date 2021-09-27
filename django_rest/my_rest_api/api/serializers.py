from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Student


## Validator
def roll_should_positive(value):
    if value <= 0:
        raise serializers.ValidationError("Negative Roll Number")


class StudentSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    name  = serializers.CharField(max_length=100)
    # roll = serializers.IntegerField()
    roll = serializers.IntegerField(validators=[roll_should_positive])
    city = serializers.CharField(max_length=100)

    def create(self,validated_data):
        return Student.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance


    ## Field level validation
    # This method gets automatically called when is_valid() method is called
    def validate_roll(self,value):
        if value <= 1:
            raise serializers.ValidationError("Invalid roll number")
        return value
    
    ## object level validation
    ### if we want validate multiple fields
    def validate(self, data):
        name = data.get('name')
        roll = data.get('roll')
        city = data.get('city')

        if roll <=1:    
            raise serializers.ValidationError("Invalid roll number")

        if name is None or city is None:
            raise serializers.ValidationError("Invalid data")
        
        return data




## Model Serializer

class StudentModelSerializer(serializers.ModelSerializer):
    
    def validate_roll(self,value):
        if value <= 1:
            raise serializers.ValidationError("Invalid roll number")
        return value
    
    class Meta:
        model = Student
        fields = '__all__'
        # exclude = ["city"]

    