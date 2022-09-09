import subprocess
subprocess.run("pyinstaller -F -w -i icon.ico main.py", shell=True)