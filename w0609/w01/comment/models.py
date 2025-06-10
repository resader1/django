from django.db import models
from board.models import Board
from member.models import Member

# Create your models here.
class Comment(models.Model):
    cno = models.AutoField(primary_key=True)
    board = models.ForeignKey(Board,on_delete=models.CASCADE)       # 게시글 삭제시 하단 댓글 전부 삭제
    member = models.ForeignKey(Member,on_delete=models.SET_NULL,null=True)  # 작성자 삭제시 null로 대체
    cpw = models.CharField(max_length=20,null=True,blank=True)
    ccontent = models.TextField(blank=True)
    cdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.cno},{self.member.id},{self.ccontent}'
     