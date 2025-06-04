from django.shortcuts import render,redirect
from board.models import Board

# 상세보기
def view(request,bno):
    qs = Board.objects.get(bno=bno)
    context = {'board':qs}
    return render(request,'board/view.html',context)



#게시판 글쓰기(쓰기 페이지, 쓰기 저장)
def write(request):
    if request.method == 'GET':
        
        return render(request,'board/write.html')
    elif request.method == 'POST':
        id = 'aaa'
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        # DB 저장후 QS변수로 다시 리턴받음.
        print('데이터 확인 : ',btitle,bcontent,bfile)
        qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent)
        qs.bgroup = qs.bno
        print('데이터추가 : ',bfile,qs.bgroup,qs.bstep)
        qs.save()
        return redirect('board:list')
        



# 게시판리스트
def list(request):
    #모든 데이터 가져오기
    qs = Board.objects.all().order_by('-bno')
    context = {'list':qs}
    return render(request,'board/list.html',context)


