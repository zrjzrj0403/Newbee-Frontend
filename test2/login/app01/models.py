from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField('姓名', max_length=32)
    pwd = models.CharField('密码', max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '管理员'


class User2(models.Model):
    user2_name = models.CharField('姓名', max_length=32)
    numc = models.IntegerField('完型数量')
    numr = models.IntegerField('阅读数量')
    numm = models.IntegerField('单选数量')

    def __str__(self):
        return self.user2_name

    class Meta:
        verbose_name_plural = '用户'
