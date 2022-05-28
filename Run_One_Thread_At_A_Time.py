import threading
import time
#Try to understand how thread works
#This code only runs one thread at a time
start = time.perf_counter()

global u_input
u_input = int(input("Number 0-100: "))

def do_something(name, start1, limit1):
  print("Running %s\n" %name)
  for i in range(start1,limit1):
    if i == u_input or u_input < start1:
      break
    print(i, 'second...', u_input, end='\r')
    time.sleep(0.5)
  print("%s has finished execution\n" %name)

t1 = threading.Thread(target=do_something("First Thread",1, 51))
t2 = threading.Thread(target=do_something("Second Thread",51,101))

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds(s)')
