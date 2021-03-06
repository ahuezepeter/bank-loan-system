import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.cross_validation import train_test_split 
from sklearn.metrics import accuracy_score, confusion_matrix
from features import features # getting the features needed for this project
from features import target # getting the target


data = pd.read_csv('lending-club-data.csv',low_memory=False)
data['safe_loans'] = data['bad_loans'].apply((lambda x: +1 if x== 0 else -1))
ddata = data.dropna() #dropping data wih null values
loans = ddata[features +[target]]


cats = []
ccols = []
for c,d in zip(loans.columns, loans.dtypes):
  if d == object:
    cats.append(c)

for cat in cats:
  a = loans.groupby(cats)[cats].count()
  ccols = ccols + a.index.tolist()

# one hot encoding....
print 'Performing One hot encoding...'
cat_loans = loans[cats]
dict_loans = cat_loans.T.to_dict().values()

vectorizer = DictVectorizer(sparse=True)
mat_loans = vectorizer.fit_transform(dict_loans)

newloans = pd.DataFrame(mat_loans, columns=ccols)
nloans = loans.drop(cats, axis=1)

newloans = newloans.join(nloans)


feats = newloans[features]
tars = newloans[target]

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

