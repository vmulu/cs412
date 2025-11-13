#
from rest_framework import serializers
from .models import *

class JokeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Joke
        fields = [
            'text',
            'name',
        ]

    # def create(self, validated_data):
    #     """
    #     override superclass method
    #     """

    #     # print(f'validated_data={validated_data}')

    #     # # create article object
    #     # article = Article(**validated_data)

    #     # # attach fk for the User
    #     # article.user = User.objects.first()

    #     # # save the object to database
    #     # article.save()

    #     # return article

    #     # simpler way
    #     validated_data['joke'] = Joke.objects.first()

    #     return Joke.objects.create(**validated_data)

class PictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Picture
        fields = [
            'image_url',
            'name',
        ]

    def create(self, validated_data):
        """
        override superclass method
        """

        # print(f'validated_data={validated_data}')

        # # create article object
        # article = Article(**validated_data)

        # # attach fk for the User
        # article.user = User.objects.first()

        # # save the object to database
        # article.save()

        # return article

        # simpler way
        validated_data['picture'] = Picture.objects.first()

        return Picture.objects.create(**validated_data)
