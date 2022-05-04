import requests
import re
import json
from bs4 import BeautifulSoup
import json
import asyncio
import aiohttp
import time

data_kina = []

async def get_page_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'ua,ua-UA;q=0.8,en-US;q=0.5,en;q=0.3',
        'Referer': 'https://www.espncricinfo.com/',
        'Upgrade-Insecure-Requests': '1',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }
    async with aiohttp.ClientSession(trust_env=True) as session:

        q = await session.get(url, headers = headers)
        soup = BeautifulSoup(await q.text(), "lxml")
        try:
            nazFilm = soup.find(class_="lister-item-header").find('a').text
            href = 'https://www.imdb.com' + soup.find(class_="lister-item-header").find('a')['href']
            imdb = soup.find(class_="ratings-bar").find('strong').text
            pic = soup.find(class_="loadlate")
            pic_href = pic['src']
            all_ganre = soup.find(class_="genre").text
            all_ganre = re.sub(r"[ \n]", "", all_ganre)
            all_ganre = all_ganre.split(",")

        except:
            nazFilm = "Нет названия фильма"


        print(nazFilm)
        data = {
            'href': href,
            'nazFilm': nazFilm,
            'pic_href': pic_href,
            'imdb': imdb,
            # 'prosmotr': prosmotr,
            # 'year': year,
            'ganre': all_ganre,

        }
        data_kina.append(data)


async def gather_data():
    tasks = []
    for i in range(1, 20, 1):
        url = f'https://www.imdb.com/search/title/?genres=comedy&start={i}&ref_=adv_nxt'

        task = asyncio.create_task(get_page_data(url))
        tasks.append(task)
    await asyncio.gather(*tasks)

def main():
    asyncio.run(gather_data())
    with open('data.json', 'w', encoding='utf-8') as json_file:
        json.dump(data_kina, json_file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()


# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     'Accept-Language': 'ua,ua-UA;q=0.8,en-US;q=0.5,en;q=0.3',
#     'Referer': 'https://www.espncricinfo.com/',
#     'Upgrade-Insecure-Requests': '1',
#     'Connection': 'keep-alive',
#     'Pragma': 'no-cache',
#     'Cache-Control': 'no-cache',
# }
# silka_url_list = []
# for i in range(1, 151, 50):
#
#     url = f'https://www.imdb.com/search/title/?genres=comedy&start={i}&ref_=adv_nxt'
#
#     req = requests.get(url, headers=headers)
#
#     src = req.text
#     print(i)
#
#     soup = BeautifulSoup(src, "lxml")
#
#     all_tit_hrefs = soup.find_all(class_="lister-item-content")
#
#     for item in all_tit_hrefs:
#         item_href = item.find("a").get("href")
#         silka_url_list.append(item_href)
#
# with open("silka_url_list.txt", "w") as file:
#     for line in silka_url_list:
#         file.write('https://www.imdb.com' + f"{line}\n")

