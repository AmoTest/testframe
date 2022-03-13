
import logging
import os
import time

"""
logging提供四大组件实现日志处理：
    1.logger：日志器，提供应用程序代码直接使用的接口
    2.handler：处理器，用于将日志记录发送到指定的目的位置
    3.filter：过滤器，用于决定哪些日志将会被输出
    4.formatter：格式器，用于控制日志信息最终输出的格式

一个事件通常需要以下内容：
    1.事件发生的具体事件
    2.事件发生的位置
    3.事件发生的严重程度（日志级别）
    4.事件的具体内容

logging.baseConfig(filename="log.log", level=logging.INFO)  # 将日志输出到log.log文件中
"""

class Log:

    def __init__(self, LogFile, CmdLevel=logging.INFO, FileLevel=logging.INFO):

        self.logger = logging.getLogger(LogFile)
        self.logger.setLevel(logging.DEBUG)

        fmt = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

        #设置控制台日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(CmdLevel)

        #设置文件日志
        fh = logging.FileHandler(LogFile)
        fh.setFormatter(fmt)
        fh.setLevel(FileLevel)

        #给logger添加handler
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)


if __name__ == "__main__":

    timeInfo = time.strftime("%Y%m%d%H%M%S", time.localtime())
    logFile = os.path.dirname(os.path.abspath('./..')) + f'/Report/Log/{timeInfo}.log'

    logger = Log(logFile)
    logger.info("This is info information")
