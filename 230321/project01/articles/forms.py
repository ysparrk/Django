from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=30)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'  
        # Article model에 있는 field들 중에서 어떤 field를 대상으로 form을 만들 것인가

    # is_vaild 할때, django라는 키워드가 있는지 확인하고 싶다. -> 유효성 검사
    # def clean_title(self):
    #     title = self.cleaned_data['title'] # 데이터 가져오기
    #     if 'django' in title:
    #         return True

