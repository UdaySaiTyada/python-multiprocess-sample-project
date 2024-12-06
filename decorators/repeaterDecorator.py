from time import sleep

def doTwice(func):
        def wrapper():
            func()
            sleep(1)
            print("Waited 1 seconds")
            func()
            pass
        return wrapper

@doTwice
def healthCheck():
    print("HEALTHY")

if __name__ == "__main__":
    healthCheck()