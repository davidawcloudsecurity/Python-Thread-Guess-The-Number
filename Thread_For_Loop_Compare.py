import concurrent.futures
import time
import random

start = time.perf_counter()

global u_input, u_limit
u_limit = int(input("Enter limit: "))
u_input = int(input(f"Number 0-{u_limit}: "))

def do_something(name):
  print("Running %s\n" %name)
  
  for i in range(u_limit):
    if i == u_input:
      print("\nMatch")
      break
    print(i, 'second...', end = '\r')
    #time.sleep(1)
    i += 1
  print("%s has finished execution\n" %name)
    
with concurrent.futures.ThreadPoolExecutor() as executor:
  f1 = executor.submit(do_something, "First Thread")
  #f2 = executor.submit(do_something, "Second Thread")
  
finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds(s)')
