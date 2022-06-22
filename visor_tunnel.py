import os, sys, fileinput
from subprocess import run
from time import sleep


file_path = "tunnel.py" 

restart_timer = 2


if not os.system("tunnel.py"):
    sleep(restart_timer)
    run("python "+file_path, check=True)
