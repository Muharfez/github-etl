import logging

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            logger = logging.getLogger("app_logger")
            logger.setLevel(logging.DEBUG)

            if not logger.handlers:
                ch = logging.StreamHandler()
                ch.setLevel(logging.INFO)
                
                fh = logging.FileHandler("application.log", mode='w')
                fh.setLevel(logging.DEBUG)

                formatter = logging.Formatter(
                    "%(asctime)s - %(levelname)s - %(message)s",
                    "%Y-%m-%d %H:%M:%S"
                )
                
                ch.setFormatter(formatter)
                fh.setFormatter(formatter)

                logger.addHandler(ch)
                logger.addHandler(fh)

            cls._instance.logger = logger
        return cls._instance

    def get_logger(self):
        return self.logger