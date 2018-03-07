import urls_create
import requests
import hashlib

old_urls = {}
def get_html():
    pass
def url_filter(new_url):
    if new_url in old_urls:
        return True
    else:
        return False
def get_new_url(urls_list):
    new_url = urls_list.pop()
    return new_url
def old_urls_md5(old_url):
    m = hashlib.md5()
    m.update(old_url.encode('utf-8'))
    m.hexdigest()
    old_urls.add(m.hexdigest())
    return old_urls

if __name__ == '__main__':
    urls = urls_create.Get_urls()
    while True:
        try:
            new_url = get_new_url(urls)
            print(new_url)
        except:
            print("没有URLS了")
            break





    #
    # if url_filter(new_url):
    #     get_html()
