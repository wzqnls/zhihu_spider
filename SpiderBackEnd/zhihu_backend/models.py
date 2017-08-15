from django.db import models


class Customer(models.Model):
    id = models.CharField(verbose_name="id", max_length=50, primary_key=True)
    name = models.CharField(verbose_name="姓名", max_length=50, null=True, blank=True)
    headline = models.CharField(verbose_name="个性签名", max_length=128, null=True)
    industry = models.CharField(verbose_name="行业", max_length=128, null=True)
    job_history = models.CharField(verbose_name="职业经历", max_length=128, null=True)
    education = models.CharField(verbose_name="教育经历", max_length=128, null=True)
    gender = models.IntegerField(verbose_name="性别", choices=((1, '男'), (0, '女')), default=1)
    url_token = models.CharField(verbose_name="token", max_length=50)
    url = models.CharField(verbose_name="用户api", max_length=256)
    avatar_url_template = models.CharField(verbose_name="头像url模板", max_length=128)
    answer_count = models.IntegerField(verbose_name="回答数", null=True)
    question_count = models.IntegerField(verbose_name="问题数", null=True)
    articles_count = models.IntegerField(verbose_name="文章数", null=True)
    special_column_count = models.IntegerField(verbose_name="专栏数", null=True)
    share_count = models.IntegerField(verbose_name="分享数", null=True)
    followed_count = models.IntegerField(verbose_name="关注者数", null=True)
    follower_count = models.IntegerField(verbose_name="关注数", null=True)
    approval_num = models.IntegerField(verbose_name="赞同数", null=True)
    thank_num = models.IntegerField(verbose_name="感谢数", null=True)
    collected_num = models.IntegerField(verbose_name="收藏数", null=True)
    follow_live_num = models.IntegerField(verbose_name="live", null=True)
    follow_special_column_num = models.IntegerField(verbose_name="关注专栏数", null=True)
    follow_question_num = models.IntegerField(verbose_name="关注问题数", null=True)
    follow_collection_num = models.IntegerField(verbose_name="关注收藏夹数", null=True)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Follow(models.Model):
    follower = models.ForeignKey(Customer, related_name="follower")
    followed = models.ForeignKey(Customer, related_name="followed")

