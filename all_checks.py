import os, sys, shutil

def check_disk_usage(disk, min_gb, min_percent):
    """Return True if there is enough free disk space, false otherwise"""
    du = shutil.disk_usage(disk)

    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30

    if percent_free < min_percent or gigabytes_free < min_gb:
        return False
    return True

def check_reboot():
    """Returns True if the computer has a pending reboot"""
    return os.path.exists('/run/reboot-required')

def check_root_full():
    """Return True if the root partition is full, False otherwise"""
    return check_disk_usage(disk='/', min_gb=2, min_percent=10)


def main():
    if check_reboot():
        print('Pending Reboot.')
        sys.exit(1)
    print(f'Everything ok')
    sys.exit(0)
    

if __name__ == '__main__':
    main()
    


