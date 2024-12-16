# Understanding intense online sentiment: The Youtube Apology and related intense online discourse using NLP
This repo was my first attempt at NLP, using Google's API and VADER sentiment analysis tool. You can find the report [here](https://github.com/FluveFV/StrangersOnYoutube/blob/main/CSS_DavideVandelli.pdf)

Today, on the Internet, slang and online lingo persist and spread as a form of typical communication. To have quantitative analysis on i.e. YouTube comments, it means to possess precious information on the behaviour of thousands of people, interacting with specific content. This can give insight over how humans are interacting on this platform, and if their behaviour is deviant and needs rehabilitation, or alternatively is a byproduct of the platform's rules. 

For slang NLP, VADER is a light-weight pretrained model used in this repository. In this specific project, I have personally reviewed 1000 YouTube comments and evaluated if they meant positive, neutral or negative content, in order to evaluate how VADER would perform on one video's comment section. 

Usage: 

- to obtain data (using your Google API key!) and your Youtube video of choice, change the link and the Google API key when running the notebook data_retrieval_and_cleaning.ipynb.
- to make a sample for human annotation of the semantic analysis (for whatever purposes; I recommend making a small dataset of groundtruth and using it to evaluate other NLP models under comments of your choice) run basic_sentiment_analysis.ipnyb
- to annotate comments that come from any csv file named 'sample_for_groundtruth.csv' and has columns named 'Unnamed: 0' representing users' ID and 'Comments' representing users' comments, the last cell of the previous script. You cannot do this unless you have ran the other two scripts or you change some of the input files. 
Other scripts are there to allow for editing specific important classes, such as "Note" class which allows for CLI human evaluation of comments.


