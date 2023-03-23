from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        
        model = get_user_model()  # 현재 프로젝트에서 활성화 된 user 모델을 리턴한다.
        # fields = UserCreationForm.Meta.fields + ('email', )  # 추가로 받아오고 싶은 것들

class CustomUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm.Meta):  
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')





