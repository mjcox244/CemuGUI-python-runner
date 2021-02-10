import os, wget, time
from zipfile import ZipFile
import shutil

latest_cemu="1.22.5"




	




#get the latest version of this tool (at least when i work out how to copy the python file out the folder it makes)
wget.download("https://github.com/mjcox244/CemuGUI-python-runner/archive/main.zip")
with ZipFile('CemuGUI-python-runner-main.zip', 'r') as zipObj:
	# Extract all the contents of zip file in current directory
	zipObj.extractall()
os.remove("CemuGUI-python-runner-main.zip")
cmd = "xcopy CemuGUI-python-runner-main " + os.getcwd() + "/s /Y /Q"
os.system(cmd
os.system("rmdir CemuGUI-python-runner-main"))

#update / dowmload cemu
wget.download("https://cemu.info/releases/cemu_"+ latest_cemu +".zip")
with ZipFile("cemu_"+ latest_cemu + ".zip", 'r') as zipObj:
	# Extract all the contents of zip file in current directory
	zipObj.extractall('')
os.remove("cemu_"+ latest_cemu + ".zip")
try:
	os.system('cmd /c "mkdir Cemu"')
except:
	print("")
os.system('cmd /c "xcopy cemu_1.22.5 Cemu /s /Y /Q /K"')
os.system("rmdir cemu_" + latest_cemu)



if(os.path.isfile("Setup-done")):
	print ("DEBUG THE FILE IS THERE")
else:
	
	#download CemuGUI
	wget.download("https://download1653.mediafire.com/dl74cd2ahxmg/qfegbxxrda3i10r/CemuGUI+2.0+Beta.zip")
	with ZipFile("CemuGUI 2.0 Beta.zip", 'r') as zipObj:
		zipObj.extractall("")
	os.remove("CemuGUI 2.0 Beta.zip")
	with open("Setup-done", 'w') as file_object:
		file_object.write("Setup is done!")
