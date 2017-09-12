from django.shortcuts import render
from django_web.models import ArtiInfo
from django.core.paginator import Paginator

# Create your views here.
#视图函数,用render函数调用index页面
#render(request,x.html,context)
#context:上下文，替换不同的词来进行句义的表达，把数据库中的数据和网页展示的内容进行映射
def index(request):
    limit = 4
    arti_info = ArtiInfo.objects[:20]
    paginator = Paginator(arti_info, limit)
    page = request.GET.get('page',1)
    print(request)
    print(request.GET)
    loaded = paginator.page(page)


    context = {
        'ArtiInfo':loaded
    } #对网页中的内容进行替换,html 中用双括号进行替换内容
    return render(request, 'index.html', context)
