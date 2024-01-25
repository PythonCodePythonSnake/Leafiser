import os
from shutil import rmtree

if os.path.isdir(os.path.join(os.getcwd(), "Dataset")):
    rmtree(os.path.join(os.getcwd(), "Dataset"))
    print("dataset removed")
else: print("dataset already removed")