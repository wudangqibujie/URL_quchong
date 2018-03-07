import random

def Get_urls():
    urls = []
    url = "https://www.doutula.com/article/list/?page=%d"
    for i in range(50):
        urls.append(url%random.randint(1,30))
    return urls
    # print(urls)


