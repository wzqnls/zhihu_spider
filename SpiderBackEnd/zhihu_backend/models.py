from django.db import models


class Customer(models.Model):
    id = models.CharField(verbose_name="id", max_length=50, primary_key=True)
    name = models.CharField(verbose_name="姓名", max_length=50, null=True, blank=True)
    signature = models.CharField(verbose_name="个性签名", max_length=128, null=True, blank=True)
    # education = models.CharField(verbose_name="教育程度", max_length=128, null=True, blank=True)
    gender = models.IntegerField(verbose_name="性别", choices=((1, '男'), (0, '女')), default=1)
    pic_path = models.CharField(verbose_name="头像存储地址", max_length=256, null=True, blank=True)
    pic_url = models.CharField(verbose_name="头像url", max_length=256, null=True, blank=True)
    url = models.CharField(verbose_name="用户地址", max_length=256)
    follows = models.TextField(verbose_name="关注")
    followers = models.TextField(verbose_name="关注者")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
