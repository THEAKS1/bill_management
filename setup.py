from cx_Freeze import setup, Executable

base = None    

executables = [Executable("sms2.py", base=base)]

packages = ["idna","PyQt5","datetime","reportlab","mysql","images"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Bill_management",
    options = options,
    version = "1.0",
    description = 'Creates bill',
    executables = executables
)