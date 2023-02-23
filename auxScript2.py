import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
import json

with open("auxSript_output/methodInfo.json", "r") as readfile:
    info = json.load(readfile)
    json.dumps(info,indent = 4)

for i in range(0,len(info)):
    fileName = info[str(i)]['file_name']
    f = open('executer_' + fileName, "x")
