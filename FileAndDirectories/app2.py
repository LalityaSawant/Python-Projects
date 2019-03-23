from pathlib import Path

path = Path()
for dirs in path.glob('*'): # * --> dirs and files *.* gives only files
    print(dirs)
