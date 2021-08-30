# 管理画面の利用

## カスタムユーザーモデルを使用する

AbstractBaseUserが使いやすいので、継承して作成する。

```python　:　models.py
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
 
class UserManager(BaseUserManager):
 
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
```

* create_user(self, email, password=None):ユーザーがログインした場合、Emailをセットして、パスワードもセットするメソッド

* create_superuser(self, email, password=None):管理者権限のユーザーがログインした場合、使用するメソッド.

```python : models.py
class User(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
 
    is_active = models.BooleanField(default=True)
 
    is_admin = models.BooleanField(default=False)
 
    objects = UserManager()
 
    USERNAME_FIELD = 'email'
 
    REQUIRED_FIELDS = []
 
    def __str__(self):
        return self.email
 
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
 
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
```

Userクラスを定義している。
User名はEmailとし、パスワードも設定する。

## admin.pyの編集

* まずSettings.pyに`AUTH_USER_MODEL = 'mysite.User'`を追加し、Djangoの標準のユーザーではなく、作成したUserを使用することを明記する。

次に、admin.pyを以下のように編集する。

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from mysite.models import User

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields':(
                'email',
                'password',
            )
        }),
        (None, {
            'fields':(
                'is_active',
                'is_admin',
            )
        })
    )

    list_display = ('email', 'is_active')
    list_filter = ()
    ordering = ()
    filter_horizontal = ()

     # --- adminでuser作成用に追加 ---
    add_fieldsets = (
        (None, {
            'fields': ('email', 'password',),
        }),
    )
    # --- adminでuser作成用に追加 ---

admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
```

Adminに作成したUserを使用するため、CustomUserAdminクラスを作成する。

また、不要な項目として、Groupは表示されないように、`unregister(Group)`としておく。

## マイグレーション

## createsuperuserと管理画面

`python manage.py createsuperuser`で作成