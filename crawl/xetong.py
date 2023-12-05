import os
import time

import requests
from urllib.parse import urlparse
import urllib.parse

_cookie = 'shop_version_type=4; anony_token=0d9d7a59867b4cdc0f9ab45c9cf1b75d; xenbyfpfUnhLsdkZbX=0; sensorsdata2015jssdkcross=%7B%22%24device_id%22%3A%2218c378c26565c6-070d0cf3e894d3-16525634-2073600-18c378c2657733%22%7D; sajssdk_2015_new_user_appozttsb523729_h5_xiaoeknow_com=1; ko_token=8d308c22b8dc1e9ad6b103a2af7d3a84; sa_jssdk_2015_appozttsb523729_h5_xiaoeknow_com=%7B%22distinct_id%22%3A%22u_627fb2138b256_vN5Ee1rW8H%22%2C%22first_id%22%3A%2218c378c26565c6-070d0cf3e894d3-16525634-2073600-18c378c2657733%22%2C%22props%22%3A%7B%7D%7D; logintime=1701741069; logintime=1701742365; shop_version_type=4'
_app = "appozttsb523729"

def download_pdf(url):
    url = url.replace(r'\/', '/')
    parsed_url = urlparse(url)
    file_name = urllib.parse.unquote(parsed_url.query).lstrip("download_name=")
    file_path = "./files/" + file_name
    headers = {
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"'
    }

    response = requests.request("GET", url, headers=headers, data={})
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(response.content)


def get_urls(resource_id):
    url = f"https://{_app}.h5.xiaoeknow.com/xe.course.business.courseware_list.get/2.0.0"

    payload = f'bizData%5Bresource_id%5D={resource_id}&bizData%5Bresource_type%5D=6&bizData%5Bcheck_available%5D=1'
    headers = {
        'authority': f'{_app}.h5.xiaoeknow.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': _cookie,
        'req-uuid': '20231205095115000300071',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()


def get_columns(lesson_id):
    url = f"https://{_app}.h5.xiaoeknow.com/xe.course.business.member.column_items.get/2.0.0"

    payload = f'bizData%5Bcolumn_id%5D={lesson_id}&bizData%5Bpage_index%5D=1&bizData%5Bpage_size%5D=50'
    headers = {
        'authority': f'{_app}.h5.xiaoeknow.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': _cookie,
        'origin': 'https://appozttsb523729.h5.xiaoeknow.com',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()


if __name__ == '__main__':
    columns = get_columns("p_61542cf6e4b0dfaf7fa8fbd7")
    for col in columns.get("data").get("list"):
        time.sleep(1)
        print(col.get("resource_title"))
        urls = get_urls(col.get("resource_id"))
        print(urls)
        for i_url in urls.get("data"):
            download_pdf(i_url.get("url"))
