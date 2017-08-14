from django.db import models


class Customer(models.Model):
    id = models.CharField(verbose_name="id", max_length=50, primary_key=True)
    name = models.CharField(verbose_name="姓名", max_length=50, null=True, blank=True)
    headline = models.CharField(verbose_name="个性签名", max_length=128, null=True)
    gender = models.IntegerField(verbose_name="性别", choices=((1, '男'), (0, '女')), default=1)
    url_token = models.CharField(verbose_name="token", max_length=50)
    # article_count = models.IntegerField()
    pic_path = models.CharField(verbose_name="头像存储地址", max_length=256, null=True)
    url = models.CharField(verbose_name="用户api", max_length=256)
    avatar_url_template = models.CharField(verbose_name="头像url模板", max_length=128)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Follow(models.Model):
    follower = models.ForeignKey(Customer, related_name="follower")
    followed = models.ForeignKey(Customer, related_name="followed")

