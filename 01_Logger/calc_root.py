import logging


logging.basicConfig(filename="basic_1.log", level=logging.DEBUG,
                    format="%(asctime)s - %(name)s | %(levelname)s :  - %(message)s")


def add(x, y):
    return x + y


if __name__ == "__main__":

    num_1 = 5
    num_2 = 3

    add_result = add(num_1, num_2)
    logging.debug("Add: {} + {} = {}".format(num_1, num_2, add_result))
