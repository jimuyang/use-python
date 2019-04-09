import requests

url = "https://www.toutiao.com/api/pc/feed/"

querystring = {"category":"news_hot","utm_source":"toutiao","widen":"1","max_behot_time":"0","max_behot_time_tmp":"0","tadrequire":"true"}

payload = ""
headers = {
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    'content-type': "application/x-www-form-urlencoded",
    'accept': "text/javascript, text/html, application/xml, text/xml, */*",
    'authority': "www.toutiao.com",
    'cache-control': "no-cache",
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)