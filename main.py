import pyautogui as gui
import glob
import os
title = "ModLoader2.0"
os.system("cls")

def newest_subdir(b='.'):
    return max(glob.glob(os.path.join(b, '*/')), key=os.path.getmtime)
path = os.environ.get('LOCALAPPDATA')+'\\Roblox\Versions\\'
version = newest_subdir(path)

#the newest version is found but let's confirm with user
bs = '\\'
_ = gui.confirm(
    f'Newest Version:\n{version.split(bs)[-2][8:]}\nContinue with newest version?', title+' - Select Version', ['OK', 'Custom'])
if _ == 'Custom':
    version = gui.prompt('Enter Version path', title+' - Select Version')
#the user now knows the version they want to use and we can start working on it


import funcs 
#start the gui loop
while 1:
    try:
        options = []
        for i,name in enumerate(funcs.modes):
            options.insert(len(options), name)
        option=gui.confirm('Select Mode', title+' - Select Mode', options)
        funcs.modes[option](ver=version,)
    except KeyboardInterrupt:
        print("exiting...")
        break
    except:
        pass