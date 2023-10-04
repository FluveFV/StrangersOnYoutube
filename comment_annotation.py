import json
import pandas as pd
import pprint
import numpy as np
file_name = "sample_for_groundtruth.csv"
annotations = "annotations.csv"

class Notes:
    """
    at least four attributes other than initialization
    0- loads the dataframe with comments from the same folder this class is located in
    1- checks the state of progress is made it's uploaded and won't be lost.
    2- prints one text (one comment) and takes the annotation input
    3- iterates over the dataframe and uses #2
    4- saves the progress made.
    """
    def __init__(self):
        self.__dataloader__()
        self.grpr = self.__progress__()
        self.ground_truthing = self.ground_truthing

    #0
    def __dataloader__(self):
        try:
            self.dataframe = pd.read_csv(file_name)
            self.dataframe.rename(columns={'Unnamed: 0': 'Comments', '0': 'User ID'}, inplace=True)
            print("Data was loaded. First comment:")
            print(self.dataframe.head(1))
        except FileNotFoundError:
            print(f'File "{file_name}" not found!')

    #1
    def __progress__(self):
        try:
            self.annotations = pd.read_csv(annotations)
            anncheck = True
            print("Previous progress found. First progress made:")
        except FileNotFoundError:
            anncheck = False
            print(f"File {annotations} not found!")

        if anncheck:
            self.grpr = self.annotations
            print(self.grpr.head(1))
        else:
            print("Previous progress not found.")
            self.grpr = []
        return self.grpr
    #2
    def ground_truthing(text):
        pp = pprint.PrettyPrinter(width=64, depth=1)
        pp.pprint(text)
        inp = str(input("Evaluation:\t\t"))
        if inp not in ["0", "1", "2"]:
            print("Please insert a valid evaluation between 0, 1, 2, or \n press 'exit' to quit.")
            if str(input("")) == "exit":
                return float('NaN')
            inp = int(text.ground_truthing(text))
        return inp

    def evaluation(self, dataframe, startingpoint=0):

        a = len(dataframe['Original comments'])
        if startingpoint != 0:
            for comment in dataframe['Original comments'][startingpoint:]:
                res = self.ground_truthing(comment)
                self.grpr.append(res)
                if type(res) == float:
                    b = len(self.grpr)
                    c = a - b
                    grpr.extend([res] * c)
                    print(f'Session finished at length {b}')
                    break
        else:
            for comment in dataframe['Original comments']:
                res = ground_truthing(comment)
                grpr.append(res)
                if type(res) == float:
                    b = len(grpr)
                    c = a - b
                    grpr.extend([res] * c)
                    print(f'Session finished at length {b}')
                    break

Notes()
Notes.evaluation()




