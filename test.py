import requests

url = "http://kvpy.iisc.ac.in/kvpy.Twenty/checkMarksSuccess.php"

payload='dd=08&id=20073462&mm=07&yyyy=2004'
headers = {
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Cookie': 'PHPSESSID=mn48i8qot8sld669s2n9boran7'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
