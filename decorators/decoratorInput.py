
def repeat(times):
    def decorator(func):
        def wrapper():
            for i in range(times):
                func()
            pass
        return wrapper
    return decorator

@repeat(5)
def doJob():
    print("Job done")

if __name__ == "__main__":
    doJob()