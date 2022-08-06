import json
def write(what,where):
    what=what
    clear(where)
    with open("data_file.json", "w") as write_file:
        json.dump(what, write_file)
    return True
def clear(what):
    with open(what,'w') as cleared:cleared.close()
    return True
def read(read):
    '''returns data'''
    with open(read, "r") as read_file:
        data = json.load(read_file)
    return data