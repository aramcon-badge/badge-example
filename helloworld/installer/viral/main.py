import os
from tools.uiutils import alert
from tools import copyfloppy

def install():
    print("starting installation")
    copyfloppy.copyfloppy('/apps/helloworld2')
    alert("Finished installing helloworld!")
    print("finished installation")

print("running installation")
install()
