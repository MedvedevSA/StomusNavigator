#script.py
import subprocess


ui_name = "ui_main.ui"
py_name = "ui_main.py"

subprocess.Popen(f"pyside2-uic {ui_name} -o {py_name}")
