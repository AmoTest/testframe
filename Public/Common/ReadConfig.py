
from configparser import ConfigParser
import os

class ReadConfig:

    def __init__(self, filename):

        self.config = ConfigParser()
        self.config.read(filename)

    def getConfigValue(self, section, option):

        configValue = self.config.get(section, option)
        return configValue


if __name__ == "__main__":

    file = os.path.dirname(os.path.abspath('./..')) + '/Config/config.ini'
    print(file)

    config = ReadConfig(file)
    value = config.getConfigValue('environment', 'url')
    print(value)


