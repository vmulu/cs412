# convert our django data models to a text representation
# suitable to transmit over HTTP

from rest_framework import serializers
from .models import *

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'author',
            'text',
        ]

    # add methods to customize the CRUD operations

    def create(self, validated_data):
        """
        overide superclas method
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
        validated_data['user'] = User.objects.first()

        return Article.objects.create(**validated_data)