import logging

def logging_test():
    logger1 = logging.getLogger("logger1")
    logger1.setLevel(logging.DEBUG)

    handler1 = logging.StreamHandler()
    handler1.setLevel(logging.DEBUG)

    formatter1 = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler1.setFormatter(formatter1)

    logger1.addHandler(handler1)

    logger1.debug("this is debug message")
    logger1.info("this is info message")
    logger1.warn("this is warn message")
    logger1.error("this is error message")
    logger1.critical("this is critical message")
    print(logging.root)
    print(logging.getLogger())
    print(logging.root.handlers)
    print(logging.lastResort)
    print(logger1.parent)

if __name__ == "__main__":
    logging_test()
