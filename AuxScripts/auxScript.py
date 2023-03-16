import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import glob as gl
import pathlib
import time
import json
import os

def process(path):
    file_name = path.split('/')[-1]
    method_name = file_name.split('.')[0]
    ext = file_name.split('.')[-1]
    
    mainDF = {
        'path': path,
        'file_name': file_name,
        'method_name': method_name,
        'ext': ext
    }

    auxList.append(mainDF)

def save_json(df, output, savePath):
    
    df.to_json(savePath + '/' + output + '.json', indent= 4, orient="index")


def save_csv(df, output, savePath):
    df.to_csv(savePath + '/' + output + '.csv')

if __name__ == '__main__':

    import click 

    global mainDF
    mainDF = {}

    global auxList
    auxList = []

    @click.command()
    @click.option('-i', '--input_path', 'input_path')
    @click.option('-o', '--output', 'output')

    def main(input_path, output):
        
        mainPath = str(pathlib.Path().absolute()) + '/' + 'auxSript_output'

        try:
            os.mkdir(mainPath)
        except:
            pass

        filePath = gl.glob(input_path)

        for path in filePath:
            process(path)

        df = pd.DataFrame(auxList)

        save_csv(df, output, mainPath)
        save_json(df, output, mainPath)



main()
