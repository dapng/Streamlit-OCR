import os
import sys # System-specific parameters and functions


# start_tunnel = os.system('lt --port 8501 --subdomain ocrweb')


print('start tunnel')


def main():
    print('main func')
    pass

if __name__ == "__main__":
    if os.system('lt --port 8501 --subdomain ocrweb'):
        main() and print('go main')
    else:
        os.execv(sys.argv[0], sys.argv) and print('restart')