import aiohttp
import requests
import json
import math
import pandas as pd
import asyncio
datas = []


async def main():
    ids = input("Введите ссылку: ")
    ids = ids.split("https://www.tripadvisor.com/Airline_Review-d")[1]
    ids = ids.split('-')[0]
    cookies = {
        'TAUnique': '%1%enc%3ATT0OJjZFfNatpD4Bco0G7sPVNYq5aIf10DQ959ME2dbLBrWAw0tWog%3D%3D',
        'TASSK': 'enc%3AAEUyieriSdJuSw8wiVCtGcH7eS86dZ2nweRWHDJPfpRmsc9cZGDicfcBE8HiwtU8L%2BWSy7DqBPbdIUQ%2Bv9XAhzrqqKk%2BB%2FIBZ3wxEh8Z2N4tiBamDPv4yE%2BQijTNUxGwVQ%3D%3D',
        'TART': '%1%enc%3AraQ%2BAXKNBu5T2HGp2VW4eR0Tq3kE0wBBOZVKbqLXqZbOy8vllOcM5fFnX1LJl7uX%2BWhIFD%2Fa4fk%3D',
        'TATravelInfo': 'V2*A.2*MG.-1*HP.2*FL.3*RS.1',
        'TATrkConsent': 'eyJvdXQiOiJBRFYsU09DSUFMX01FRElBIiwiaW4iOiJBTkEsRlVOQ1RJT05BTCJ9',
        'TADCID': 'GtFLJlf_cWhGC_m7ABQCFdpBzzOuRA-9xvCxaMyI12-_L_GMe-q3hi36KaBS1_-khV8HwM_flxlbBMQzbDGh2lwwHsjEwrBadoM',
        'PAC': 'AOdQGg5K_MRtzrlpeRGer7dWhKZva4i1eaDzjJAxK_AfWj_SZUM9AvdDnI3uppHy-hGtVINmolvr9c5JP4zxEMQxXOhMTkZfUCjfqVuAbw6T1Ex_fujycTo1B7MDIHTqitpuIq0Wqe5BfJhSEdwzFLRUwVmpskMGZf54FYjUhxol',
        'ServerPool': 'X',
        'PMC': 'V2*MS.55*MD.20220823*LD.20220825',
        'ak_bmsc': 'C89B11ED2FE8CFBE596C7DCF08F27B5C~000000000000000000000000000000~YAAQlh8WAh+Tz8mCAQAAE4Ne1BB+M3qdjJ0KkjvXq6E2reNZqNlyX8Tk0aqLE51C7C88D0dwbzmSdkp2UBLFe6o6dXD2fKvj0SqyInUSiiPeWiekVmEEtM/OJcmi9V1MjUuFEE3jxbpjzg+eOmkq6Ittyc2pIWaljusVdyj/Ssc0hHU80AYvIiB9nx1qGebpxIcP75tcTFfCSvF4FzcSF1nOw6+urpkjvVJYa0U2eOYai8Gz3PfFOnqdVCzBkM9xZ26TiPS0EFVOyBcTj3Bokq1Y8YMsJrqIW4yoZdsDqvTP/SLggYoThJT3anhNF+asYWgkdzj6M9yuo+9gan5bXwryBxOfNjpi4HSYfEW0y03pzu6VgsJDh8/AgzEx3cEHp+k4XrIJac4HJs+iWVCHeA==',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Aug+25+2022+14%3A46%3A18+GMT%2B0500+(%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.30.0&isIABGlobal=false&hosts=&consentId=566f8740-737a-46e0-a9d1-130745ee827f&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A0&AwaitingReconsent=false',
        '__vt': 'ZltZFN83VSJ37f6TABQCIf6-ytF7QiW7ovfhqc-AvR-dH7khcEfZ_5uxz7Z-56xq_Ub7VfgSV6IiLQRPIs9zFZpn67lNWMUX2X3sS9kAW5QMupToy6y2851uBzoZqwc_BygKd6R17RmnOW5TMgXfr6Uw5Q',
        'TASession': 'V2ID.0D0BF5C43DB8468A82EB049299225DC8*SQ.8*LS.DemandLoadAjax*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*FA.1*DF.0*TRA.true*LD.8729141*EAU._',
        'SRT': 'TART_SYNC',
        'TAUD': 'LA-1661247568859-1*RDD-1-2022_08_23*LG-177535266-2.1.F.*LD-177535267-.....',
        'TASID': '0D0BF5C43DB8468A82EB049299225DC8',
        'TAReturnTo': '%1%%2FAirline_Review-d17550095-Reviews-Advanced-Air',
        'roybatty': 'TNI1625!ACFEFgE%2FN6Pu5psaDUmW9Sfb%2FaK9bAa2o9oFqLiWtKsMkUZNSotCySffeaL4yvapN2J4Ja94JV0Aa0h9%2FT2yV6bDP8HPxCN8vSTMt41E3OdvLajCK%2B4TCS2M52SYPZDPISzFD8hMvETlTFbzzBFVJltKTZgPI1iDYvv1gxTr3O6Q%2C1',
        'bm_sv': '95ED7A75FAC44240ED5762A5FDAF6A75~YAAQlB8WAo8dAMiCAQAAiTqn1BARaTez17dHeQAd1N4jQbpBB4X29K3IGoJ4+Mpvpf9Xtw3f5s2KpwQTprLvXhZg3OMrp+wSde1FcI/+QMDM+8TTCF7Qfwdij5ulIhI8zU1nCDCvIs2vKblH6WxnuijY5ro1dsWSF3m4a/Oul9Ix3TADsXDcw+xpqISJnTBGlmohnbJSE7KTgyoXD20lfKHtJ291it+ektc3MPOEwLdFhuJFFg4eNejZViLIoNr9JkjYk6RW~1',
    }
    headers = {
        'authority': 'www.tripadvisor.com',
        'accept': '*/*',
        'accept-language': 'ru,en;q=0.9,la;q=0.8',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'TAUnique=%1%enc%3ATT0OJjZFfNatpD4Bco0G7sPVNYq5aIf10DQ959ME2dbLBrWAw0tWog%3D%3D; TASSK=enc%3AAEUyieriSdJuSw8wiVCtGcH7eS86dZ2nweRWHDJPfpRmsc9cZGDicfcBE8HiwtU8L%2BWSy7DqBPbdIUQ%2Bv9XAhzrqqKk%2BB%2FIBZ3wxEh8Z2N4tiBamDPv4yE%2BQijTNUxGwVQ%3D%3D; TART=%1%enc%3AraQ%2BAXKNBu5T2HGp2VW4eR0Tq3kE0wBBOZVKbqLXqZbOy8vllOcM5fFnX1LJl7uX%2BWhIFD%2Fa4fk%3D; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RS.1; TATrkConsent=eyJvdXQiOiJBRFYsU09DSUFMX01FRElBIiwiaW4iOiJBTkEsRlVOQ1RJT05BTCJ9; TADCID=GtFLJlf_cWhGC_m7ABQCFdpBzzOuRA-9xvCxaMyI12-_L_GMe-q3hi36KaBS1_-khV8HwM_flxlbBMQzbDGh2lwwHsjEwrBadoM; PAC=AOdQGg5K_MRtzrlpeRGer7dWhKZva4i1eaDzjJAxK_AfWj_SZUM9AvdDnI3uppHy-hGtVINmolvr9c5JP4zxEMQxXOhMTkZfUCjfqVuAbw6T1Ex_fujycTo1B7MDIHTqitpuIq0Wqe5BfJhSEdwzFLRUwVmpskMGZf54FYjUhxol; ServerPool=X; PMC=V2*MS.55*MD.20220823*LD.20220825; ak_bmsc=C89B11ED2FE8CFBE596C7DCF08F27B5C~000000000000000000000000000000~YAAQlh8WAh+Tz8mCAQAAE4Ne1BB+M3qdjJ0KkjvXq6E2reNZqNlyX8Tk0aqLE51C7C88D0dwbzmSdkp2UBLFe6o6dXD2fKvj0SqyInUSiiPeWiekVmEEtM/OJcmi9V1MjUuFEE3jxbpjzg+eOmkq6Ittyc2pIWaljusVdyj/Ssc0hHU80AYvIiB9nx1qGebpxIcP75tcTFfCSvF4FzcSF1nOw6+urpkjvVJYa0U2eOYai8Gz3PfFOnqdVCzBkM9xZ26TiPS0EFVOyBcTj3Bokq1Y8YMsJrqIW4yoZdsDqvTP/SLggYoThJT3anhNF+asYWgkdzj6M9yuo+9gan5bXwryBxOfNjpi4HSYfEW0y03pzu6VgsJDh8/AgzEx3cEHp+k4XrIJac4HJs+iWVCHeA==; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Aug+25+2022+14%3A46%3A18+GMT%2B0500+(%D0%95%D0%BA%D0%B0%D1%82%D0%B5%D1%80%D0%B8%D0%BD%D0%B1%D1%83%D1%80%D0%B3%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.30.0&isIABGlobal=false&hosts=&consentId=566f8740-737a-46e0-a9d1-130745ee827f&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A0&AwaitingReconsent=false; __vt=ZltZFN83VSJ37f6TABQCIf6-ytF7QiW7ovfhqc-AvR-dH7khcEfZ_5uxz7Z-56xq_Ub7VfgSV6IiLQRPIs9zFZpn67lNWMUX2X3sS9kAW5QMupToy6y2851uBzoZqwc_BygKd6R17RmnOW5TMgXfr6Uw5Q; TASession=V2ID.0D0BF5C43DB8468A82EB049299225DC8*SQ.8*LS.DemandLoadAjax*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*FA.1*DF.0*TRA.true*LD.8729141*EAU._; SRT=TART_SYNC; TAUD=LA-1661247568859-1*RDD-1-2022_08_23*LG-177535266-2.1.F.*LD-177535267-.....; TASID=0D0BF5C43DB8468A82EB049299225DC8; TAReturnTo=%1%%2FAirline_Review-d8729141-Reviews-Ryanair; roybatty=TNI1625!ACFEFgE%2FN6Pu5psaDUmW9Sfb%2FaK9bAa2o9oFqLiWtKsMkUZNSotCySffeaL4yvapN2J4Ja94JV0Aa0h9%2FT2yV6bDP8HPxCN8vSTMt41E3OdvLajCK%2B4TCS2M52SYPZDPISzFD8hMvETlTFbzzBFVJltKTZgPI1iDYvv1gxTr3O6Q%2C1; bm_sv=95ED7A75FAC44240ED5762A5FDAF6A75~YAAQlB8WAo8dAMiCAQAAiTqn1BARaTez17dHeQAd1N4jQbpBB4X29K3IGoJ4+Mpvpf9Xtw3f5s2KpwQTprLvXhZg3OMrp+wSde1FcI/+QMDM+8TTCF7Qfwdij5ulIhI8zU1nCDCvIs2vKblH6WxnuijY5ro1dsWSF3m4a/Oul9Ix3TADsXDcw+xpqISJnTBGlmohnbJSE7KTgyoXD20lfKHtJ291it+ektc3MPOEwLdFhuJFFg4eNejZViLIoNr9JkjYk6RW~1',
        'dnt': '1',
        'origin': 'https://www.tripadvisor.com',
        'referer': 'https://www.tripadvisor.com/Airline_Review-d17550095-Reviews-Advanced-Air',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Yandex";v="22"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.4.957 Yowser/2.5 Safari/537.36',
        'x-requested-by': 'TNI1625!AMlaSN4qCEwwBmeo+ghqwSe6epU2NiG61GflsDvLHlhsScGJ9pBp2LrHjbLy/TnKQ3G0tXnAYQW4g+bCVcNE0CUZHLGlpqgDBtunOCLigoCay6MzECzX6jSQK17GkCYbVoee0ckjpW/lgu8+UIYMzkUhSeDRpNTDDkASzKxvW1mB',
    }
    json_data = [
        {
            'query': '3405e326c2c3293d928cc2d4e49569ce',
            'variables': {
                'clientPageViews': {
                    'clientRequestTimestampMs': 1661425107467,
                    'request': [
                        {
                            'eventTimestampMs': 1661425107467,
                            'identifierType': 'TA_PERSISTENTCOOKIE',
                            'locale': 'en-US',
                            'userId': None,
                            'sessionId': '0D0BF5C43DB8468A82EB049299225DC8',
                            'origin': 'https://www.tripadvisor.com',
                            'page': 'Airline_Review',
                            'params': [
                                {
                                    'key': 'detail',
                                    'value': '8729141',
                                },
                            ],
                            'path': '/Airline_Review-d17550095-Reviews-Advanced-Air',
                            'referrer': 'https://www.tripadvisor.ru/',
                            'route': '{"page":"Airline_Review","params":{"detail":8729141},"path":"/Airline_Review-d17550095-Reviews-Advanced-Air","fragment":""}',
                            'currency': 'RUB',
                            'uid': '598f00ab-f683-4ee7-b02b-880838a25c28',
                            'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.4.957 Yowser/2.5 Safari/537.36',
                            'viewportCategory': 'DESKTOP',
                            'userAgentCategory': 'DESKTOP',
                            'browserType': 'CHROME',
                            'browserVersion': '102',
                            'osType': 'UNKNOWN',
                        },
                    ],
                },
            },
        },
        {
            'query': '321f914b018c052a546e2c4077b7dfcd',
            'variables': {
                'currency': 'RUB',
                'trafficSourceInfo': {
                    'mcid': None,
                    'servletName': 'Airline_Review',
                    'sessionId': '0D0BF5C43DB8468A82EB049299225DC8',
                    'referrer': 'https://www.tripadvisor.ru/',
                },
            },
        },
        {
            'query': '21093e71975659dafb402053322164f9',
            'variables': {
                'locationId': ids,
                'albumId': 107,
                'fetchTips': True,
            },
        },
        {
            'query': 'c6a86f2cafa4d771868cb7781bb1dfc5',
            'variables': {
                'locationId': ids,
                'albumId': 107,
            },
        },
        {
            'query': '498386bf27e866578dda2b091a87e86e',
            'variables': {
                'locationId': ids,
                'limit': 5,
                'offset': 0,
                'album': 107,
                'loggedInUserId': None,
                'loggedIn': False,
            },
        },
        {
            'query': 'cb6c7bd48b7cc04eb64c367f670f4a8c',
            'variables': {
                'locationId': ids,
                'offset': 0,
                'limit': 5,
                'loggedIn': False,
            },
        },
        {
            'query': 'dbec852cb5641f07639f199f526966e4',
            'variables': {
                'airlineId': ids,
                'currentLocation': 'SVX',
                'fareCategories': [
                    'DOMESTIC',
                    'INTERNATIONAL',
                ],
            },
        },
        {
            'query': '05ee4484c857bedd3a8bb64a1642744c',
            'variables': {
                'key': 'locationReviewFilters_8729141',
                'val': '[{"axis":"LANGUAGE","selections":["en"]}]',
            },
        },
        {
            'query': 'ccb94b358727fd48687b7175909b85ae',
            'variables': {
                'locationId': ids,
                'offset': 0,
                'filters': [
                    {},
                ],
                'prefs': None,
                'initialPrefs': {},
                'limit': 5,
                'filterCacheKey': None,
                'prefsCacheKey': 'locationReviewPrefs_8729141',
                'needKeywords': True,
                'keywordVariant': 'location_keywords_v2_llr_order_30_en',
            },
        },
        {
            'query': 'dbec852cb5641f07639f199f526966e4',
            'variables': {
                'airlineId': ids,
                'currentLocation': 'SVX',
                'fareCategories': [
                    'POPULAR',
                ],
            },
        },
    ]
    response = requests.post('https://www.tripadvisor.com/data/graphql/ids', cookies=cookies, headers=headers, json=json_data)
    answer = response.json()
    count = answer[2].get("data").get("locations")[0].get("reviewSummary").get("count")
    Name = answer[5].get("data").get("locations")[0].get("name")
    print(count)
    page = count / 5
    print(page)
    page = math.ceil(page)
    print(page)
    loop = 0
    loop3 = 30000
    loop2 = 0
    tasks = []
    print("Открыл сессию")
    sessions = aiohttp.ClientSession()
    for p in range(1, page):
        json_data = [
            {
                'query': '3405e326c2c3293d928cc2d4e49569ce',
                'variables': {
                    'clientPageViews': {
                        'clientRequestTimestampMs': 1661425107467,
                        'request': [
                            {
                                'eventTimestampMs': 1661425107467,
                                'identifierType': 'TA_PERSISTENTCOOKIE',
                                'locale': 'en-US',
                                'userId': None,
                                'sessionId': '0D0BF5C43DB8468A82EB049299225DC8',
                                'origin': 'https://www.tripadvisor.com',
                                'page': 'Airline_Review',
                                'params': [
                                    {
                                        'key': 'detail',
                                        'value': ids,
                                    },
                                ],
                                'path': 'Airline_Review-d17550095-Reviews-Advanced-Air',
                                'referrer': 'https://www.tripadvisor.ru/',
                                'route': '{"page":"Airline_Review","params":{"detail":8729141},"path":"/Airline_Review-d17550095-Reviews-Advanced-Air","fragment":""}',
                                'currency': 'RUB',
                                'uid': '598f00ab-f683-4ee7-b02b-880838a25c28',
                                'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.4.957 Yowser/2.5 Safari/537.36',
                                'viewportCategory': 'DESKTOP',
                                'userAgentCategory': 'DESKTOP',
                                'browserType': 'CHROME',
                                'browserVersion': '102',
                                'osType': 'UNKNOWN',
                            },
                        ],
                    },
                },
            },
            {
                'query': '321f914b018c052a546e2c4077b7dfcd',
                'variables': {
                    'currency': 'RUB',
                    'trafficSourceInfo': {
                        'mcid': None,
                        'servletName': 'Airline_Review',
                        'sessionId': '0D0BF5C43DB8468A82EB049299225DC8',
                        'referrer': 'https://www.tripadvisor.ru/',
                    },
                },
            },
            {
                'query': '21093e71975659dafb402053322164f9',
                'variables': {
                    'locationId': ids,
                    'albumId': 107,
                    'fetchTips': True,
                },
            },
            {
                'query': 'c6a86f2cafa4d771868cb7781bb1dfc5',
                'variables': {
                    'locationId': ids,
                    'albumId': 107,
                },
            },
            {
                'query': '498386bf27e866578dda2b091a87e86e',
                'variables': {
                    'locationId': ids,
                    'limit': 5,
                    'offset': loop,
                    'album': 107,
                    'loggedInUserId': None,
                    'loggedIn': False,
                },
            },
            {
                'query': 'cb6c7bd48b7cc04eb64c367f670f4a8c',
                'variables': {
                    'locationId': ids,
                    'offset': loop,
                    'limit': 5,
                    'loggedIn': False,
                },
            },
            {
                'query': 'dbec852cb5641f07639f199f526966e4',
                'variables': {
                    'airlineId': ids,
                    'currentLocation': 'SVX',
                    'fareCategories': [
                        'DOMESTIC',
                        'INTERNATIONAL',
                    ],
                },
            },
            {
                'query': '05ee4484c857bedd3a8bb64a1642744c',
                'variables': {
                    'key': 'locationReviewFilters_8729141',
                    'val': '[{"axis":"LANGUAGE","selections":["en"]}]',
                },
            },
            {
                'query': 'ccb94b358727fd48687b7175909b85ae',
                'variables': {
                    'locationId': ids,
                    'offset': loop,
                    'filters': [
                        {},
                    ],
                    'prefs': None,
                    'initialPrefs': {},
                    'limit': 5,
                    'filterCacheKey': None,
                    'prefsCacheKey': 'locationReviewPrefs_8729141',
                    'needKeywords': True,
                    'keywordVariant': 'location_keywords_v2_llr_order_30_en',
                },
            },
            {
                'query': 'dbec852cb5641f07639f199f526966e4',
                'variables': {
                    'airlineId': ids,
                    'currentLocation': 'SVX',
                    'fareCategories': [
                        'POPULAR',
                    ],
                },
            },
        ]
        task = asyncio.ensure_future(get_coment(cookies, headers, json_data, sessions, page))
        tasks.append(task)
        loop = loop + 5
        loop2 = loop2 + 1
        if loop2 > 30000:
            loop2 = 0
            responses = asyncio.gather(*tasks)
            print(count, " / ", loop)
            await responses
            tasks = []
    responses = asyncio.gather(*tasks)
    print(count, " / ", loop)
    await responses
    await sessions.close()
    List_to_xls(datas, Name)

async def get_coment(cookies, headers, json_data, session, page):
    try:
        async with session.post('https://www.tripadvisor.com/data/graphql/ids', cookies=cookies, headers=headers, json=json_data) as response:
            answer = await response.json()
            answer_coment = answer[8].get("data").get("locations")[0].get("reviewListPage").get("reviews")
            for a in answer_coment:
                try:
                    name = a.get("userProfile").get("displayName")
                    rating = a.get("rating")
                    long = a.get("userProfile").get("hometown").get("location")
                    if long is not None:
                        long = long.get("additionalNames").get("long").split(",")
                    else:
                        long = None
                    labels = a.get("labels")
                    if labels is not None and labels != []:
                        to = labels[0].split("-")[0].strip()
                        out = labels[0].split("-")[1].strip()
                        region = labels[1].strip()
                        _class = labels[2].strip()
                    else:
                        to = None
                        out = None
                        region = None
                        _class = None
                    text = a.get("text")
                    mount_travel = a.get("tripInfo").get("stayDate")
                    if mount_travel is not None:
                        mount_travel = mount_travel.split("-")[1]
                    years_travel = a.get("tripInfo").get("stayDate")
                    if years_travel is not None:
                        years_travel = years_travel.split("-")[0]
                    additionalRatings = a.get("additionalRatings")
                    Legroom = None
                    Inflight_entertainment = None
                    Value_for_money = None
                    Check_in_and_boarding = None
                    Seat_comfort = None
                    Customer_service = None
                    Cleanliness = None
                    Food_and_beverage = None
                    Onboard_Experience = None
                    if additionalRatings != []:
                        for rat in additionalRatings:
                            ratingLabel = rat.get("ratingLabel")
                            if ratingLabel == "Legroom":
                                Legroom = rat.get("rating")
                            elif ratingLabel == "In-flight Entertainment":
                                Inflight_entertainment = rat.get("rating")
                            elif ratingLabel == "Value for money":
                                Value_for_money = rat.get("rating")
                            elif ratingLabel == "Check-in and boarding":
                                Check_in_and_boarding = rat.get("rating")
                            elif ratingLabel == "Seat comfort":
                                Seat_comfort = rat.get("rating")
                            elif ratingLabel == "Customer service":
                                Customer_service = rat.get("rating")
                            elif ratingLabel == "Cleanliness":
                                Cleanliness = rat.get("rating")
                            elif ratingLabel == "Food and Beverage":
                                Food_and_beverage = rat.get("rating")
                            elif ratingLabel == "Onboard Experience":
                                Onboard_Experience = rat.get("rating")
                    datas.append({
                        "name": name,
                        "rating": rating,
                        "long": long,
                        "to": to,
                        "out": out,
                        "region": region,
                        "_class": _class,
                        "mount_travel": mount_travel,
                        "years_travel": years_travel,
                        "Legroom": Legroom,
                        "text": text,
                        "Inflight_entertainment": Inflight_entertainment,
                        "Value_for_money": Value_for_money,
                        "Check_in_and_boarding": Check_in_and_boarding,
                        "Seat_comfort": Seat_comfort,
                        "Customer_service": Customer_service,
                        "Cleanliness": Cleanliness,
                        "Food_and_beverage": Food_and_beverage,
                        "Onboard_Experience": Onboard_Experience
                    })
                except Exception as e:
                    pass
    except Exception as e:
        pass

def List_to_xls(datas, Name):
    ids = []
    names = []
    ratings = []
    sitys = []
    countrys = []
    tos = []
    outs = []
    regions = []
    _classs = []
    mount_travels = []
    years_travels = []
    Legrooms = []
    texts = []
    Inflight_entertainments = []
    Value_for_moneys = []
    Check_in_and_boardings = []
    Seat_comforts = []
    Customer_services = []
    Cleanlinesss = []
    Food_and_beverages = []
    Onboard_Experiences = []
    loop = 1
    for d in datas:
        try:
            name = d.get("name")
            rating = d.get("rating")
            region = d.get("region")
            long = d.get("long")
            if long is not None and long != []:
                if len(long) == 2:
                    sity = long[0]
                    country = long[1]
                else:
                    sity = long[0]
            else:
                sity = None
                country = None
            to = d.get("to")
            out = d.get("out")
            __class = d.get("_class")
            mount_travel = d.get("mount_travel")
            years_travel = d.get("years_travel")
            Legroom = d.get("Legroom")
            text = d.get("text")
            Inflight_entertainment = d.get("Inflight_entertainment")
            Value_for_money = d.get("Value_for_money")
            Check_in_and_boarding = d.get("Check_in_and_boarding")
            Seat_comfort = d.get("Seat_comfort")
            Customer_service = d.get("Customer_service")
            Cleanliness = d.get("Cleanliness")
            Food_and_beverage = d.get("Food_and_beverage")
            Onboard_Experience = d.get("Onboard_Experience")
            ids.append(loop)
            names.append(name)
            ratings.append(rating)
            sitys.append(sity)
            countrys.append(country)
            tos.append(to)
            outs.append(out)
            regions.append(region)
            _classs.append(__class)
            mount_travels.append(mount_travel)
            years_travels.append(years_travel)
            Legrooms.append(Legroom)
            texts.append(text)
            Inflight_entertainments.append(Inflight_entertainment)
            Value_for_moneys.append(Value_for_money)
            Check_in_and_boardings.append(Check_in_and_boarding)
            Seat_comforts.append(Seat_comfort)
            Customer_services.append(Customer_service)
            Cleanlinesss.append(Cleanliness)
            Food_and_beverages.append(Food_and_beverage)
            Onboard_Experiences.append(Onboard_Experience)
            loop = loop + 1
        except Exception as e:
            print(e, long)
    df = pd.DataFrame({
        "ID": ids,
        "Название авиалинии": Name,
        "Имя Фамилия/Nick": names,
        "Общий рейтинг": ratings,
        "Локация userа (город)": sitys,
        "Локация userа (страна)": countrys,
        "Направление (откуда)": tos,
        "Направление (куда": outs,
        "Регион (Europe) ": regions,
        "Класс": _classs,
        "Отзыв": texts,
        "Legroom": Legrooms,
        "In-flight entertainment": Inflight_entertainments,
        "Value for money": Value_for_moneys,
        "Check-in and boarding": Check_in_and_boardings,
        "Seat comfort": Seat_comforts,
        "Customer service": Customer_services,
        "Cleanliness": Cleanlinesss,
        "Food and beverage": Food_and_beverages,
        "Onboard Experience": Onboard_Experiences
    })
    df.to_excel(f'./{Name}.xlsx', engine='xlsxwriter')

if __name__ == '__main__':
    asyncio.run(main())

