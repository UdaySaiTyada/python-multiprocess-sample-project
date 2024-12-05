from multiprocessing import Process

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")

if __name__ == '__main__':
    p = Process(target=print_numbers)  # Define the process
    p.start()  # Start the process
    p.join()   # Wait for the process to finish
    print("Main process finished.")