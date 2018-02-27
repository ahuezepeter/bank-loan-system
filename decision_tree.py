import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import train_test_split 
from sklearn.metrics import accuracy_score, confusion_matrix
from features import features # getting the features needed for this project
from features import target # getting the target


data = pd.read_csv('lending-club-data.csv',low_memory=False)

cols_needed = data[features +[target]]

num_data = cols_needed.convert_objects(convert_numeric=True)
onlydata = num_data.dropna() # dropping null values

feats = onlydata[features]
tars = onlydata[target]

feat_train, feat_test, tar_train, tar_test =train_test_split(feats, tars, test_size=.3)

# running the Decision tree classifier
classifier = DecisionTreeClassifier()
dtree = classifier.fit(feats_train, tar_train)

# performing predictions
predictions = dtree.prediction(feats_test)

#running the metrics

print 'Accuracy Score =',
print accuracy_score(predictions, tar_test)
print
print 'Confusion Matrix='
print consuion_matrix(predictions, tar_test)

