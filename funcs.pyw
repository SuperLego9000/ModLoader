from os import system as sys
import JsonUtils as jsu
import glob
import pyautogui as gui
cwd="C:/Users/drake/OneDrive/Desktop/Desktop/programs/ROBLOX/modloader/ModLoader2.0"

def backup(**kwargs):
    """
    takes current version full path
        backup(ver='C:\\myrobloxpath\\Versions\\myversion\\')
    """
    try:
        _ = kwargs['ver']
        _ = None
    except KeyError:
        raise KeyError('ver is a required argument')

    ver = kwargs['ver']
    sys(f'rmdir "{cwd}/resources/backup/" /Q /S')  # delete backup folder
    print("old backup deleted")
    sys(f'mkdir "{cwd}/resources/backup/"')  # make backup folder
    print("new backup copying...")
    sys(f'xcopy "{ver}" "{cwd}/resources/backup/" /Y /Q /s /i')
    gui.alert('Backup Complete', 'Backup Complete')
    # copy version to backup folder

def restore(**kwargs):
    """
    takes current version full path
        ver='C:\\myrobloxpath\\Versions\\myversion\\')
    """
    try:
        _ = kwargs['ver']
        _ = None
    except KeyError:
        raise KeyError('ver is a required argument')
    ver = kwargs['ver'].replace("\\", "/")
    sys(f'robocopy "{cwd}/resources/backup/" "{ver}" /MIR'+" >nul 2>&1") #should copy the mod into the version folder
    print("installation restored")

def pickmod(**kwargs):
    bs='\\'
    """
    takes current version full path
        pickmod(ver='C:\\myrobloxpath\\Versions\\myversion\\')
    """
    try:
        _ = kwargs['ver']
        _ = None
    except KeyError:
        raise KeyError('ver is a required argument')
    #for folders in resources/mods
    #open manifest.json with context manager
    #if file is a json file
    names=[]
    for folder in glob.glob(f'{cwd}/resources/mods/*'): #for all the mods
        #replace the \\ in folder with /
        folder=folder.replace('\\','/')
        data=jsu.read(f"{folder}/manifest.json") #decode
        names.insert(len(names),data['Name']) #append mod name
    names.append('Exit')
    mod=gui.confirm('Select Mod', 'Select Mod', buttons=names)
    #if user selects a mod
    if mod!='Exit':
        #open manifest.json with context manager
        data=jsu.read(f'{cwd}/resources/mods/{mod}/manifest.json')
        _ = gui.confirm(f"discription:\n{data['Discription']}\n\nchanges:\n{data['changes']}",f"{data['Name']} - Info",['Load','Exit'])
        if _=='Load':
            loadmod(mod=f'{cwd}/resources/mods/{mod}/',ver=kwargs['ver'])

def loadmod(**kwargs):
    """
    takes current version full path
        loadmod(ver='C:\\myrobloxpath\\Versions\\myversion\\')
    takes mod directory full path
        loadmod(mod='./resources/mods/mymod/')
    """
    try:
        _ = kwargs['ver']
        _ = kwargs['mod']
        _ = None
    except KeyError as err:
        raise KeyError(f'{err} is a required argument')
    ver = kwargs['ver'].replace("\\", "/")
    mod = kwargs['mod'].replace("\\", "/")
    #ver=f"{mod}../cheese/"
    sys(f'mkdir "{ver}"'+" >nul 2>&1")
    # sys('pause')
    ver=ver[:-1]
    mod=mod[:-1]
    sys(f'robocopy {mod} {ver} /S'+" >nul 2>&1") #should copy the mod into the version folder
    print("mod loaded")

def newmod(**kwargs):
    global cwd
    bs='\\'
    """
    takes resources full path
        newmod(res='./resources/')
    """
    try:
        _ = kwargs['res']
        _ = None
    except KeyError:
        raise KeyError('res is a required argument')
    res = kwargs['res'].replace("\\", "/")
    
    name=gui.prompt('Enter Mod Name', 'newmod')
    cwd=cwd.replace('/', bs)
    sys(f"mkdir {cwd.replace('/', bs)}\\resources\\mods\\{name}")
    sys(f'copy "{cwd}\\resources\\templatemod\\manifest.json" "{res}mods\\{name}\\manifest.json"') #copy the manifest over
    print("mod created")
    sys(f'explorer "{cwd}\\resources\\mods\\{name}\\"')
    gui.confirm(f'change the name in the manifest to "{name}"', 'newmod')
    sys('pause')

def openver(**kwargs):
    """
    takes current version full path
        openver(ver='C:\\myrobloxpath\\Versions\\myversion\\')
    """
    try:
        _ = kwargs['ver']
        _ = None
    except KeyError:
        raise KeyError('ver is a required argument')
    ver = kwargs['ver']
    sys(f'explorer "{ver}"')

if __name__ == '__main__':
    newmod(ver="JOE",mod="alsojoe",res='./resources/')

modes = {
    'backup version': backup,
    'restore version': restore,
    'select mod': pickmod,
    'open version': openver,
}
