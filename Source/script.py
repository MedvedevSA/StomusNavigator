#script.py
import subprocess


ui_name = "ui_main.ui"
py_name = "ui_main.py"

def convert ():
    subprocess.Popen(f"pyside2-uic {ui_name} -o {py_name}")


def test():
    db = {  1:"01",
            2:"02",
            3:"03"}

    name = "Номер один"
    tmp_df = {}
    tmp_df[name] = db[1]
    print(tmp_df) 

test()
