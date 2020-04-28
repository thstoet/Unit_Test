import logging

logging.basicConfig(filename="log.txt", level=logging.INFO) # root Logger

logger = logging.getLogger("meinLogger") # neuen logger basteln
logger.setLevel(logging.DEBUG)

fileh = logging.FileHandler("logme.txt") # FileHandler und Formatter erstellen
form = logging.Formatter('%(name)s - %(levelname)s : %(asctime)s - %(message)s')

fileh.setFormatter(form)    # Formatter dem Filehandler zweisen
logger.addHandler(fileh)    # Alles unserem Logger zuweisen

logger.debug("Was fuer eins Debug")     # meinLogger

logging.info("info fur root")           # rootlogger
logging.error("error")