import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s | %(levelname)s :  - %(message)s")

file_handler = logging.FileHandler("clac_advanced.log")
file_handler.setLevel(logging.ERROR)  #Es werden nur Errors geloggt
file_handler.setFormatter(formatter)  #Log Inhalte werden in Konsole angezeigt

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add(x, y):
    return x + y

def div(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        #logger.error("Tried to devide by zero")
        logger.exception("Tried to devide by zero") #So werden noch trace back infos im log gezeigt
    else:
        return result

def div2(x, y):
    if y == 0:
        raise ValueError("Can not devide by zero!")
    return x/y

if __name__ == "__main__":

    num_1 = 5
    num_2 = 0

    add_result = add(num_1, num_2)
    logger.debug("Add: {} + {} = {}".format(num_1, num_2, add_result))

    div_result = div(num_1, num_2)
    logger.debug("Div: {} / {} = {}".format(num_1, num_2, div_result))