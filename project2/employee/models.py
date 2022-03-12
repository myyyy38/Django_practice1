from django.db import models
from django.utils import timezone
# Create your models here.

class Department(models.Model):
    name = models.CharField('部署名',max_length=20)
    created_at = models.DateTimeField('日付',default=timezone.now)

    #管理画面で、一覧に表示するものの設定
    def __str__(self):
        return self.name

class Club(models.Model):
    name = models.CharField('部活名',max_length=20)
    created_at = models.DateTimeField('日付',default=timezone.now)

    #管理画面で、一覧に表示するものの設定
    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField('名',max_length=20)
    last_name = models.CharField('姓',max_length=20)
    email = models.EmailField('メールアドレス',blank=True)
    #foreignKey 1対多のリレーション(1部署に対して複数人) 
    #on_delete = models.PROTECT on_deleteで削除時の挙動、
    # models.PROTECTは、親に属する子がいるときには削除不可のモード
    # models.CASCADEは、親に属する子がいるときに子ごと削除
    department = models.ForeignKey(
        Department, verbose_name ='部署',on_delete = models.PROTECT,
    )
    club = models.ManyToManyField(
        Club, verbose_name= '部活'
    )
    #OneToOneField　1部署一人に指定したいとき

    created_at = models.DateTimeField('日付',default=timezone.now)

    def __str__(self):
        return f'{self.last_name},{self.first_name},{self.department}'
