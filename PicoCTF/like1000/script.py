import subprocess
import os

##################################################################

# Initial Solution:

def list_dir():
    result = subprocess.run(["ls"], stdout=subprocess.PIPE, text=True)
    list_result = []
    temp = ""
    for i in result.stdout:
        if(i == '\n'):
            list_result += [temp]
            temp = ""
        else:
            temp += i    
    return list_result

#It turns out this one is not necessary because there is no flag in the filler.txt file
def checkIfFlag(list_result):
    for i in list_result:
        if "txt" in i:
            result = subprocess.run(["cat", "filler.txt"], stdout=subprocess.PIPE, text=True)
            if "picoCTF" in result.stdout:
                print("FLAG found ----> ", result.stdout)      

def unzipAndRemove(fileId):
    arg = "tar -xvf " + str(fileId) + ".tar"
    os.system(arg)
    if(fileId != 1000):
        arg = "rm -r " + str(fileId) + ".tar"
        os.system(arg)

def main():
    for i in range(1000, 0, -1):
        unzipAndRemove(i)
        checkIfFlag(list_dir())

##################################################################

# This part is enough:

def unzipAndRemoveAll1000():
    for i in range(1000, 0, -1):
        arg = "tar -xvf " + str(i) + ".tar"
        os.system(arg)
        if(i != 1000):
            arg = "rm -r " + str(i) + ".tar"
            os.system(arg)

unzipAndRemoveAll1000()