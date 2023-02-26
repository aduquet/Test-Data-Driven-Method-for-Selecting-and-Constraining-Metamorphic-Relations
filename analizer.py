import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import glob as gl
import pathlib
import random
import json
import os

def save_json(df, output, savePath):
    
    df.to_json(savePath + '/' + output + '.json', indent= 4, orient="index")


def save_csv(df, output, savePath):
    df.to_csv(savePath + '/' + output + '.csv')

def infoExtractor(methodName, df):
    size = len(df)

    mr1 = df['MR1_checker'].value_counts()
    mr2 = df['MR2_checker'].value_counts()
    mr3 = df['MR3_checker'].value_counts()
    mr4 = df['MR4_checker'].value_counts()
    mr5 = df['MR5_checker'].value_counts()
    mr6 = df['MR6_checker'].value_counts()
    mr1Keys = mr1.keys().to_list()
    mr2Keys = mr2.keys().to_list()
    mr3Keys = mr3.keys().to_list()
    mr4Keys = mr4.keys().to_list()
    mr5Keys = mr5.keys().to_list()
    mr6Keys = mr6.keys().to_list()

    MR1_Not_violated = 0
    MR1_Violated = 0

    MR2_Not_violated = 0
    MR2_Violated = 0

    MR3_Not_violated = 0
    MR3_Violated = 0

    MR4_Not_violated = 0
    MR4_Violated = 0

    MR5_Not_violated = 0
    MR5_Violated = 0

    MR6_Not_violated = 0
    MR6_Violated = 0

    if 'Not-violated' in mr1Keys:
        MR1_Not_violated = round((mr1['Not-violated']*100)/size)
    
    if 'Violated' in mr1Keys:

        MR1_Violated = round((mr1['Violated']*100)/size)

    ## MR2
    if 'Not-violated' in mr2Keys:
        MR2_Not_violated = round((mr2['Not-violated']*100)/size)
    
    if 'Violated' in mr2Keys:

        MR2_Violated = round((mr2['Violated']*100)/size)

    # MR3
    if 'Not-violated' in mr3Keys:
        MR3_Not_violated = round((mr3['Not-violated']*100)/size)
    
    if 'Violated' in mr3Keys:

        MR3_Violated = round((mr3['Violated']*100)/size)
    
    # MR4
    if 'Not-violated' in mr4Keys:
        MR4_Not_violated = round((mr4['Not-violated']*100)/size)
    
    if 'Violated' in mr4Keys:

        MR4_Violated = round((mr4['Violated']*100)/size)

    # MR5
    if 'Not-violated' in mr5Keys:
        MR5_Not_violated = round((mr5['Not-violated']*100)/size)
    
    if 'Violated' in mr5Keys:

        MR5_Violated = round((mr5['Violated']*100)/size)
    
    # MR6
    if 'Not-violated' in mr6Keys:
        MR6_Not_violated = round((mr6['Not-violated']*100)/size)
    
    if 'Violated' in mr6Keys:
        MR6_Violated = round((mr6['Violated']*100)/size)
    
    mainDF = {
        'methodName': methodName,
        
        'MR1_Not_violated': MR1_Not_violated,
        'MR1_Violated' : MR1_Violated,
        
        'MR2_Not_violated': MR2_Not_violated,
        'MR2_Violated' : MR2_Violated,
        
        'MR3_Not_violated': MR3_Not_violated,
        'MR3_Violated' : MR3_Violated,
        
        'MR4_Not_violated': MR4_Not_violated,
        'MR4_Violated' : MR4_Violated,
        
        'MR5_Not_violated': MR5_Not_violated,
        'MR5_Violated' : MR5_Violated,
        
        'MR6_Not_violated': MR6_Not_violated,
        'MR6_Violated' : MR6_Violated
    }
    
    return mainDF



if __name__ == '__main__':

    import click 

    global mainDF
    mainDF = {}

    global auxListmainDF
    auxListmainDF = []

    @click.command()
    @click.option('-i', '--input_path', 'input_path')
    # @click.option('-d', '--dir', 'dir')
    @click.option('-o', '--output', 'output')

    def main(input_path, output):
        
        mainPath = str(pathlib.Path().absolute()) + '/' + 'AnaliserOutputs'

        try:
            os.mkdir(mainPath)
        except:
            pass
        
        filePath = gl.glob(input_path)
        jsonPathFiles = []
        csvPathFiles = []

        

        for i in filePath:
            if i.find('.json') != -1:
                jsonPathFiles.append(i)
            else:
                csvPathFiles.append(i)

        for i in csvPathFiles:
            methodName = i.split('.')[0]
            methodName = methodName.split('/')[-1]
            methodName = methodName.split('MrChecker_')[-1]
            df = pd.read_csv(i, index_col=0)
            df2 = infoExtractor(methodName, df)
            auxListmainDF.append(df2)
        
        finalDF = pd.DataFrame(auxListmainDF)
        final = finalDF.sort_values(by=['methodName']).reset_index(drop=True)
        print(final)

        save_csv(final, output, mainPath)
        save_json(final, output, mainPath)

main()