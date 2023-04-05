import urllib.request
import json
import urllib.parse
url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
headers = {
    'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Acs-Token': '1677402009280_1677419084451_ytrXK5TP73qFD/LLXLE0Eevx+oyOH5IvDdnQiZ4EWFthHn4owL7cL6WvT1kKln9tGxJFy6JlPjRV+maqErGg3d4SivgvGd1OXJr837a7dfvQGmc7i8UqseXq4BHnIn0cOr2O1JamUxt/XT3kf/e0JTrQu627td9cdGQLb2yuQ+yo8nz0KZZAVug3DAa/7ziBM9/9bWo2VxsVL+XRJ+BfFo6SyAfBCANdHsbdGLpiU3igZPDYfIrtG1dZboRsnWCUTsgLUUXHmpZfeC7EAwsTPQyRbGRgw8vZmzZ54J8VIlHIleyuxUUYwqBkbl7oAcqruRnPTv4a6UJ+wwqoQIvQ7Q==',
    'Connection': 'keep-alive',
    'Content-Length': '135',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BAIDUID=24446F2215BE675B7F3024CD44141A70:FG=1; BAIDUID_BFESS=24446F2215BE675B7F3024CD44141A70:FG=1; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1677418920; BIDUPSID=24446F2215BE675B7F3024CD44141A70; PSTM=1677418972; BDRCVFR[AhpjB_mUdht]=D7T3OLhzhM6IAd_n1mdQhPEUf; BA_HECTOR=8k2l05ah0g250ka08kag2k771hvmofn1k; ZFY=TsW2H:BNgeKwrNeRpsBzjZdqDC7Bo:BCYYMweDrb8diJg:C; BDRCVFR[S4-dAuiWMmn]=XrdtJXujCbbfjn3njnvrHnvg1wxpA7E; delPer=0; PSINO=5; H_PS_PSSID=; ab_sr=1.0.1_YjZkZGYxMDc1YzQ3MTBjZWMzNjZiNWM5NTEwZTI3MTI1ZGI2ZGY4YzFmOGVhMjZjZjJjN2I5NmEyZjgyYjZiNmY1NzdmYzFlOWZhYzUyNmNhNTY4M2ZiM2ZkNDAxYjhmNDM2YWMzM2RkMTcwYjZjMTkyYmZlODM1ZWI4MDUxZTlmMjU2YzBlNmVlM2FhM2VhYWVlYmU1Mjk0Mjc3ZTc4OA==; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1677419008',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'Windows',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
data = {
    'from': 'en',
    'to': 'zh',
    'query': 'love',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '198772.518981',
    'token': 'c90ff4432db71b67d37d0bb328881679',
    'domain': 'common'
}
data = urllib.parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(url=url, data=data, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
obj = json.loads(content)
print(obj)