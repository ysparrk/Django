# accounts/forms.py
# UCF을 그대로 사용할 것이다(상속-오버라이딩) class Meta의 model만 바꿔 줄 것.
# 상속의 상속 -> 내가 바꿀 model만 가져온다.


from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        # model이 accounts의 User를 보게 해 주면 된다
        model = get_user_model()  # settings.py의 AUTH_USER_MODEL를 가져온다/usermodel을 바꿔도 여기서 수정할 필요 없음


class CustomUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm.Meta):  
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')
    
