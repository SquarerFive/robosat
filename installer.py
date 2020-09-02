import os
with open("cinstaller.bat", "r") as f:
    a = f.read().split("\n")
for command in a:
    if pip not in command:
        os.system(command + " -y")
