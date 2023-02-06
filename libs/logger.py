import logging

def init_logger(level: int):
    log = logging.getLogger("my-api")
    FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(format=FORMAT, level=level)

