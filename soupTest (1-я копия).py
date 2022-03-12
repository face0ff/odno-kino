import requests
import re
import json
from bs4 import BeautifulSoup
import json


headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
}

# silka_url_list = []

# for i in range(1, 712, 1):

# 	url = f'https://rezka.ag/films/page/{i}'

# 	req = requests.get(url, headers= headers)

# 	src = req.text
# 	print(i)



# 	soup = BeautifulSoup(src, "lxml")

# 	all_tit_hrefs = soup.find_all(class_="b-content__inline_item")

# 	# for item in all_tit_hrefs:
# 	# 	item_pic = soup.find('img')
# 	# 	item_text = item.get_text().replace("Фильм   Смотреть трейлер   ", "")
# 	# 	item_href = item.find("a").get("href")
# 	# 	print(f"{item_text}: {item_href}: {item_pic['src']}")

# 	for item in all_tit_hrefs:
# 		item_href = item.find("a").get("href")
# 		silka_url_list.append(item_href)


# with open("silka_url_list.txt", "a") as file:
# 	for line in silka_url_list:
# 		file.write(f"{line}\n")

with open("silka_url_list.txt") as file:
	lines = [line.strip() for line in file.readlines()]

	data_kina =[]
	count = 0
	for line in lines:
		q =requests.get(line)
		result = q.content

		soup = BeautifulSoup(result, "lxml")

		nazFilm = soup.find(class_="b-post__title").find("h1").text
		imdb = soup.find(class_="b-post__info_rates imdb")
		if imdb:
			imdb = imdb.find('span').text
		else:
			imdb = '0'

		ganre_of_kino = []
		all_ganre = soup.findAll(itemprop="genre")
		for item in all_ganre:
			ganre_of_kino.append(item.get_text())

		pic = soup.find(itemprop="image")
		pic_href = pic['src']

		href = soup.find(class_='comments-form')
		if href:

			href = 'https://rezka.ag' + soup.find(class_='comments-form').get("action")
		
		else: 'https://rezka.ag'


		data ={
			'href' : href,
			'nazFilm' : nazFilm,
			'pic_href' : pic_href,
			'imdb' : imdb,
			'ganre' : ganre_of_kino
		}

		count +=1
		print(f'#{count}: {line} is done!')

		data_kina.append(data)

		with open('data.json', 'w', encoding='utf-8') as json_file:
			json.dump(data_kina, json_file, indent=4, ensure_ascii=False)

		


