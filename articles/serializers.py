from rest_framework import serializers
from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'headline', 'image_url', 'author', 'slug', 'pub_date', 'date_modified']
