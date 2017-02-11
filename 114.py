import requests
import json

s = requests.session()
headers={
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
    'Origin': 'http://114yeah.com',
    'Referer': 'http://114yeah.com/index/speedup.html',
    'X-Requested-With': 'XMLHttpRequest',
}
r = s.get("http://114yeah.com/index/sign.html", headers=headers)
if (r.status_code != 200):
    r.raise_for_status()
print(s.cookies['PHPSESSID'])
r = s.post('http://114yeah.com/index/encrypchar.html', data={}, headers=headers)
if (r.status_code != 200):
    r.raise_for_status()
j = json.loads(r.text)
print(j)
r = s.get('http://61.160.183.220/jsts/ebit/start', params={'k': j}, headers=headers)
if (r.status_code != 200):
    r.raise_for_status()
j = json.loads(r.text)
if(j['code']=='0'): print("提速成功")
elif(j['code']=='-30000'):  print("提速失败")
elif(j['code']=='-21502'):  print("您未签约")
elif(j['code']=='-21523'):  print("已处于提速状态")
else:  print("加速失败")
print (json.dumps(j))
