import subprocess
from sys import argv
import os

path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'commands.py'))
subprocess.run(["python", path] + argv[1:])