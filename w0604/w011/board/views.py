from django.shortcuts import render,redirect
from board.models import Board
from django.db.models import F

# 게시글쓰기
def write(request):
    if request.method == "GET":
        return render(request,'board/write.html')
    elif request.method == "POST":
        id = request.POST.get('id')
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        # 1.save() 방식 저장
        Board(id=id,btitle=btitle,bcontent=bcontent,bfile=bfile).save()
        # 2. create저장
        qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent,bfile=bfile)
        qs.bgroup = qs.bno
        qs.save()
        return render(request,'/board/write.html')

# 게시글보기
def view(request,bno):
    qs = Board.objects.get(bno=bno)
    # 1.qs값 수정
    # qs.bhit += 1
    # qs.save()
    
    # 2.F함수사용 - qs에서 특정컬럼의 값을 가져오는 함수
    # qs.update(bhit = F('bhit')+1) #save까지 됨.
    
    context = {'board':qs}
    return render(request,'board/view.html',context)

# 게시판리스트
def list(request):
    # 게시글 전체 가져오기
    qs = Board.objects.order_by('-bgroup','bstep')
    context = {"list":qs}
    return render(request,'board/list.html',context)
