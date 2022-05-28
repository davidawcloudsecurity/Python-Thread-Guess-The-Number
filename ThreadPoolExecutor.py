import concurrent.futures
import time
start = time.perf_counter()

def do_something(name):
  print("Running %s\n" %name)
  for i in range(1,11):
    print(i, 'second...', end='\r')
    time.sleep(1)
  print("%s has finished execution\n" %name)

with concurrent.futures.ThreadPoolExecutor() as executor:
  f1 = executor.submit(do_something, "First Thread")
  f2 = executor.submit(do_something, "Second Thread")

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds(s)')
