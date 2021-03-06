#This script segregates the continous data of Innings, Venue & Winners into dummy variables

import pandas as pd

match_data = pd.read_csv('dataset.csv')
new_data = match_data[['Innings_Team1','Innings_Team2','Venue_Team1','Venue_Team2','Winner']].copy()
feature_cols = list(new_data.columns[0:5])
extra_cols = list(match_data.columns[0:207])

print("Feature columns:\n{}".format(feature_cols))

print("Extra columns:\n{}".format(extra_cols))

X_all = match_data[feature_cols]

def convert_intoDummyTeams(X):
	output = pd.DataFrame(index = X.index)

	for col,col_data in X.iteritems():
		if col_data.dtype == object:
			col_data = pd.get_dummies(col_data,prefix = col)
		output = output.join(col_data)
	return output

X_all = convert_intoDummyTeams(X_all)

print("Processed Feature columns:\n{}".format(list(X_all.columns)))

NewDF = pd.DataFrame(index = match_data.index)

oldDF = match_data[extra_cols]

NewDF = NewDF.join(oldDF)

print(NewDF.head())

NewDF = NewDF.join(X_all)

print(NewDF.head())




NewDF.to_csv('dataset_InningsWinner_IntoDummies.csv',index=False)
