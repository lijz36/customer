from django.db import models
import datetime


# 声明标题模型类
class Title(models.Model):
    name = models.CharField(max_length=100, verbose_name='网站标题', null=True)
    logo = models.ImageField(upload_to='static/logoimgs', verbose_name='企业logo',null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '网站标题'
        verbose_name_plural = verbose_name
        db_table = 'tb_title'


# 声明用户模型类
class Users(models.Model):
    user_phone = models.CharField(max_length=20,verbose_name='手机号', unique=True)
    user_passwd = models.CharField(max_length=100, verbose_name='密码')
    user_name = models.CharField(max_length=20, default='管理员', verbose_name='用户名')
    user_gender = models.CharField(max_length=4,default='F', choices=(('F','女'),('M','男')))
    user_age = models.SmallIntegerField(verbose_name='年龄')
    user_avatar = models.ImageField(upload_to='static/userimgs', verbose_name='用户头像', default='static/userimgs/default_avatar.jpg')
    user_createdat = models.DateTimeField(default=datetime.datetime.now(),verbose_name='注册时间')
    user_updatedat = models.DateTimeField(default=datetime.datetime.now(), verbose_name='更新时间')
    user_active = models.BooleanField(default=True,verbose_name='是否活跃')

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户列表'
        verbose_name_plural = verbose_name


# 声明主页面导航分类模型
class Types(models.Model):
    type_name = models.CharField(max_length=20, verbose_name="导航分类")

    def __str__(self):
        return self.type_name

    class Meta:
        db_table = 'tb_types'
        verbose_name = '导航分类'
        verbose_name_plural = verbose_name


# 声明导航类型的二级分类模型
class SecTypes(models.Model):
    sectype_name = models.CharField(max_length=20,verbose_name="二级分类")
    types = models.ForeignKey(Types,verbose_name='导航分类', on_delete=models.CASCADE)

    def __str__(self):
        return self.sectype_name

    class Meta:
        db_table = 'tb_sectype'
        verbose_name = '二级分类'
        verbose_name_plural = verbose_name

