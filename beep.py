import winsound
from playsound import playsound
from pygtail import Pygtail
import sys
while True:
	try:
		for line in Pygtail(sys.argv[1]):
			if "+CEREG: 0" in line:
				print("+CEREG: 0")
				#winsound.Beep(3000,2000)
				playsound("Cereg0.wav")
			elif "+CEREG: 1" in  line:
				print("+CEREG: 1")
				playsound("Cereg1.wav")
			elif "+CEREG: 2" in  line:
				print("+CEREG: 2")
				playsound("Cereg2.wav")
			elif "+CEREG: 3" in  line:
				print("+CEREG: 3")
				playsound("Cereg3.wav")
			elif "+CEREG: 4" in  line:
				print("+CEREG: 4")
				playsound("Cereg4.wav")
	except UnicodeDecodeError:
		pass; 