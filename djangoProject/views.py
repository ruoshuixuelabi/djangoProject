from django.http import JsonResponse

import cpca


def hello(request):
    name = request.GET.get('name')
    try:
        df = cpca.transform_text_with_addrs(name)
    except KeyError as e:
        df = None
    if df is None:
        # print("序号：%s   值：%s " % (name_list.index(i) + 1, i))
        a = {
            "jiexi": 1963
        }
    else:
        # print("序号：%s   值：%s 分词结果：%s" % (name_list.index(i) + 1, i, df))
        a = df.to_dict('dict')
    return JsonResponse(a)
