import os, sys, shutil

def check_disk_usage(disk, min_absolute, min_percent):
    """Return True if there is enough free disk space, false otherwise"""
    du = shutil.disk_usage(disk)

    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30

    if percent_free < min_percent or gigabytes_free < min_absolute:
        return False
    return True

def check_reboot():
    """Returns True if the computer has a pending reboot"""
    return os.path.exists('/run/reboot-required')


def main():
    if check_reboot():
        print('Pending Reboot.')
        sys.exit(1)
    print(f'Everything ok')
    sys.exit(0)
    

if __name__ == '__main__':
    main()
    


