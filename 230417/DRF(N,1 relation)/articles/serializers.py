from rest_framework import serializers
from .models import Article, Comment

# 1. 특정 게시글에 작성된 댓글 목록 출력하기
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__' 
        read_only_fields = ('article',)  # 읽기 전용 필드, 직렬화할때만 사용한다.

    
# class ArticleListSerializer(serializers.ModelSerializer):
#     # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # 1:N -> many=True
#     comment_set = CommentSerializer(many=True, read_only=True)  # CommentSerializer를 통한 직렬화 데이터를 넣어준다. 
#     class Meta:
#         model = Article
#         # fields = ('id', 'title', 'content',)
#         fields = '__all__'


# 2. 특정 게시글에 작성된 댓글의 개수 출력
class ArticleListSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True) # 1) 기본적으로 들어있는 역참조 매니저
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True) # 2) 
    
    class Meta:
        model = Article
        # fields = ('id', 'title', 'content',)
        fields = '__all__'
    
    # 필드명 수정 및 필요 없는 필드 삭제
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['comments'] = rep.pop('comment_set', [])  
        return rep
