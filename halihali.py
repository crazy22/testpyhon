##爬取动漫视频
import requests
from bs4 import BeautifulSoup
import time
import hashlib
from contextlib import closing
import threading
import os


def getPage(user_agent, referer, host):
    header = {'User-Agent': user_agent, 'Referer': referer}
    try:
        html_bytes = requests.get(url=referer, headers=header)
        html = html_bytes.content.decode("UTF-8")
        soup = BeautifulSoup(html, "html.parser")
    except BaseException:
        return "1"
    else:
        return soup


def crawling(agent, str_, h, num):
    for r in range(1, num):
        str_1 = str_.replace('?', str(r))
        s = getPage(agent, str_1, h)
        print(s)
        print('-----------------------------------------------------------------------')
        if s is not "1":
            infos = s.find_all(name='script')
            j = 0
            if infos.__len__() == 0:
                pass
            else:
                pass
            for info in infos:
                j += 1
                scriptStr = info.get_text().replace("\\", "")
                scriptUrl = scriptStr[scriptStr.find('var zanpiancms_player = {\"url\":\"') + len(
                    'var zanpiancms_player = {\"url\":\"'):scriptStr.find('\",')]
                if scriptUrl.find('mp4') > 0:
                    fobj.write(scriptUrl + '?' + str(r) + "\n")
                    urls.add(scriptUrl + '?' + str(r))
                    print('url: ', scriptUrl + '?' + str(r))
                else:
                    pass
        else:
            pass
    for r in range(4):
        t = threading.Thread(target=run)
        # t.daemon = True
        t.start()


def download_file(url, path):
    with closing(requests.get(url, stream=True)) as r:
        chunk_size = 1024 * 10
        content_size = int(r.headers['content-length'])
        if os.path.exists(path) and os.path.getsize(path) >= content_size:
            print('已下载')
            return
        print('下载开始')
        with open(path, "wb") as f:
            p = ProgressData(size=content_size, unit='Kb', block=chunk_size, file_name=path)
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
                p.output()


def run():
    for u in urls:
        url_arr = u.split('?')
        if u is None:
            print(u'全下完啦')
            break
        h = hashlib.md5()
        h.update(url_arr[0].encode("utf8"))
        url = url_arr[0]
        name = videoName + '-第' + url_arr[1] + '集'  # h.hexdigest()
        path = 'e:/download/MP4/' + name + '.mp4'
        print(h.hexdigest(), ':', url_arr[1])
        if os.path.exists(path):
            pass
        else:
            download_file(url, path)


class ProgressData(object):

    def __init__(self, block, size, unit, file_name='', ):
        self.file_name = file_name
        self.block = block / 1000.0
        self.size = size / 1000.0
        self.unit = unit
        self.count = 0
        self.start = time.time()

    def output(self):
        self.end = time.time()
        self.count += 1
        speed = self.block / (self.end - self.start) if (self.end - self.start) > 0 else 0
        self.start = time.time()
        loaded = self.count * self.block
        progress = round(loaded / self.size, 4)
        if loaded >= self.size:
            print(u'%s下载完成\r\n' % self.file_name)
        else:
            print(u'{0}下载进度{1:.2f}{2}/{3:.2f}{4} {5:.2%} 下载速度{6:.2f}{7}/s'.
                  format(self.file_name, loaded, self.unit,
                         self.size, self.unit, progress, speed, self.unit))
            print('%50s' % ('/' * int((1 - progress) * 50)))


star_url = ' .html' #http://www.halihali.cc/v/jinjidejurendisanji/0-2.html
complete_url = ''
user_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
strUrl = "http://www.halihali.cc/v/dongjingshishiguidisanji/0-1.html"
host_ = 'http://www.halihali.cc/'
urls = set()
videoName = ''

if __name__ == '__main__':
    videoUrl = input('请输入视频地址:')
    videoName = input('请输入视频名称:')
    try:
        # videoName = videoUrl[videoUrl.find('/v/') + len('/v/'):videoUrl.find('/0-')]
        strSplit = videoUrl.split('/')
        for i in strSplit:
            if str(i).find('.html') > 0:
                i = '0-?.html'
            else:
                i = i + '/'
            complete_url = complete_url + i
        # open(path, ‘-模式-‘,encoding=’UTF-8’)
        # 即open(路径+文件名, 读写模式, 编码)
        fobj = open("url.txt", 'a', encoding='utf-8')
        # 这里的a意思是追加，这样在加了之后就不会覆盖掉源文件中的内容，如果是w则会覆盖。
    except IOError:
        print('*** file open error:')
    else:
        #  这里的\n的意思是在源文件末尾换行，即新加内容另起一行插入。
        # fobj.write(h1.get_text()+'\n\n') E:\vidio\vi1
        crawling(user_Agent, complete_url, host_, 13)
        fobj.write('----------------------我是分割线----------------------' + '\n')
        #   特别注意文件操作完毕后要close
        fobj.close()
