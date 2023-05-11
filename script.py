import bs4 as bs
from requests.api import request
import requests
import sys

# ssl._create_default_https_context = ssl._create_unverified_context
# conn = http.client.HTTPSConnection("kvpy.iisc.ernet.in")

url = "http://kvpy.iisc.ac.in/kvpy.Twenty/checkMarksSuccess.php"
HEADERS = {
	'Upgrade-Insecure-Requests': '1',
	'Content-Type': 'application/x-www-form-urlencoded',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'Cookie': 'PHPSESSID=bstn1i2hqr9b0r36vgpcgtu2u3'
}

def get_marks(ID):
	for month in range(1,13):
		for day in range(1, 32):
			payload=f"dd={str(day).zfill(2)}&id={ID}&mm={str(month).zfill(2)}&yyyy=2003"
			print(f"Day: {day} Month: {month}\r", end="")

			response = requests.request("POST", url, headers=HEADERS, data=payload)
			# data = response.read().decode("utf-8")
			soup = bs.BeautifulSoup(response.text, 'html.parser')

			try:
				marks = float(soup.find_all(class_="result_right")[-1].text.strip()[2:])
				return marks
			except:
				pass


def main():

	if len(sys.argv) < 2:
		print("Usage: python3 script.py [APPLICATION_NUMBER]")
		return
	
	ID = int(sys.argv[1])

	marks = get_marks(ID)
	print()
	print(f"Marks Obtained: {marks}", end="")

if __name__== "__main__":
	main()