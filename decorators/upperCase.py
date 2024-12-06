def capitalize(func):
    def wrapper():
        value = func()
        return str.upper(value)
    return wrapper

@capitalize
def name():
    return "uday"

if __name__ == "__main__":
    print(name())