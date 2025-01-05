import threading
import time
t=time.time()
def add(num):
    sum1=0
    for i in num:
        sum1+=i
        time.sleep(0.1)
        print("t1")
    print(sum1)

def mul(num):
    mull=1
    for i in num:
        mull*=i
        time.sleep(0.2)
        print("t2")
    print(mull)

# Create thread instances properly
arr=[10,20,30,40,50,60]
t1 = threading.Thread(target=add, args=(arr,))
t2 = threading.Thread(target=mul, args=(arr,))

# Start the threads
t1.start()
t2.start()

# Wait for threads to complete
t1.join()
t2.join()
print(time.time()-t)