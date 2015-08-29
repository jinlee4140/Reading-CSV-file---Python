import pandas as pd

csv_read = pd.read_csv('data.csv')
print csv_read.head()

#Our file has headers, which the function inferred upon reading in the file. Had we wanted to be more explicit, we could have passed header=None
#to the function along with a list of column names to use.

cols = ['num', 'game', 'date', 'team', 'home_away', 'opponent',
        'result', 'quarter', 'distance', 'receiver', 'score_before',
        'score_after']


manningcsv = pd.read_csv('peytonmanning.csv', sep=',', header=None, names=cols)
print manningcsv.head()

#This following one is incorrect because you need a header.
manningcsv2 = pd.read_csv('peytonmanning.csv')
print manningcsv2.head()

