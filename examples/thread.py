import threading
import time

class SharedDataSafe:
    count = 0  # Shared class variable
    lock = threading.Lock()  # Thread-safe lock

    @classmethod
    def increment(cls):
        with cls.lock:  # Ensure only one thread modifies at a time
            cls.count += 1

# Function to run in multiple threads
def worker():
    for _ in range(10000):
        SharedDataSafe.increment()
    time.sleep(60)

# Running the same threaded test
threads = [threading.Thread(target=worker, name=f'My-Worker-{i}') for i in range(10)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print(SharedDataSafe.count)  # Output: 100000 (Correct!)
