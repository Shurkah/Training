import os
import subprocess

# os.system('ls')

subprocess.run(['ls', '-l', 'README.md'])

command = 'ps'
argument = '-x'


subprocess.run([command, argument])