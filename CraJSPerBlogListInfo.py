##爬取CSDN个人博客首页的目录信息
import requests
from bs4 import BeautifulSoup
import re

def getPage(user_agent,referer,host):
    header = {'User-Agent': user_agent, 'Referer': referer, 'Host': host}
    try:
        html_bytes = requests.get(url=referer, headers=header)
        html = html_bytes.content.decode("UTF-8")
        soup = BeautifulSoup(html, "html.parser")
    except BaseException:
        return "1"
    else:
        return soup

def crawling(agent,str_,h,num):
    for i in range(1,num):
        s = getPage(agent,str_,h)
        print(s)
        if s is not "1":
            infos = s.find_all(name='code')
            j = 0
            if infos.__len__() == 0 :
                break
            else:
                pass
            fobj.write("第"+str(i)+"页\n")
            for info in infos:
                j += 1
                fobj.write(info.get_text()+"\n")
                print(info.get_text()+"\n")
        else:
            break


star_url ="https://www.jianshu.com/p/36b4cbfdc016" #"https://www.jianshu.com/p/c6fad9831d3b"  #
end_url = "/article/list/{}?"
complete_url = star_url #+ end_url
user_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
strUrl = "https://www.jianshu.com/p/c6fad9831d3b"
host_ = 'cdn2.jianshu.io'

if __name__ == '__main__':
    try:
        #open(path, ‘-模式-‘,encoding=’UTF-8’)
        #即open(路径+文件名, 读写模式, 编码)
        fobj=open("简书.txt",'a',encoding='utf-8')
        # 这里的a意思是追加，这样在加了之后就不会覆盖掉源文件中的内容，如果是w则会覆盖。
    except IOError:
        print('*** file open error:')# CSDN博客目录信息.txt
    else:
        s = getPage(user_Agent,star_url,host_)
        h1 = s.find("h1", class_="title")
        #  这里的\n的意思是在源文件末尾换行，即新加内容另起一行插入。
        fobj.write(h1.get_text()+'\n\n')
        crawling(user_Agent,complete_url,host_,10)
        fobj.write('END'+'\n\n\n\n\n')
        #   特别注意文件操作完毕后要close
        fobj.close()
