import requests
import time
from bs4 import BeautifulSoup
from win10toast import ToastNotifier 


toast = ToastNotifier()


def checkNet(i):
	print("Checking for internet connection...")
	try:
		response = requests.get("http://www.google.com")
		print("response code: ", response.status_code)
		return True
	except requests.ConnectionError:
		if i % 7 == 0:
			toast.show_toast("Internet Not Connected", "Can't Sync", duration = 10)
		return False

i = 0
while 1:
	is_net_working = checkNet(i)
	while is_net_working != True:
		time.sleep(5)
		i += 1
		is_net_working = checkNet(i)

	link = "https://codeforces.com"
	cf = requests.get(link)
	#print(f.text)

	soup = BeautifulSoup(cf.text, 'html.parser')
	countDown = soup.find('span', {'class':'countdown'}).get_text()

	div = soup.find('div', {'class':'roundbox sidebox'})
	stri = div.find('a').get_text()

	if countDown.find('d') == -1:
		hrs = int((countDown[0] + countDown[1]), 10)
		mins = int((countDown[3] + countDown[4]), 10)
		if hrs == 0 and (mins == 20 or mins <= 10):
			toast.show_toast("CodeForces", stri +" is about to start", duration = 10) 

	time.sleep(600)