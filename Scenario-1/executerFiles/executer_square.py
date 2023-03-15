from MTexecuter import MTexecuter
from Methods_one_input.square	import	square
import pandas as pd
import pathlib
import json
import os

def dataExecution(testData, outputData, outputchecker, pathdata, pathChecker):
    AUXtestInput = []
    AUX_MR1 = []
    AUX_MR2 = []
    AUX_MR3 = []
    AUX_MR4 = []
    AUX_MR5 = []
    AUX_MR6 = []

    for i in range(0, len(testData)):
        testInput = testData[str(i)]['test_data'].copy()
        MR1 = testData[str(i)]['MR1-PER'].copy()
        MR2 = testData[str(i)]['MR2-ADD'].copy()
        MR3 = testData[str(i)]['MR3-MUL'].copy()
        MR4 = testData[str(i)]['MR4-INV'].copy()
        MR5 = testData[str(i)]['MR5-INC'].copy()
        MR6 = testData[str(i)]['MR6-EXC'].copy()

        output_testData = square(testInput)
        output_MR1 = square(MR1)
        output_MR2 = square(MR2)
        output_MR3 = square(MR3)
        output_MR4 = square(MR4)
        output_MR5 = square(MR5)
        output_MR6 = square(MR6)

        AUXtestInput.append(output_testData)
        AUX_MR1.append(output_MR1)
        AUX_MR2.append(output_MR2)
        AUX_MR3.append(output_MR3)
        AUX_MR4.append(output_MR4)
        AUX_MR5.append(output_MR5)
        AUX_MR6.append(output_MR6)

    mainDF['output_testInput'] = AUXtestInput
    mainDF['output_MR1'] = AUX_MR1
    mainDF['output_MR2'] = AUX_MR2
    mainDF['output_MR3'] = AUX_MR3
    mainDF['output_MR4'] = AUX_MR4
    mainDF['output_MR5'] = AUX_MR5
    mainDF['output_MR6'] = AUX_MR6
    
    finalDF = mainDF.copy()

    save_csv(finalDF, outputData, pathdata)
    save_json(finalDF, outputData, pathdata)    
    
    
    for index, row in mainDF.iterrows():

        mr = MTexecuter(row['output_testInput'])

        #MR1
        finalDF.at[index,'MR1_checker'] = mr.mr_PER(row['output_MR1'])

        #MR2
        finalDF.at[index,'MR2_checker'] = mr.mr_ADD(row['output_MR2'])

        #MR3
        finalDF.at[index,'MR3_checker'] = mr.mr_MUL(row['output_MR3'])

        #MR4
        finalDF.at[index,'MR4_checker'] = mr.mr_INV(row['output_MR4'])

        #MR5
        finalDF.at[index,'MR5_checker'] = mr.mr_INC(row['output_MR5'])

        #MR6
        finalDF.at[index,'MR6_checker'] = mr.mr_EXC(row['output_MR6'])

    # finalDF.to_csv('add_values_MRChecker.csv')
    save_csv(finalDF, outputchecker, pathChecker)
    save_json(finalDF, outputchecker, pathChecker)

def save_json(df, output, savePath):
    
    df.to_json(savePath + '/' + output + '.json', indent= 4, orient="index")


def save_csv(df, output, savePath):
    df.to_csv(savePath + '/' + output + '.csv')

if __name__ == '__main__':

    import click 

    global mainDF
    mainDF = pd.DataFrame()

    global auxListmainDF
    auxListmainDF = []

    @click.command()
    @click.option('-i', '--input_path', 'input_path')
    @click.option('-o', '--output', 'output')

    

    def main(input_path, output):
        
        mainPathOutputs = str(pathlib.Path().absolute()) + '/' + 'SUT_outputs'
        mainPathMRChecker = str(pathlib.Path().absolute()) + '/' + 'MR_Checker'

        try:
            os.mkdir(mainPathOutputs)
            os.mkdir(mainPathMRChecker)
        except:
            pass

        with open(input_path, "r") as readfile:
            testData = json.load(readfile)
            json.dumps(testData, indent = 4)

        dataExecution(testData, 'output_' + output, 'MrChecker_' + output, mainPathOutputs, mainPathMRChecker)

main()