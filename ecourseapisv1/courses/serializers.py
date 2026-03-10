from courses.models import Category, Course, Lesson
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.image:
            data['image'] = instance.image.url
        return data

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CourseSerializer(ItemSerializer):
    class Meta:
        model = Course
        fields = ['id','subject','description', 'created_date', 'image']

class LessonSerializer(ItemSerializer):
    class Meta:
        model = Lesson
        fields = ['id','subject','image']