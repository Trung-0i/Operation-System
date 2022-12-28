import concurrent.futures
import threading
import time
import csv

start = time.perf_counter() #Start the process

THREAD_NUMBER = 1000

count = 0
timeValue = []  #   Period each thread stay in Created & Running State
threadPool = []
threadLock = threading.Lock()   


#   Thread instructions
def routine(index, t1):
    run = time.perf_counter()   #   Timemark before runring thread
    #threadLock.acquire()    #   Acquire lock
    print(f'Running thread {index} ...\n')
    global count
    count += 1
    time.sleep(0.01)
    print(f'Exitting thread {index} ...\n')
    #threadLock.release()    #   Release lock
    exit = time.perf_counter()  #   Timemark after runring thread
    return run - t1, exit - run

with concurrent.futures.ThreadPoolExecutor() as exe:
    for i in range(THREAD_NUMBER):
        print(f'Creating thread {i} ...\n')
        t1 = time.perf_counter()    #   Timemark before creating a thread
        t = exe.submit(routine, i, t1)  #   Create thread 
        threadPool.append(t)
    for f in concurrent.futures.as_completed(threadPool):
        value = {
            'creState': f.result()[0],
            'runState': f.result()[1]
        }
        timeValue.append(value)

#   CSV header
fieldnames = ['creState', 'runState']

with open('C:/Users/admin/Downloads/time.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(timeValue)

end = time.perf_counter()
print(f'Process run in {end - start} seconds.')
