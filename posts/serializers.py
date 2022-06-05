from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'post_id',
            'categoriya',
            'start_sanasi',
            'ozgartirilgan_sanasi'
        )