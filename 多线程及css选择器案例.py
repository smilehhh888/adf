import time
import requests
import parsel
import threading
cookies = {
    '__mta': '119837111.1729582202585.1729582248926.1729582254247.7',
    'uuid_n_v': 'v1',
    'uuid': '73EF6000904711EFB8583B7B754A7F950A53A51827F04C5C9C7F0E33943BB27A',
    '_csrf': '3c282a7c27088072eb2c89c95d022ad88faaa902de7468b93ebe279a74ac305f',
    '_lx_utm': 'utm_source%3DBaidu%26utm_medium%3Dorganic',
    '_lxsdk_cuid': '192b321fdc7c8-01ba4a8453e2e2-26001051-144000-192b321fdc7c8',
    '_lxsdk': '73EF6000904711EFB8583B7B754A7F950A53A51827F04C5C9C7F0E33943BB27A',
    '__mta': '119837111.1729582202585.1729582223774.1729582224422.5',
    '_lxsdk_s': '192b321fdc7-32d-36a-1c4%7C%7C14',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '__mta=119837111.1729582202585.1729582248926.1729582254247.7; uuid_n_v=v1; uuid=73EF6000904711EFB8583B7B754A7F950A53A51827F04C5C9C7F0E33943BB27A; _csrf=3c282a7c27088072eb2c89c95d022ad88faaa902de7468b93ebe279a74ac305f; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=192b321fdc7c8-01ba4a8453e2e2-26001051-144000-192b321fdc7c8; _lxsdk=73EF6000904711EFB8583B7B754A7F950A53A51827F04C5C9C7F0E33943BB27A; __mta=119837111.1729582202585.1729582223774.1729582224422.5; _lxsdk_s=192b321fdc7-32d-36a-1c4%7C%7C14',
    'Pragma': 'no-cache',
    'Referer': 'https://www.maoyan.com/board/6?timeStamp=1729582247686&channelId=40011&index=5&signKey=cf9455bacb029e2975b0f987d85a3c3f&sVersion=1&webdriver=false',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'timeStamp': '1729582253999',
    'channelId': '40011',
    'index': '6',
    'signKey': '237a75189d5f6150d7c9e82430181532',
    'sVersion': '1',
    'webdriver': 'false',
}


def get_info(page):
    url1 = f"https://www.maoyan.com/board/4?timeStamp=1729587236399&channelId=40011&index=5&signKey=c26d7e80cca3f067c26d79769438779a&sVersion=1&webdriver=false&offset={page}"
    response = requests.get(url=url1, params=params, cookies=cookies, headers=headers)
    sel = parsel.Selector(response.text)
    dds = sel.css('dd')
    for dd in dds:
        # title = dd.css('p.name a::text').getall()[0]
        # star = dd.css('p.star::text').getall()[0].strip()
        # time = dd.css('p.releasetime::text').getall()[0]
        # score = "".join(dd.css('p.score i::text').getall())[0]
        # print(title,star,time,score)
        print(
            {
                "电影名":dd.css('p.name a::text').getall()[0],
                "主演":dd.css('p.star::text').getall()[0].strip(),
                "上映时间":dd.css('p.releasetime::text').getall()[0],
                "评分":"".join(dd.css('p.score i::text').getall())
            }
        )
#         zip 如果有一条是空的呢

# 总共的运行时间 多线程
start_time = time.time()
for page in range(0,100,10):
    threading.Thread(target=get_info,args=(page,)).start()
print("总线程数:",threading.enumerate())# threading.enumerate()函数返回当前活动的线程数量
while len(threading.enumerate())>1: # 活动线程的数量大于1时，表示还有线程在执行任务 当还有线程在执行时，会一直执行pass语句
    pass
print("总共运行时间：",time.time()-start_time,"s",sep=" ")

