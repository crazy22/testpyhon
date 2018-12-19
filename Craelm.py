## 根据需要的菜单爬取相应图片下载
import os
import urllib

import requests
from bs4 import BeautifulSoup
import re
import json

import difflib


# import jieba
# import Levenshtein


def getJsonData(user_agent, referer, url, cookie):
	header = {'User-Agent': user_agent, 'Referer': referer, 'cookie': cookie}
	try:
		html_bytes = requests.get(url=url, headers=header)
		html = html_bytes.content.decode("UTF-8")

		shop_data = json.loads(html)
		# soup = BeautifulSoup(html, "html.parser")
	except BaseException:
		return "1"
	else:
		return shop_data


user_Agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36'

food_referer = "https://h5.ele.me/msite/food/"
shop_rReferer = "https://h5.ele.me/shop/"
cookie = "-------------cookie从浏览器上copy-------------------"
# rank_id --》 地理信息
star_url = "https://h5.ele.me/restapi/shopping/v3/restaurants?latitude=30.487358&longitude=114.415994&keyword=&offset=0&limit=30&extras[]=activities&extras[]=tags&terminal=h5&rank_id=cb3f6dd8750b48e0a8829ac3e266eb7d&brand_ids[]=&restaurant_category_ids[]=209&restaurant_category_ids[]=212&restaurant_category_ids[]=213&restaurant_category_ids[]=214&restaurant_category_ids[]=215&restaurant_category_ids[]=216&restaurant_category_ids[]=217&restaurant_category_ids[]=219&restaurant_category_ids[]=265&restaurant_category_ids[]=266&restaurant_category_ids[]=267&restaurant_category_ids[]=268&restaurant_category_ids[]=269&restaurant_category_ids[]=221&restaurant_category_ids[]=222&restaurant_category_ids[]=223&restaurant_category_ids[]=224&restaurant_category_ids[]=225&restaurant_category_ids[]=226&restaurant_category_ids[]=227&restaurant_category_ids[]=228&restaurant_category_ids[]=231&restaurant_category_ids[]=232&restaurant_category_ids[]=263&restaurant_category_ids[]=218&restaurant_category_ids[]=234&restaurant_category_ids[]=235&restaurant_category_ids[]=236&restaurant_category_ids[]=237&restaurant_category_ids[]=238&restaurant_category_ids[]=211&restaurant_category_ids[]=229&restaurant_category_ids[]=230&restaurant_category_ids[]=264"

shop_url_start = "https://h5.ele.me/pizza/shopping/restaurants/"
shop_url_end = "/batch_shop?user_id=142140910&code=0.9515950814125727&extras=%5B\"activities\"%2C\"albums\"%2C\"license\"%2C\"identification\"%2C\"qualification\"%5D&terminal=h5&latitude=30.487358&longitude=114.415994"

food_menu_arr = ['香菜拌牛肉',
				 '凉拌皮蛋',
				 '油炸花生米',
				 '凉拌腐竹',
				 '泡椒藕带',
				 '养生黑木耳',
				 '凉拌毛豆',
				 '刀拍黄瓜',
				 '精武鸭头',
				 '番茄土鸡蛋汤',
				 '青菜豆腐汤',
				 '三鲜汤',
				 '香豆渣白菜汤',
				 '山药肉片汤',
				 '香菇炖生态土鸡',
				 '秘制生态老鸭汤',
				 '干锅肥肠',
				 '香辣基围虾',
				 '白灼基围虾',
				 '酸菜牛肉锅仔',
				 '土豆烧鸡',
				 '秘制黄豆鱼',
				 '蒜香排骨',
				 '土豆烧鸭',
				 '狗肉炒面',
				 '肉丝炒面',
				 '皇上面',
				 '黄鳝面',
				 '胖头鱼火锅',
				 '三腊火锅',
				 '干锅黄豆蹄花',
				 '牛肉火锅',
				 '羊肉锅仔',
				 '墨鱼排骨汤',
				 '莲藕炖排骨',
				 '海带炖骨头',
				 '玉米炖骨头',
				 '红烧肉烧土豆',
				 '蒸土鸡蛋',
				 '土豆饼',
				 '红糖发糕',
				 '米酒汤圆',
				 '麦乐鸡块',
				 '手工饺子',
				 '奶油馒头',
				 '本地韭菜炒土鸡蛋',
				 '青椒炒土鸡蛋',
				 '西红柿炒土鸡蛋',
				 '酸辣土豆丝',
				 '农家豆腐',
				 '清炒油麦菜',
				 '香菇小白菜',
				 '清炒红菜苔',
				 '白菜杆炒肉',
				 '农家小炒肉',
				 '榨菜炒肉丝',
				 '香干炒肉',
				 '爆炒回锅肉',
				 '胡萝卜肉丝',
				 '千张肉丝',
				 '莴苣炒肉',
				 '笋子炒腊肉',
				 '藜蒿炒腊肉',
				 '大蒜炒腊肉',
				 '腊肉炒年糕',
				 '农家苕粉丸',
				 '家常鱼块',
				 '爆炒肥肠',
				 '火爆猪肝',
				 '火爆腰花',
				 '干锅手撕包菜',
				 '虎皮青椒',
				 '爆炒顺风',
				 '回锅牛肉'
				 ]
