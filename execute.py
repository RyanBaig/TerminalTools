import subprocess
from sys import argv

path = "./commands.py"
subprocess.run(["python", path] + argv[1:])