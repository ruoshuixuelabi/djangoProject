from django.http import JsonResponse

import cpca
from pdf2docx import Converter
import uuid


def pdf(request):
    name = request.GET.get('name')
    names = uuid.uuid1()
    try:
        pdf_file = 'D:/pdftohtml/' + name + '.pdf'
        docx_file = 'D:/pdftohtml/' + name + '.docx'
        # convert pdf to docx
        cv = Converter(pdf_file)
        cv.convert(docx_file)  # all pages by default
        cv.close()
    except KeyError as e:
        df = None
        # print("序号：%s   值：%s 分词结果：%s" % (name_list.index(i) + 1, i, df))
    a = {'result': name}
    return JsonResponse(a)
