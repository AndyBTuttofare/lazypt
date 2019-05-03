import os

def path_finder():

    script_path = os.path.abspath(__file__)
    script_path = script_path.split("\\")
    le = len(script_path)
    script_path = '\\'.join(script_path[0:le-1])
    script_path = script_path + '\\'

    return script_path