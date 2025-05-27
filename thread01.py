# basic threading example
import threading

class MyThread(threading.Thread):
    def run(self):
        print("working in thread:")
t = MyThread()
t.start()
t.join()  # Wait for the thread to finish

# functional version
def worker():
    print("working in thread function")
t = threading.Thread(target=worker)  # Create a thread with the worker function
t.start()