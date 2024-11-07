from rest_framework import serializers
from .models import PostProduct, ClassDay, TwoPictures, TenPictures


class ClassDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassDay
        fields = ['days']


class TwoPicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwoPictures
        fields = ['image']


class TenPicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenPictures
        fields = ['image']


class PostProductSerializer(serializers.ModelSerializer):
    class_days = ClassDaySerializer(many=True, required=False)
    two_pictures = TwoPicturesSerializer(many=True, required=False)
    ten_pictures = TenPicturesSerializer(many=True, required=False)

    class Meta:
        model = PostProduct
        fields = [
            'id', 'title', 'image', 'description', 'big_description',
            'duration', 'number_of_sessions', 'class_days', 'two_pictures', 'ten_pictures'
        ]

    def create(self, validated_data):
        class_days_data = validated_data.pop('class_days', [])
        two_pictures_data = validated_data.pop('two_pictures', [])
        ten_pictures_data = validated_data.pop('ten_pictures', [])

        product = PostProduct.objects.create(**validated_data)

        for day_data in class_days_data:
            ClassDay.objects.create(product=product, **day_data)

        for picture_data in two_pictures_data:
            TwoPictures.objects.create(product=product, **picture_data)

        for picture_data in ten_pictures_data:
            TenPictures.objects.create(product=product, **picture_data)

        return product

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.image = validated_data.get('image', instance.image)
        instance.description = validated_data.get('description', instance.description)
        instance.big_description = validated_data.get('big_description', instance.big_description)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.number_of_sessions = validated_data.get('number_of_sessions', instance.number_of_sessions)
        instance.save()

        class_days_data = validated_data.pop('class_days', [])
        instance.class_days.all().delete()
        for day_data in class_days_data:
            ClassDay.objects.create(product=instance, **day_data)

        two_pictures_data = validated_data.pop('two_pictures', [])
        instance.two_pictures.all().delete()
        for picture_data in two_pictures_data:
            TwoPictures.objects.create(product=instance, **picture_data)

        ten_pictures_data = validated_data.pop('ten_pictures', [])
        instance.ten_pictures.all().delete()
        for picture_data in ten_pictures_data:
            TenPictures.objects.create(product=instance, **picture_data)

        return instance
