import urllib.request
import re
def TaoBao(url, a):
    headers = 'User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url)
    data = file.read().decode('utf-8')
    pat = '"pic_url":"//(.*?)","price"'
    lis = re.compile(pat).findall(data)
    j = a + 1
    for i in lis:
        print(i)
        url = 'http://{}'.format(i)
        req = urllib.request.Request(url)
        data = urllib.request.urlopen(req).read()
        Tu_Pian = open(r'E:\淘宝手机图片\{}'.format(str(j) + '.jpg'), 'ab+')
        Tu_Pian.write(data)
        j += 1
        Tu_Pian.close()


for a in range(0,4800,48):
    if a == 0:
        url = 'https://s.taobao.com/search?q=%E6%89%8B%E6%9C%BA&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=&ie=utf8&initiative_id=tbindexz_20170306'
    else:
        url = 'https://s.taobao.com/search?q=%E6%89%8B%E6%9C%BA&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=&ie=utf8&initiative_id=tbindexz_20170306&p4ppushleft=5%2C48&s={}'.format(a)
    TaoBao(url, a)

