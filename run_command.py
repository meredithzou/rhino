import subprocess

process = subprocess.Popen("Z:\\tmp/rhino.exe Z:\\tmp/a Z:\\tmp/bdc")
process.wait()
print process.returncode

# import os

# os.system("Z:\\tmp/rhino.exe Z:\\tmp/a Z:\\tmp/bdc")
