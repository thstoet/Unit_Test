import logging
import random
import re

logging.basicConfig(filename="Generator_Log.log", level=logging.DEBUG,
                    format="%(levelname)s - %(name)s - %(message)s")

myLogger = logging.getLogger("Generator")

class Generator_Log:


    def random_Level(self):
        self.rnd_Lvl = random.randint(0,2)
        if self.rnd_Lvl == 0:
            myLogger.debug("Message")
        elif self.rnd_Lvl == 1:
            myLogger.warning("Message")
        elif self.rnd_Lvl == 2:
            myLogger.error("Message")

    def generate_log_entries(self):
        for i in range(0,50):
            self.random_Level()

class Log_scanner:

    def scan_Warning(self):
        with open("Generator_Log.log") as lg:
            for line in lg:
                self.sc = re.findall(r"WARNING", line)
                if self.sc:
                    print("Warning detected")

    def scan_Error(self):
        with open("Generator_Log.log") as lg:
            for line in lg:
                self.sc = re.findall(r"ERROR", line)
                if self.sc:
                    print("Error detected")

    def scan_Counter(self):
        with open("Generator_Log.log") as lg:
            self.patter=re.compile("WARNING|ERROR")
            self.count=0
            for line in lg:
                self.scan=self.patter.findall(line)
                self.count+=1
            if self.count>0:
                print("{} x Warning or Error".format((self.count)))
        return self.count


if __name__ == "__main__":
    myGenerator = Generator_Log()
    myScanner = Log_scanner()

    print("Write Log File")
    myGenerator.generate_log_entries()

    print("Scan Warnings")
    myScanner.scan_Warning()

    print("Scan Errors")
    myScanner.scan_Error()

    print("Count Highlights")
    myScanner.scan_Counter()
