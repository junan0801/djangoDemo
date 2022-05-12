import json
from mysql.models import BookInfo
from django.http.response import HttpResponse, JsonResponse
from django.views import View


class BookListView(View):
    def get(self, request):
        books = BookInfo.objects.all()
        book_list = []
        for book in books:
            book_dict = {
                'id': book.id,
                'btitle': book.btitle,
                'bpub_data': book.bpub_data
            }
            book_list.append(book_dict)
        return JsonResponse(book_list, safe=False)

    def post(self, request):
        json_str_byte = request.body
        json_str = json_str_byte.decode()
        book_dict = json.loads(json_str)
        book = BookInfo(
            btitle=book_dict['btitle'],
            bpub_data=book_dict['bpub_data']
        )
        book.save()
        json_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'book.bpub_data': book.bpub_data
        }
        return JsonResponse(json_dict, status=201)


class BookDetailView(View):
    def get(self, request, pk):
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse({'message:': '查询数据不存在'}, status=404)
        book_dir = {
            'id': book.id,
            'btitle': book.btitle,
            'book.bpub_data': book.bpub_data
        }
        return JsonResponse(book_dir)

    def put(self, request, pk):
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse({'message:': '要修改的数据数据不存在'}, status=404)
        json_str_byte = request.body
        json_str = json_str_byte.decode()
        book_dict = json.loads(json_str)
        book.btitle = book_dict['btitle'],
        book.bpub_data = book_dict['bpub_data']
        book.save()
        json_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'book.bpub_data': book.bpub_data
        }
        return JsonResponse(json_dict)

    def delete(self, request, pk):
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse({'message:': '待删除数据不存在'}, status=404)
        book.delete()
        return HttpResponse(status=204)
