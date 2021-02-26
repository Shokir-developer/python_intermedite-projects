import time
from datetime import datetime
from playsound import playsound

hour = int(input("enter hour: "))
minute = int(input("enter minute: "))
alarmtime = f"{hour}:{minute}"

while True:
	nowtime = datetime.now().strftime('%H:%M')
	if nowtime == alarmtime:
		playsound("Music.wav")
		print("Wake up")
		break
	else:
		print("not yet")
		time.sleep(10)