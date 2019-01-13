import json
import os
import sys
from google import google
from random import randint

def crawl(word, num_page=10):

    # 从google获取数据
    search_results = google.search(word, num_page)
    result = []

    # 将query的每个结果加入到result，分别获取title, description, url
    for item in search_results:
        result.append({
            'title' : item.name,
            'description' : item.description,
            'url' : item.link
        })


    # 直接将包含了dict的list转换成json并保存到文件
    with open('result/{}.txt'.format(word), 'wt') as fw:
        fw.write(json.dumps(result))

    # 相比上面，没有list的[]
    with open('result2/{}.txt'.format(word), 'at') as fw:
        for x in result:
            fw.write(json.dumps(x))


result=[]
with open('doc.txt','rb') as f:
    result = [x.decode('utf8').strip() for x in f.readlines()]
word_set = []
# 待查询的query
word_set = result
print(result)
count = 0
for word in word_set:
    print('begin {}'.format(word))
    crawl(str(word))

    print('end {}'.format(word))
