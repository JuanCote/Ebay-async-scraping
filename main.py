import datetime
import time
from bs4 import BeautifulSoup
import csv
import asyncio
import aiohttp
import lxml

cookies = {
    '__ssds': '2',
    '__ssuzjsr2': 'a9be0cd8e',
    '__uzmaj2': '2ece1212-611b-4d4b-aef5-67a4adba6ccc',
    '__uzmbj2': '1656161630',
    'QuantumMetricUserID': '2c843599a9815f01995106f8e371e5fe',
    '__gsas': 'ID=3c544129365ec14b:T=1656161706:S=ALNI_MaUvQLNiAbvjLfXYY8PTmoBGZDbKA',
    '__uzma': 'cb0d5f5f-f5f8-4eee-b938-d698fc65db99',
    '__uzmb': '1656161789',
    '__uzme': '5073',
    '__deba': 'bsnnXDtsRbAISwGjo256RmeQgnAXZoOp5CvZbI17Ti2kclay8IlfCCAEGnKRS3EHXR8UW1J2_XMwSXzXGqPFGHULunsUX3CTIXMVVD57NsaKW3_iTX6IUkzMTbIcWDtkLAC0g-RLupcaQd2reQvn3Q==',
    '__uzmc': '701201921694',
    '__uzmd': '1656256380',
    '__uzmf': '7f60000fe9750f-3b91-46f8-9a5f-538aa27efb1a165616178966894590676-2106141f3beecc2d19',
    'ak_bmsc': 'B813AD7D28DC9FFF44702E3FB057C11E~000000000000000000000000000000~YAAQnU1lX/B4HZSBAQAAZ76SoBDG9Q+FtWuU4c65P5x9wv7rI/8FMecp+iW/sHaeJRZ4KzZdQX1aouO4bCxeXZ85b5rWM4Bk5giHdaFo41Nmbn+AhHBPckEzIXuljb3H7yENeqjES6QBCz3tTAKxtGWeThLFVlhBNqvM/IDcLdDKB1BTE/a8qaozYqink7c4vUQ22gs/t5sP+9mr3vnCTkVWo7JbhFknyRLGyevXcBOSModuCudTLANP0QNlOUYKm9nw4CMkDDFqJ9DrLx+XwwmDP3vvGH/tGaZhqbLa8U3vp1RE33IKIJbSUJ+r+MUDF/uDPtCHzvI/w0VJrTu/D+ckCRhweBbiQPUTAfYIAfnNluqIEL7yLQx8ySLb5EO8l5Ym+ZfsBXM=',
    '__uzmcj2': '636962878746',
    '__uzmdj2': '1656256380',
    's': 'CgAD4ACBiucj+OWFlY2Y3MzgxODEwYWQzNDNhOWJjZmJkZmZkZjk1YmXc1qQg',
    'QuantumMetricSessionID': '6c2d54c203e7e2297d28a63c93db291e',
    'ebay': '%5Ejs%3D1%5Esbf%3D%23000000%5E',
    'bm_sv': 'E7823F5CABB1D0A03752323652D3156E~YAAQbr17XLdrzY2BAQAAMCGtoBAz3uZKkxXvG4uR0wBtxCRYd0MreJYSukf2CgP3BCRVUDMuErCJYG/KOyn8cUnXLcLtsO1CtcwcZVkkHFrQypZB13bOYK0S8zZPnHhZeZ8DMVygSgXl4jOQmcU05rkGSyJtZDAoj4peftG9KrpCBYrFEDFmJkbU+Uz7qVEGMCY/eWP2vxJNudgQjMK3hGdrBQ1YO0SCsy9xtZwML5dOhXOj7xvVpW9uJmsBvo8=~1',
    'dp1': 'bu1p/QEBfX0BAX19AQA**667ae5b2^pbf/%23e000e000000000000000006499b232^bl/UA667ae5b2^',
    'nonsession': 'BAQAAAYA5+AiKAAaAADMABWSZsjIxNDAwMADKACBmeuWyOWFlY2Y3MzgxODEwYWQzNDNhOWJjZmJkZmZkZjk1YmUAywACYriFujY2n2cTiaa4n6SABuCdq2zbNki7LOM*',
    'totp': '1656258710473.8c4zG5YXwjdob2W8f5IdUyt+m6erDUOaOEdvT7rLGD2t2Hq53BP+WGWjNSRIa5MAfjrquJ0i6ujhOjmzG1hHHlHh2VVOGtdd7snyTvBn+Gen6rSOEnKBsttqbXAcNOtg',
}

headers = {
    'authority': 'www.ebay.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-US;q=0.6,uk;q=0.5',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-full-version': '"102.0.5005.115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
}

params = {
    '_pgn': '1',
}

result_data = []


async def get_page_data(session, page, category):
    params['_pgn'] = page

    async with session.get(url=category, params=params, cookies=cookies, headers=headers) as response:
        response_text = await response.text()
        soup = BeautifulSoup(response_text, 'lxml')
        cards = soup.find_all('li', class_='s-item s-item--large')
        if len(cards) == 0:
            return 1

        for card in cards:
            name = card.find('a', class_='s-item__link').find('h3').text
            try:
                rate = card.find('span', class_='b-rating__rating-star').find('svg').find('title').text
            except:
                rate = 'No rate'
            try:
                price = card.find('span', class_='s-item__price').text
            except:
                price ='No price'
            try:
                logistic_cost = card.find('span', class_='s-item__shipping s-item__logisticsCost').text
            except:
                logistic_cost = 'No cost of deliver'
            result_data.append({
                'name': name,
                'rate': rate,
                'price': price,
                'logistic_cost': logistic_cost
            })


async def get_tasks(category, i=1):
    while True:
        async with aiohttp.ClientSession() as session:
            tasks = []
            for page in range(i, i + 20):
                tasks.append(asyncio.create_task(get_page_data(session, page, category)))

            result = await asyncio.gather(*tasks)
            if 1 in result:
                break
            i += 20


def main(category):
    date = datetime.date.today()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(get_tasks(category))

    with open(f'result_{date}.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(
            ('Name', 'Rate', 'Price', 'Logistic Cost')
        )

    with open(f'result_{date}.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        for elem in result_data:
            writer.writerow(
                (
                    elem['name'],
                    elem['rate'],
                    elem['price'],
                    elem['logistic_cost']
                )
            )

    result_data.clear()
    return f'result_{date}.csv'



