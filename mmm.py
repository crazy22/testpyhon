# 批量 -- 提取url下载图片
import os
import urllib
import redis
import time

img_urls = set()  # set 集合

str_map = map()

f = open("D:\\workspaces\\testpyhon\\test.txt", "rb")
while True:
    line = f.readline()  # 按行读取文件
    if line:
        # do something here
        line = str(line).strip()  # str() 将line转化为string
        index = str(line).find('https:')
        if index > 0:
            end_no = str(line).find('png') + 3  # find java --> indexOf
            img_url = str(line)[index:end_no]  # [start,end] 剪切字段 java --> substring()

            print("剪切开始位置:", index, "剪切结束位置:", end_no, "原文:", str(line), "目标文字:", img_url)
            img_urls.add(img_url)
    else:
        break
f.close()

for img_url in img_urls:  #
    try:
        s_num = str(img_url).find('https:') + len('https://www.xxxxxxxx.xxx/app/')
        end_no = str(img_url).find('png') + 3
        img_name = str(img_url)[s_num:end_no]

        pic_exist = os.path.exists(
            'K:\\video-sys\\yd\\images\\' + img_name)
        if pic_exist:
            continue
        else:
            print(img_name)
            f = open('K:\\video-sys\\yd\\images\\' + img_name, 'wb')
            f.write((urllib.request.urlopen(img_url)).read())
            f.close()
    except Exception as e:
        print(img_url + " 图片写入异常！")
print(" 下载完成！")


