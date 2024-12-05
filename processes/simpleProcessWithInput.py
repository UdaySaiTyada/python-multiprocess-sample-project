from multiprocessing import Process

def printNumbers(start, end):
    for i in range(start, end + 1):
        print(i)
    pass

if __name__ == '__main__':
    process = Process(target=printNumbers, args=(1,10,))
    process.start()
    process.join()