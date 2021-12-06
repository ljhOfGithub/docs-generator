import sys
import re
def getRepo(self,examFile):
    #suppose example file is in the examples folders that is essential to use the script.
    #examFile is a file name
    importRepo = []
    with open(examFile,'r') as exam:
        #recognize the function in exam
        #split the function body and function name
        #store the import repo to the 'importRepo' list
        #suppose all repos are imported by "import *"(*represent the repo name)
        importPara = []
        lines = exam.readlines()
        for line in lines:
            if "import" in line:
                    importPara.append(line)
        importReReg = r'import\s^[A-Za-z0-9]+$' #suppose repo name is combined of letter or underline
        importRepo = re.match(importPara,importReReg)#get all imported repo
        

def getWellLine(self,examFile):
    with open(examFile,'r') as exam:
        lines = exam.readlines()
        wellLine = []
        for line in lines:#get the line starting with '#'
            if line.startswith("#")
                wellLine.append(line)
        
    return wellLine

# TODO:get the three-quote lines
# def getQuoteLine(self,examFile):
#     with open(examFile,'r') as exam:
#         lines = exam.readlines()
#         quoteLine = ""
#         for line in lines:
#             if line.startswith()


def getFuncName(self,examFile):
    with open(examFile,'r') as exam:
        funcNames = []
        for line in lines:
            if line.startswith("def"):
                funcName = GetMiddleStr(line,'def','(')
                funcNames.append(funcName)
        return funcNames

def getFuncPara(self,examFile):
    with open(examFile,'r') as exam:
        funcParas = []
        for line in lines:
            if line.startswith("def"):
                funcParaStr =  line.split("(")
                funcParas = funcParaStr.split(",")
        return funcParas











