import threading
import time
start = time.perf_counter()

def do_something(name):
  print("Running %s\n" %name)
  for i in range(1,11):
    print(i, 'second...', end='\r')
    time.sleep(1)
  print("%s has finished execution\n" %name)

t1 = threading.Thread(target=do_something("First Thread",))
t2 = threading.Thread(target=do_something("Second Thread",))

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds(s)')
