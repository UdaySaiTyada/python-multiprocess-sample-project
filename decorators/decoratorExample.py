from datetime import datetime
from time import sleep

def timeLog(func):
    def wrapper():
        print(datetime.now().time())
        func()
        print(datetime.now().time())
    pass
    return wrapper

@timeLog
def operation():
    sleep(5)
    print("The operation is done")
    pass



if __name__ == '__main__':
    operation()