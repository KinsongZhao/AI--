import datetime
import logging


class SingletonLogger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingletonLogger, cls).__new__(cls, *args, **kwargs)
            cls._instance._setup_logger()
        return cls._instance

    def _setup_logger(self):
        # 创建一个 logger 对象
        self.logger = logging.getLogger("my_logger")

        # 设置日志级别
        self.logger.setLevel(logging.DEBUG)

        log_filename = datetime.datetime.now().strftime("%Y-%m-%d_%H.txt")
        # 创建文件处理器，将日志写入到文件
        file_handler = logging.FileHandler(log_filename, encoding='utf-8')

        # 创建控制台处理器，将日志输出到控制台
        console_handler = logging.StreamHandler()

        # 创建日志格式器
        # 创建一个格式化器，用于定义日志的格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # 将格式器添加到处理器
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # 将处理器添加到 logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger
