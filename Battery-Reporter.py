import subprocess
import os
import webbrowser
output_path = os.path.join(os.getcwd(), "battery-report.html")
command = f'powercfg /batteryreport /output "{output_path}"'
subprocess.run(command, shell=True)
webbrowser.open(f"file:///{output_path}")


# Instal Work: # py -m pip install pyinstaller
# Work:  # py -m PyInstaller --onefile  Battery.AC.py
