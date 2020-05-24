#from mymodule import my_func

#mymodule_func()

# Now importing from a package
from MyMainPackage import some_main_script
# Importing functions within a sub directory
from MyMainPackage.SubPackage import mysubscript

some_main_script.report_main()

mysubscript.sub_report()

print("Name in myprogram.py")
print(__name__)