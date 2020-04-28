from datetime import timedelta, datetime
import sys

class washer_calc:
	duration=0
	start=0
	set=0
	
	def __init__(self, hour_now, min_now, hour_fin, min_fin, hour_def, min_def):
		self.hour_now=hour_now
		self.min_now=min_now
		self.hour_fin=hour_fin
		self.min_fin=min_fin
		self.hour_def=hour_def
		self.min_def=min_def
	
			
	def calc_def(self):
		self.duration=timedelta(hours=self.hour_def, minutes=self.min_def)
		self.start=(timedelta(hours=self.hour_fin, minutes=self.min_fin))-self.duration
		self.set=self.start-timedelta(hours=self.hour_now,minutes=self.min_now)
		if self.set < timedelta(hours=0, minutes=0):
			print("pow")
			sys.exit()
		else:
			return self.set.seconds

def change(c):
	str_c=str(c/float(3600))
	h=str_c[0]
	m=int(str_c[2:4])
	min=str(m/100*60)
	set= h + ":" + min[0:2]
	min_index = min[1]	
	if min_index is None:
		set= h + ":" + min[0]
	return set
	
	
if __name__ == "__main__":
	
	print("Wann soll die Wäsche fertig sein?")
	h_fin=int(input("Die Stunde bitte: "))
	m_fin=int(input("Die Minute bitte: "))
	
	myCalc_eco = washer_calc(datetime.now().hour, datetime.now().minute, h_fin, m_fin, 1, 50)
	
	myCalc_wolle=washer_calc(datetime.now().hour, datetime.now().minute, h_fin, m_fin, 2, 30)
	
	myCalc_koch=washer_calc(datetime.now().hour, datetime.now().minute, h_fin, m_fin, 3, 40)
	
	Programm=(myCalc_eco.calc_def(), myCalc_wolle.calc_def(), myCalc_koch.calc_def())
	
	wahl=input("Wähle ein Programm! (E)co, (W)olle, (K)och")
	if wahl == "e":
		x=0
	elif wahl == "w":
		x=1
	elif wahl =="k":
		x=2
	else:
		print("Error")
		sys.exit()
	
	set_washer=Programm[x]
	
	set_stnd_hours=change(set_washer)
	print("Vorwahl auf %s"%set_stnd_hours)
	
		
	

