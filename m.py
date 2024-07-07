# Import the 'os' module to work with the operating system.
import os
# Use the 'os.path.realpath(__file__)' to get the full path of the current Python script.
# This will print the path of the current file.
print("Current File Name: ", os.path.realpath(__file__))
# Import the 'multiprocessing' module to work with multi-processing features.
import multiprocessing

# Use 'multiprocessing.cpu_count()' to determine the number of available CPU cores.
cpu_count = multiprocessing.cpu_count()

# Print the number of CPU cores available on the system.
print(cpu_count)

