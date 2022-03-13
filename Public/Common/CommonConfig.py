
from datetime import datetime

def getCurrentTime():

    fmt = "%a %b %d %H:%M:%S %Y"
    return datetime.now().strftime(fmt)

print(getCurrentTime())