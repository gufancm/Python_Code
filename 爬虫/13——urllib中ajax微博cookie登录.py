import urllib.request

url = 'https://weibo.cn/6451491586/info'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}
data = {
#     ':authority':'weibo.com',
# '    :method':'GET',
# '    :path':'/',
# '    :scheme':'https',
'    accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
# '    accept-encoding':'gzip, deflate, br',
'    accept-language':'zh-CN,zh;q=0.9,en;q=0.8',
'    cache-control':'max-age=0',
'    cookie':'wb_view_log=1536*8641.25; SINAGLOBAL=4788586119490.992.1679373422041; ULV=1679392930131:2:2:2:9049400847648.924.1679392930129:1679373422045; SCF=Ar0I4yudmc2I8DtmGZwRbwlB0OXUscnAiTuOn82_Up4R5z5Itg1l9IXo5sLqJeA-1_Sll5qIz1Wh0dxzkFL6NnI.; ALF=1681998064; SUB=_2A25JHcOgDeRhGeFG6VER9SbJwzqIHXVq4e3orDV8PUJbkNANLWbHkW1NfhzjyXueUQNLwEcCPR-esoQCug2TxmYS; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFXC9Xw631-PcxeKEa1N8I_5JpX5oz75NHD95QN1hz0eh-RSKncWs4Dqcj-i--4i-2pi-i8i--fiKnNi-2pU02t; XSRF-TOKEN=0_ReahUyNA1EUlZxzm4SdCuQ; WBPSESS=Dt2hbAUaXfkVprjyrAZT_M1_rklbfg1Ay403l2aPp7KbAGWti-8Cy_f6BSSsE4UstVFB5s-CLeaVZQE_nAEeuR708yCNTy7gKbSgusWUn4moaDioM_mPIkayO9ZgYnxfh94fRdJ6t0-0kYgv-pd9ruGkMP7ksr3isLUwQ_JzMNJjgsE6imLPm3r4MXqUlo2jATCH44q_iCvjprvi-HC5UA==',
'    referer':'https://www.baidu.com/',
'    sec-ch-ua':'"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
'    sec-ch-ua-mobile':'?0',
'    sec-ch-ua-platform':'"Windows"',
'    sec-fetch-dest':'document',
'    sec-fetch-mode':'navigate',
'    sec-fetch-site':'same-origin',
'    sec-fetch-user':'?1',
'    upgrade-insecure-requests':'1',
}
request = urllib.request.Request(url=url,data=data,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('gb2312')
with open('weibo.html', 'w', encoding='utf-8') as df:
    df.write(content)