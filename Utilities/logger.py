import logging


class Logclass:
    def get_logs(self):
        logger = logging.getLogger()
        filehandler = logging.FileHandler("D:\\Dev_Progs\\selenium\\selenium_demo2\\Logs\\logfile.log", mode="w")
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s',datefmt='%d/%m/%Y %I:%M:%S %p')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        logger.debug("Test started")
        return logger
