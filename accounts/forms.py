#UserCreationFormクラスをインポート
from django.contrib.auth.forms import UserCreationForm
#model.pyで定義したカスタムUserモデルをインポート
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    '''UserCreationFormのサブクラス'''
    class Meta:
        '''UserCreationFormのインナークラス'''
        #連携するUserモデルを設定
        model=CustomUser
        #フォームで使用するフィールドを設定
        #ユーザ名、メールアドレス、パスワード、パスワード(確認用)
        fields=('username', 'email', 'password1', 'password2')

