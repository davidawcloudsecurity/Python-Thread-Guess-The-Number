import concurrent.futures
import time
import random
start = time.perf_counter()
#using for loop
global u_input
u_input = int(input("Number 0-100: "))

def do_something(name):
  print("Running %s\n" %name)
  for i in range(1,101):
    machine_number = random.randint(1, 100)
    if machine_number == u_input:
      print(f"Match", machine_number)
      break
    #print(i, 'second...', end='\r')
    print(i, 'second...', name, end = '\n')
    time.sleep(0.5)
  print("%s has finished execution\n" %name)

with concurrent.futures.ThreadPoolExecutor() as executor:
  f1 = executor.submit(do_something, "First Thread")
  f2 = executor.submit(do_something, "Second Thread")

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds(s)')
