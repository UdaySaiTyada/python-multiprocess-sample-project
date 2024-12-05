from multiprocessing import Process

def printNumbersWith100(start, end):
    for i in range(start, end + 1):
        if(i % 100 != 0):
            continue
        print(i)
    print(f"Task completed {start} to {end}")


if __name__ == "__main__":
    processes = []

    limits = [[1, 10000], [200000, 203000], [300000, 300100]]

    for limit in limits:
        process = Process(target=printNumbersWith100, args=(limit[0], limit[1]))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()

