
def handleException(func):
    def wrapper(*args, **kwargs):
        value = None
        try:
            value = func(*args, **kwargs)
        except Exception as e:
            print("Exception raised")
        return value
    return wrapper

@handleException
def divide(a, b):
    return a/b

if __name__ == "__main__":
    print(divide(10, 2))
    print(divide(10, 0))