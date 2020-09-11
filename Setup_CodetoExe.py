from cx_Freeze import setup, Executable

setup(name='CodetoExe',
      version='0.1',
      description='Url Parsing'
      executables= [Executable("CodetoExe.py")])

'''
after this open the folder where u want the
save the exe in command prompt and use the command
"python <setup filename> build"

