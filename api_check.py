from smsboom import load_json
import httpx
import json

def api_json_check():
    """
    用于测试api.json文件的接口
    """
    api_json_file = load_json()
    for i in api_json_file:
        data = i.handle_API('15259840022')  # 接码平台的号码 无所谓
        try:
            with httpx.Client(verify=False) as client:
                if data.method == 'POST':
                    res = client.post(url=data.url, headers=data.header, data=data.data)
                else:
                    res = client.get(url=data.url, headers=data.header, params=data.data)
                text = res.text.replace("\n", "")
                if r'\u' in res.text:
                    text = text.encode('utf-8').decode('unicode_escape')
                print(f'名称：{data.desc},接口状态：{res.status_code},接口内容：{text}')
        except Exception as e:
            print(f'名称：{data.desc},接口链接:{data.url},接口报错信息:{e}')


def check_url():
    """
    懒人测试单链接 因为懒得开接口
    F12看到接口之后右键复制curl格式复制
    在此网站可以一键格式化成请求代码 https://curlconverter.com/
    然后 将import requests删除 requests.get 改为httpx即可 这两个请求库代码几乎兼容
    """
    cookies = {
        'ASP.NET_SessionId': 'ctmgege3wvxlesdsansqvski',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': 'ASP.NET_SessionId=ctmgege3wvxlesdsansqvski',
        'Pragma': 'no-cache',
        'Referer': 'http://www.cnppump.ltd/Register/RegisterByTel.aspx',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    params = {
        'cmd': 'GetTelVerifyCode4Regit2',
        'Tel': 'xxxxxx',
        'SoftType': 'Web',
        '_': 'xxxxx',
    }

    response = httpx.get(
        'http://www.cnppump.ltd/Service/UserHandler.ashx',
        params=params,
        cookies=cookies,
        headers=headers,
        verify=False,
    )
    print(response.text)


if __name__ == '__main__':
    """
    用于快速测试接口状态
    """
    api_json_check()
    # check_url()
