import threading
import time

def print_numbers():
    for i in range(1,6):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for letter in 'abcde':
        print(f"Letter: {letter}")
        time.sleep(1.5)

s = time.time()
# Without threading, this will take 12.55s
# print_numbers()
# print_letters()

# Using threading, this will take about 7.52s
t1 = threading.Thread(target=print_numbers)  # Create a thread for printing numbers
t2 = threading.Thread(target=print_letters)  # Create a thread for printing letters
t1.start()  # Start the first thread
t2.start()  # Start the second thread
t1.join()  # Wait for the first thread to finish
t2.join()  # Wait for the second thread to finish

print(f"Time taken without threading: {time.time() - s:.2f} seconds")
"""
    print_numbers()
    print_letters()
    와 비교했을 때, 스레드가 많을수록 여러가지 작업이 있을 때 더 단축됨.
"""


# basic threading example
# import threading

# class MyThread(threading.Thread):
#     def run(self):
#         print("working in thread:")
# t = MyThread()
# t.start()
# t.join()  # Wait for the thread to finish

# functional version
# def worker():
#     print("working in thread function")
# t = threading.Thread(target=worker)  # Create a thread with the worker function
# t.start()