from rest_framework import serializers
from .models import PostProduct, ClassDay



class ClassDaySerializer(serializers.ModelSerializer):
    """This serializer is used to represent Week days of the Class"""
    class Meta:
        model = ClassDay
        fields = ['days'] # Only the days field is exposed



class PostProductSerializer(serializers.ModelSerializer):
    """Serializer for Product model, which also handles nested ClassDay"""
    class_days = ClassDaySerializer(many=True, required=False)

    class Meta:
        model = PostProduct
        fields = ['id', 'title', 'image', 'description', 'duration', 'number_of_sessions', 'class_days']

        # ======== Custom create method to handle nested ClassDays during Product creation. ========
        def create(self, validated_data):
            class_days_data = validated_data.pop('class_days', [])
            product = PostProduct.objects.create(**validated_data)

            # ======== Create each ClassDay associated with the created Product.  ========
            for day in class_days_data:
                ClassDay.objects.create(product=product, **day)
            return product