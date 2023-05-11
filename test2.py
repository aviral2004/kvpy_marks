import http.client

conn = http.client.HTTPSConnection("kvpy.iisc.ac.in")
payload = 'dd=08&id=20073462&mm=07&yyyy=2004'
HEADERS = {
	'Upgrade-Insecure-Requests': '1',
	'Content-Type': 'application/x-www-form-urlencoded',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'Cookie': 'PHPSESSID=bstn1i2hqr9b0r36vgpcgtu2u3'
}
conn.request("POST", "/kvpy.Twenty/checkMarksSuccess.php", payload, HEADERS)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))