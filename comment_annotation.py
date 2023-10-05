import pandas as pd
import pprint
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

        self.dataframe = self.__dataloader__()
        self.startingpoint, self.l = 0, []
        self.__progress__()
        print(f"Starting analysis from comment {self.startingpoint + 1}")

        self.ci = 0
        self.evaluation()
        self.__closing__()

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
            self.l = pd.read_csv(annotations)
            self.startingpoint = self.l['Last comment checked'] + 1
            # so that the starting point is one position after the last one evaluated.

        except FileNotFoundError:
            print(f"File {annotations} not found...\nCreating an empty dataframe to fill with annotations...")
            result = pd.DataFrame()
            result['Semantic evaluation'] = [] * self.dataframe.shape[0]
            result['User ID'] = self.dataframe['User ID']
            result['Last comment checked'] = 0
            #result.rename(columns={0:'Semantic evaluation'}, inplace=True)
            print("Length of the annotation dataframe:", len(result))
            self.length = len(result)
            self.l = result
            print(self.l.head())
            print("Done.")

    #2
    def ground_truthing(self, text):
        pp = pprint.PrettyPrinter(width=64, depth=1)
        pp.pprint(text)
        inp = str(input("\n\t\tSCORE -->"))
        if inp not in ('0', '1', '2'):
            if inp.strip() == 'exit':
                return float("NaN")
            if inp != 'exit':
                print("Please insert a valid input: exit, or 0, 1, 2.")
                inp = str(input("\n\t\tSCORE --> ")).strip()
                if inp.strip() == 'exit':
                    return float("NaN")

        print()
        return inp

    def evaluation(self):
        print("\n\t\tPRESS 'exit' TO QUIT")
        # ci means comment index
        for ci in range():
            res = self.ground_truthing(self.dataframe['Comments'][ci])
            if type(res) == float:
                self.ci = ci
                return
            self.l.loc[ci,'Semantic evaluation'] = int(res)-1
            self.l.loc[ci+1:, 'Semantic evaluation'] = float('NaN')
            # when going from human using a keyboard to an intuitive
            # the semantic evaluation goes from 0, 1, 2 to -1 0 +1
            self.l.loc[0, 'Last comment checked'] = ci # this is the last comment checked

    def __closing__(self):

        print(f"Progress made: {self.ci/len(self.l)}%")
        print("Saving annotations...")
        self.l.to_csv("annotations.csv", sep=',', index=False, encoding="utf-8")
        print(self.l.head())
        print("Saved.")





Notes()


