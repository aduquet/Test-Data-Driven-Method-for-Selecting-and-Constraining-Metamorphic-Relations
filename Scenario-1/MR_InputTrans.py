import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pathlib
import random
import json
import os

def MR1_PER(testData):

    # Permutative -> Randomly permute the elements

    for i in range(0, len(testData)):
        aux = testData[str(i)]['input'].copy()
        mainDF = {
            'test_data': testData[str(i)]['input'],
            'MR1-PER': random.sample(aux, len(aux))
        }
        auxListmainDF.append(mainDF)

def MR2_ADD(testData, constant):

    # Additive -> Add a positive constant

    auxListMR2 = []
    for i in range(0, len(testData)):
        aux = testData[str(i)]['input'].copy()
        auxList = []
        for i in aux:
            auxList.append(i + constant)    
        auxListMR2.append(auxList)

    return auxListMR2

def MR3_MUL(testData, constant):

    # Multiplicative -> Multiply by a positive constant
    
    auxListMR = []
    for i in range(0, len(testData)):
        aux = testData[str(i)]['input'].copy()
        auxList = []
        for i in aux:
            auxList.append(i * constant)    
        auxListMR.append(auxList)

    return auxListMR

def MR4_INV(testData):

    # Invertive -> Take the inverse of each element
    
    auxListMR = []
    for i in range(0, len(testData)):
        aux = testData[str(i)]['input'].copy()
        auxList = []
        for i in aux:
            if(i != 0):
                auxList.append(1/i) 
        auxListMR.append(auxList)

    return auxListMR

def MR5_INC(testData, constant):

    # Inclusive -> Add a new element
    
    auxListMR = []
    for i in range(0, len(testData)):
        aux = testData[str(i)]['input'].copy()
        aux.append(constant)
        auxListMR.append(aux)

    return auxListMR

def MR6_EXC(testData):

    # Exclusive -> Remove an elementt
    
    auxListMR = []
    for i in range(0, len(testData)):
        aux = testData[str(i)]['input'].copy()
        if len(aux) > 1 :
            aux.pop()
        auxListMR.append(aux)

    return auxListMR

def save_json(df, output, savePath):
    
    df.to_json(savePath + '/' + output + '.json', indent= 4, orient="index")


def save_csv(df, output, savePath):
    df.to_csv(savePath + '/' + output + '.csv')

if __name__ == '__main__':

    import click 

    global mainDF
    mainDF = {}

    global auxListmainDF
    auxListmainDF = []

    @click.command()
    @click.option('-i', '--input_path', 'input_path')
    @click.option('-o', '--output', 'output')

    def main(input_path, output):
        
        mainPath = str(pathlib.Path().absolute()) + '/' + 'MR_InputTransformations'

        try:
            os.mkdir(mainPath)
        except:
            pass

        with open(input_path, "r") as readfile:
            testData = json.load(readfile)
            json.dumps(testData,indent = 4)
        constant = 0
        while constant == 0 or constant == 1:
            constant = np.random.uniform(low=0, high=15, size=1).astype(int)[0]

        MR1_PER(testData)
        df = pd.DataFrame(auxListmainDF)

        df['MR2-ADD'] = MR2_ADD(testData, constant)
        df['MR3-MUL'] = MR3_MUL(testData, constant)
        df['MR4-INV'] = MR4_INV(testData)
        df['MR5-INC'] = MR5_INC(testData,constant)
        df['MR6-EXC'] = MR6_EXC(testData)

        save_csv(df, output, mainPath)
        save_json(df, output, mainPath)

main()