not_find_foods = ""

if __name__ == '__main__':
	try:
		# open(path, ‘-模式-‘,encoding=’UTF-8’)
		# 即open(路径+文件名, 读写模式, 编码)
		fobj = open("饿了么.txt", 'a', encoding='utf-8')
		# 这里的a意思是追加，这样在加了之后就不会覆盖掉源文件中的内容，如果是w则会覆盖。
	except IOError:
		print('*** file open error:')
	else:
		print("---需求菜单:---\n", food_menu_arr)
		food_shop = getJsonData(user_Agent, food_referer, star_url, cookie)
		if food_shop == "1":
			pass
		else:
			if "name" in food_shop:  # cookie失效
				print("未登录")
			else:
				shop_items = food_shop["items"]
				shop_items_len = len(shop_items)
				print("店铺数量: ", shop_items_len)
				for i in range(0, shop_items_len):
					restaurant_id = shop_items[i]["restaurant"]["id"]  # 店铺id
					shop_url = shop_url_start + restaurant_id + shop_url_end
					fobj.write("店名: " + shop_items[i]["restaurant"]["name"] + '\n地址: ' + shop_url + '\n\n')
					shop_data = getJsonData(user_Agent, shop_rReferer, shop_url, cookie)
					print("店名: " + shop_items[i]["restaurant"]["name"])
					if shop_data == "1":
						pass
					else:
						if "name" in shop_data:
							print("未登录")
						else:
							menu = shop_data["menu"]
							menu_len = len(menu)
							print(menu)
							for m in range(0, menu_len):
								foods = menu[m]['foods']
								foods_len = len(foods)
								#   print("菜单名称: ", menu[m]['name'], " ; 菜品数量: ", foods_len)
								for f in range(0, foods_len):
									food_name = foods[f]['name']
									fm_len = len(food_menu_arr)
									for fm in range(0, fm_len):  # 菜名匹配度>0.5的图片都怕下来了
										need_food_name = food_menu_arr[fm]
										result = difflib.SequenceMatcher(
											lambda x: x in '（不含米饭）+1234567890lL份个段根只克热冷加辣打包（单点不送）一两二三四', food_name,
											need_food_name)
										ratio = result.ratio()
										if ratio > 0.5:
											break
										else:
											continue
									if ratio > 0.5:
										pass
									else:
										continue
									food_photos = foods[f]['photos']
									food_photos_len = len(foods[f]['photos'])
									print("菜名: ", food_name, " ; 需求菜名: ", need_food_name, " ; 地址集合: ", food_photos,
										  " ; 图片数量: ", food_photos_len)
									for p in range(0, food_photos_len):
										photo_path = food_photos[p]
										path_1 = photo_path[0:1]
										path_2 = photo_path[1:3]
										path_3 = photo_path[3:]
										photo_format = photo_path[32:]
										print("地址: ", photo_path, " ; 字符串长度: ", len(photo_path), "图片格式: ", photo_format)
										real_path = "https://fuss10.elemecdn.com/" + path_1 + "/" + path_2 + "/" + path_3 + "." + photo_format
										print("真实地址: ", real_path)
										try:
											pic_exist = os.path.exists(
												'K:\\need\\' + str(food_name) + "." + photo_format)
											if pic_exist:
												print(" 图片已存在！")
												print(
													"##########################################################################")
												continue
											f = open('K:\\need\\' + str(food_name) + "." + photo_format, 'wb')
											f.write((urllib.request.urlopen(real_path)).read())
											f.close()
										except Exception as e:
											print(" 图片写入异常！")
										print(
											"##########################################################################")
									print("----------------------------------------------------------------------")
								print("----------------------------------------------------------------------")
							print("----------------------------------------------------------------------")
			fobj.write('END' + '\n\n\n\n\n')
			#   特别注意文件操作完毕后要close
		fobj.close()
		print("图片下载完成！")