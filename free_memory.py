from psutil import virtual_memory
from math import floor

def check_free_memory():
    memory = virtual_memory()
    BYTES_IN_GIGABYTE = 1000000000

    totalMemoryInBytes = memory.total
    totalMemoryInGB = floor(totalMemoryInBytes / BYTES_IN_GIGABYTE)
    freeMemoryInBytes = memory.free
    freeMemoryInGB = freeMemoryInBytes / BYTES_IN_GIGABYTE


    print(f'Total physical memory available: {totalMemoryInGB}GB')
    print(f'Free physical memory available: {freeMemoryInGB}GB')

if __name__ == '__main__':
    check_free_memory()



