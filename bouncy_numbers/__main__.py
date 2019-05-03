import time

from .core import find_least_bouncy_number

time_started = time.time()
resp = find_least_bouncy_number()
time_to_find = time.time() - time_started
print("Least number found at {}% proportion = {}".format(resp[1], resp[0]))
print("Time to find: [%0.2fs]" % time_to_find)
