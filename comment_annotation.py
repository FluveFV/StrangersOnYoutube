import json
import pandas as pd
import pprint
import numpy as np
file_name = "sample_for_groundtruth.csv"
annotations = "annotations.csv"

class Notes:

    # at least four attributes:
    # 0 loads the dataframe with comments from the same folder this class is located in
    # 1 checks the state of progress is made it's uploaded and won't be lost.
    # 2 takes prints a comment and takes the annotation input
    # 3 takes iterates over the remaining not annotated comments and calles each time
    # the function number 2
    # 4 saves the progress made.
    def __init__(self):
        self.dataloader = pd.read_csv(file_name)
        self.dataloader.rename(columns={'Unnamed: 0': 'Original indexes', '0': 'User ID'}, inplace=True)
        try:
            self.annotations = pd.read_csv(annotations)
        except FileNotFoundError:
            self.annotations = False

        print("Data was loaded")
        print(self.dataloader.head(5))

    def progress(self):
        if self.annotations:
            print("Previous progress found.")
            self.grpr = self.annotations
        else:
            print("Previous progress not found.")
            self.grpr = []

    def ground_truthing(text):
        pp = pprint.PrettyPrinter(width=64, depth=1)
        pp.pprint(text)
        inp = str(input("Evaluation:\t\t"))
        if inp not in ["0", "1", "2"]:
            print("Please insert a valid evaluation between 0, 1, 2, or \n press 'exit' to quit.")
            if str(input("")) == "exit":
                return float('NaN')
            inp = int(ground_truthing(text))
        return inp

    ground_truthing("test " * 6 * 14)


Notes()




