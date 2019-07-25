import requests
import time
from datetime import datetime as dt
from bs4 import BeautifulSoup
from win10toast import ToastNotifier 
import os

toast = ToastNotifier()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


toast.show_toast("remindingYou", "Software was successfully installed... RESTART your PC now", duration = 15, icon_path = resource_path("icon.ico"))


def codeforces():
	link = "https://codeforces.com"
	cf = requests.get(link)
	
	soup = BeautifulSoup(cf.text, 'html.parser')
	countDown = soup.find('span', {'class':'countdown'}).get_text()

	div = soup.find('div', {'class':'roundbox sidebox'})
	contest_name = div.find('a').get_text()

	if countDown.find('d') == -1:
		hrs = int((countDown[0] + countDown[1]), 10)
		mins = int((countDown[3] + countDown[4]), 10)
		if hrs == 0 and (mins <= 10):
			toast.show_toast("CodeForces: ", contest_name +" is about to start", duration = 15, icon_path = resource_path("icon.ico"))


def codechef():
	link = "https://codechef.com/contests"
	cf = requests.get(link)

	today = dt.now()
	today = today.strftime("%d/%m/%Y %H:%M:%S")

	soup = BeautifulSoup(cf.text, 'html.parser')
	start_date = soup.find_all('td', {'class':'start_date'})[2].get_text()
	contest_name = soup.find_all('td')[10].get_text()

	if start_date[0] + start_date[1] ==  today[0] + today[1]:
		if start_date[13] + start_date[14] == today[11] + today[12]:
			if int(start_date[16] + start_date[17]) - int(today[14] + today[15]) <= 10:
				toast.show_toast("CodeChef: ", contest_name +" is about to start", duration = 15, icon_path = resource_path("icon.ico"))




def checkNet(i):
	if i == 0:
		toast.show_toast("remindingYou", "Checking for internet connection...", duration = 15, icon_path = resource_path("icon.ico"))
	try:
		response = requests.get("http://www.google.com")
		global j
		if j == False:
			toast.show_toast("remindingYou","Connected to the Internet", duration = 15, icon_path = resource_path("icon.ico"))
			j = True
		return True
	except requests.ConnectionError:
		if i % 7 == 0:
			toast.show_toast("remindingYou", "Check Your Internet connection -- Can't Sync", duration = 15, icon_path = resource_path("icon.ico"))
		return False

i = 0
j = False

while 1:
	is_net_working = checkNet(i)
	while is_net_working != True:
		time.sleep(5)
		print("NOT CONNECTED TO THE INTERNET...")
		i += 1
		j = False
		is_net_working = checkNet(i)
	i += 1
	print("Connected...")
	codeforces()
	codechef()

	time.sleep(180)