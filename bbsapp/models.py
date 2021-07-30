from django.db import models

# Create your models here.

class Userinfo(models.Model):
    id=models.CharField('工号',primary_key=True,max_length=6)
    name = models.CharField('姓名', max_length=10)
    sex = models.CharField('性别', max_length=4)
    password = models.CharField('密码', max_length=50)
    keshi = models.CharField('科室', max_length=50)
    duty = models.CharField('职务', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)
    is_active = models.BooleanField('活跃状态', default=True)
    ud_operator = models.CharField('操作人', max_length=10)
    is_spuser = models.BooleanField('超级用户', default=False)

    # 表名自定义
    class Meta:
        db_table='userinfo'
        verbose_name_plural='用户信息'

    # admin界面的显示哪些数据及格式
    def __str__(self):
        return '%s | %s | %s | %s | %s'%(self.id,self.name,self.sex,self.keshi,self.duty)

class Posting(models.Model):
    index=models.CharField('索引',primary_key=True,max_length=10)
    title=models.CharField('题目',max_length=40)
    content=models.TextField('内容')
    content_digest=models.CharField('内容摘要',max_length=40,default='')
    poster=models.CharField('发帖人',max_length=10,default='游客')
    comment_num=models.IntegerField('评论数',default=0)
    like_num=models.IntegerField('点赞数',default=0)
    created_time=models.DateTimeField('创建时间',auto_now_add=True)
    updated_time=models.DateTimeField('更新时间',auto_now=True)
    is_active=models.BooleanField('活跃状态',default=True)
    operator=models.CharField('操作人',max_length=10,default='')

    class Meta:
        db_table='posting'
        verbose_name_plural='帖子表'

    def __str__(self):
        return '%s|%s|%s|%s|%s|%s'%(self.title,self.poster,self.created_time,self.updated_time,self.is_active,self.operator)

class Comments(models.Model):
    index=models.CharField('索引',primary_key=True,max_length=10)
    posting=models.ForeignKey(Posting,null=True,blank=True,on_delete=models.SET_NULL)
    content=models.TextField('评论')
    poster=models.CharField('评论人',max_length=10,default='游客')
    created_time=models.DateTimeField('创建时间',auto_now_add=True)
    updated_time=models.DateTimeField('更新时间',auto_now=True)
    is_active=models.BooleanField('活跃状态',default=True)
    operator=models.CharField('操作人',max_length=10)

    class Meta:
        db_table='comments'
        verbose_name_plural='评论表'

    def __str__(self):
        return '%s|%s|%s|%s|%s|%s'%(self.content,self.poster,self.created_time,self.updated_time,self.is_active,self.operator)






