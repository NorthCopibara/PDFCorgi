from Resources.Config import SAVE_DATA_PATH


def SavePath(path):
    with open(SAVE_DATA_PATH, "w") as file:
        file.write(path)

def LoadPath():
    with open(SAVE_DATA_PATH, "r") as file:
        return str(file.read().strip())
