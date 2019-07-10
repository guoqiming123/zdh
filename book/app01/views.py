from django.shortcuts import render,HttpResponse,redirect
from  app01  import  models
# Create your views here.




# 查看所有的书籍
def show_books(request):
    if request.method == 'GET':
        all_book_objs = models.Book.objects.all()
        return render(request, 'show_books.html', {'all_book_objs': all_book_objs})






# 添加
def add_book(request):
    if request.method == 'GET':
        return render(request, 'add_book.html')

    else:
        print(request.POST)
        book_info_dict = request.POST.dict()
        del book_info_dict['csrfmiddlewaretoken']
        print(book_info_dict)
        models.Book.objects.create(**book_info_dict)
        return redirect('show_books')  #重定向



# 删除
def del_book(request, n):
    models.Book.objects.filter(pk=n).delete()
    #最好不要使用get去删除
    return redirect('show_books')     #重定向




# 编辑书籍
def edit_book(request, n):
    if request.method == "GET":
        old_obj = models.Book.objects.get(pk=n)
        return render(request, 'edit_book.html', {'old_obj': old_obj})


    else:
        book_info_dict = request.POST.dict()
        del book_info_dict['csrfmiddlewaretoken']
        print(book_info_dict)
        models.Book.objects.filter(pk=n).update(**book_info_dict)
        return redirect('show_books')   #重定向















def  hello(request):
    return  HttpResponse('no')


def  funk(request):
    return   HttpResponse('ok')


def  funk2(request):
    return   HttpResponse('ok')
