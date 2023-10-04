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
        self.grpr = self.__progress__()
        self.dataframe = self.__dataloader__()
        self.startingpoint = 0
        self.l = []
        self.evaluation()
        self.ending()

    #0
    def __dataloader__(self):
        try:
            dataframe = pd.read_csv(file_name)
            dataframe.rename(columns={'Unnamed: 0': 'User ID', '0': 'Comments'}, inplace=True)
            print("Comments were loaded. First comment:")
            print(dataframe.head(1))
            return dataframe
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
            c = 0 # progress counter
            for element in self.grpr['Semantic evaluation']:
                if element not in [0, 1, 2] and c != 0:
                    print(f"There are still {len(self.grpr-c)} elements to annotate")
                    break
                c += 1
            self.startingpoint = c
        else:
            print("Previous progress not found.")
            self.grpr = []
        return self.grpr
    #2
    def ground_truthing(self, text):
        pp = pprint.PrettyPrinter(width=64, depth=1)
        pp.pprint(text)
        inp = str(input("Evaluation:\t\t"))
        if inp not in ["0", "1", "2"]:
            print("Please insert a valid evaluation between 0, 1, 2, or \n press 'exit' to quit.")
            if str(input("")) == "exit":
                return float('NaN')
            inp = int(ground_truthing(text))
        return inp

    def evaluation(self):

        a = len(self.dataframe['Comments'])
        l = list(self.grpr['Semantic evaluation'])
        for comment in self.dataframe['Comments'][self.startingpoint:]:
                res = self.ground_truthing(comment)
                l.append(res)
                if type(res) == float:
                    b = len(self.grpr['Semantic evaluation'])
                    c = a - b
                    l.extend([res] * c)
                    print(f'Session finished at length {c}')
                    self.l = l
                    break

    def ending(self):
        self.grpr[self.startingpoint:len(self.l)-len(self.grpr['Semantic evaluation'])] = self.l
        self.grpr.to_csv("annotations.csv", sep=',', index=False, encoding="utf-8")
        print("Saving annotations")




