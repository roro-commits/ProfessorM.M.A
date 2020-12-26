import os

name = 'fighterData'
files = os.system(' ls  -l')
location = os.system('pwd')

print("***********", location)
print("***********", files)
os.system('cd ..')
print("***********", location)
print("***********", files)