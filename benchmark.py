import os
import ss
import psutil
import time

print("Software Secret Sharing Benchmark System---------------")
process = psutil.Process(os.getpid())
start  = time.time()
string = input("Enter a 10 word string : ")
ss.main(string)
end= time.time()
print("Maximum memory requirement : ",process.memory_info().rss) 
print("Time Taken : ",end-start)
ss.main()
