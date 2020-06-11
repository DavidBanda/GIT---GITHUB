import os

def check_reboot():
    """Returns True if the computer has a pending reboot"""
    return os.path.exists('/run/reboot-required')

def main():
    print(f'Hello Git from {__name__}')
    

if __name__ == '__main__':
    main()
    


