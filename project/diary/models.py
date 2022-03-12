from statistics import mode
from django.db import models #djangoからimportしたmodelsのModelクラスを継承
from django.utils import timezone #datetime.nowの代わりにこれ
# Create your models here.

class Day(models.Model):
    # id = models.AutoField(primary_key=True)を内部で自動処理、これによりidが取得できる（自分で主キーを設定しなかったとき）
    #CharField 1行で終わりそうなときに
    title = models.CharField('タイトル',max_length = 200)
    text = models.TextField('本文')
    date = models.DateTimeField('日付',default=timezone.now)

    def __str__(self):
        return self.title

