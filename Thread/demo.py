import concurrent.futures
import threading
import time
import csv
import sys, getopt 

#   Thread instructions
def routine():
    # run = time.perf_counter()   #   Timemark before runring thread
    try:
        threadLock.acquire()    #   Acquire lock
    except:
        pass
    # print(f'Running thread {index} ...\n')
    global count
    count += 1
    # print(f'Exitting thread {index} ...\n')
    try:
        threadLock.release()    #   Release lock
    except:
        pass
    # exit = time.perf_counter()  #   Timemark after runring thread
    # return run - t1, exit - run

#   Take command line arguments
if __name__ == "__main__":
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "hn:l:")
    except getopt.GetoptError:
        print("demo.py -n <Number of thread, 1000 by default> -l <y/n if enable thread lock, NO by default>")
        sys.exit(2)

    THREAD_NUMBER = 1000
    count = 0       #   Global variable
    lockEn = False  #   Enable thread lock
    timeValue = {
        "cre": 0,
        "run": 0,
    }  #   Period each thread stay in Created & Running State
    threadPool = []

    for opt, arg in opts:
        if opt == "-h":
            print("demo.py -n <Number of thread, 1000 by default> -l <y/n if enable thread lock, NO by default>")
            sys.exit()
        elif opt == "-n":
            THREAD_NUMBER = int(arg)
        elif opt == "-l": 
            if arg == "y":
                threadLock = threading.Lock()
                lockEn = True
    start = time.perf_counter() #Start the process

    with concurrent.futures.ThreadPoolExecutor() as exe:
        for i in range(THREAD_NUMBER):
            # print(f'Creating thread {i} ...\n')
            # t1 = time.perf_counter()    #   Timemark before creating a thread
            t = exe.submit(routine)           #   Create thread, abstracted
            threadPool.append(t)

        # for f in concurrent.futures.as_completed(threadPool):
        #     timeValue["cre"] += f.result()[0]
        #     timeValue["run"] += f.result()[1]

    # print(f'Number of threads: {count}\nAverage time in created state: {timeValue["cre"] / THREAD_NUMBER} (s), running state: {timeValue["run"] / THREAD_NUMBER} (s)')
    # if lockEn:
    #     print("Thread lock enabled.")
    # else:
    #     print("Thread lock unabled.")


    # #   CSV header
    # fieldnames = ['creState', 'runState']

    # with open('C:/Users/admin/Downloads/time.csv', 'w', encoding='UTF8', newline='') as f:
    #     writer = csv.DictWriter(f, fieldnames=fieldnames)
    #     writer.writeheader()
    #     writer.writerows(timeValue)

    # end = time.perf_counter()
    # print(f'Process run in {end - start} seconds.')
