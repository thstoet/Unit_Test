import logging

# basic confic default = warning. alles ab warning wird geloggt. Alles was drunter ist wird ignoriert. deshalb muss badic confi auf default runtergesetzt werden, damit alles logging level dargeszellt werden

logging.basicConfig(filename="test.log",level=logging.DEBUG)
logging.debug("Ich bin der Root Logger") #root logger

x=36
while x <= 41:
	if x <38:
		logging.info(x)
	elif x <39:
		logging.warning(x)
	elif x <41:
		logging.critical(x)
	x += 1
	
print("\n")
logger1 = logging.getLogger("Jakob", ) #eigener logger, nimmt aber auch bezug auf root logger config
logger1.debug("Ich bin der Jakob Logger", )

x=36.7
while x <= 41:
	if x <38:
		logger1.info(x)
	elif x <39:
		logger1.warning(x)
	elif x <41:
		logger1.critical(x)
	x += 1

	