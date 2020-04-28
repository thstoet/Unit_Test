from datetime import timedelta, datetime
import sys

class washer_calc:
	duration=0
	start=0
	set=0
	
	def __init__(self, hour_now, min_now, hour_fin, min_fin):
		self.hour_now=hour_now
		self.min_now=min_now
		self.hour_fin=hour_fin
		self.min_fin=min_fin
	
	def calc_standard(self):
		self.duration=timedelta(hours=1, minutes=16)
		self.start=(timedelta(hours=self.hour_fin, minutes=self.min_fin))-self.duration
		self.set=self.start-timedelta(hours=self.hour_now,minutes=self.min_now)
		if self.set < timedelta(hours=0, minutes=0):
			print("pow")
			sys.exit()
		else:
			return self.set.seconds
			
	def calc_def(self, hour_def, min_def):
		self.duration=timedelta(hours=hour_def, minutes=min_def)
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
	
	myCalc = washer_calc(datetime.now().hour, datetime.now().minute, h_fin, m_fin)
	
	wahl=input("Wie immer, oder eigene Eingabe (j/n)?")
	if wahl == "j":
		set_washer=myCalc.calc_standard()
	elif wahl == "n":
		print("Wie lange soll die Wäsche laufen?")
		h_def=int(input("Die Stunde bitte: "))
		m_def=int(input("Die Minute bitte: "))
		set_washer=myCalc.calc_def(h_def, m_def)
	else:
		print("Error")
		sys.exit()
	
	set_stnd_hours=change(set_washer)
	print("Vorwahl auf %s"%set_stnd_hours)
	
		
	

