#!/usr/bin/python

import sys
import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectPercentile,f_classif

sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data
from visualize_new_feature import update_with_fraction_poi



### Load the dictionary containing the dataset
data_dict = pickle.load(open('final_project_dataset.pkl', "r") )

## Task 2: Remove outliers
data_dict.pop('TOTAL')

### Task 3: Create new feature(s)
data_with_fraction_poi = update_with_fraction_poi(data_dict)#Update dataset with fraction poi


df = pd.DataFrame.from_dict(data_with_fraction_poi,orient='index') #create pandas Dataframe from dataset

cols = df.columns.tolist() # get the list of features
cols.remove('email_address')#remove non numeric features
cols.remove('poi')# remove labels
impute = df[cols].copy().applymap(lambda x: 0  if x == 'NaN' else x) #replace NaN features as 0

scaled = impute.apply(MinMaxScaler().fit_transform) #Scaled each of the feature 

selPerc = SelectPercentile(f_classif,percentile=21) # Built the SelectPercentile, 21 Selected Based on the Performance
selPerc.fit(scaled,df['poi']) # Learn the Features, knowing which features to use

features_percentiled = scaled.columns[selPerc.get_support()].tolist() #Filter columns based on what Percentile support
scaled['poi'] = df['poi'] #rejoin the label


### Store to my_dataset for easy export below.
my_dataset = scaled.to_dict(orient='index') #change the dataframe back to dictionary

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi'] + features_percentiled # You will need to use more features

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.
from sklearn.naive_bayes import GaussianNB ##Default: Precision: 0.50158	Recall: 0.39600, BEST!
from sklearn.tree import DecisionTreeClassifier ##Default: Precision: 0.14830	Recall: 0.05450
from sklearn.ensemble import RandomForestClassifier ##Default: Precision: 0.47575	Recall: 0.20600, Longer time
from sklearn.linear_model import SGDClassifier ##Default: Precision: 0.29148	Recall: 0.22400

clf = GaussianNB()


### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Example starting point. Try investigating other evaluation techniques!
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)