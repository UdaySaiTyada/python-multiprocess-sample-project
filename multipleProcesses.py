from multiprocessing import Process

def printNumbers(start, end):
    for i in range(start, end + 1):
        print(i)
    pass

limits = [[1, 1000], [2000, 2250], [3000, 3400]]
if __name__ == "__main__":
    processes = []

    for limit in limits:
        process = Process(target=printNumbers, args=(limit[0], limit[1], ))
        processes.append(process)
        process.start()
        
    for process in processes:
        process.join()