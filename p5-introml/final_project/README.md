
**Summarize for us the goal of this project and how machine learning is useful in trying to accomplish it. As part of your answer, give some background on the dataset and how it can be used to answer the project question. Were there any outliers in the data when you got it, and how did you handle those?  [relevant rubric items: “data exploration”, “outlier investigation”]**

The goal for this project is to identify who's the person of interest. In other words, people who actually comitting the fraud in Enron. Their crimes include selling assets to shell companies at the end of each month, and buying them at the beginning of each month to avoid accounting losses. Hopefully if there are any other person that are not in the dataset, the machine learning can identify them based on the financial features and emails, whether the person is actually POI.

There are 146 person in the dataset, 18 of those are a person of interest (there are actually 35 persons). Since  email data is just a sample, there are missing POI data. It may cause the prediction to a little worse. There are 21 features in the dataset. 

The dataset is not without an error. Especially the financial features. Because not all POI in the dataset, we might want to add it by hand, and just put missing value for financial information. But this itself could lead an error, because machine learning could predict whether a person POI or not based on `NaN` value. So financial features is still being considered.

In the dataset, there's an outlier which is 'TOTAL'. This should be total of numerical features that every person in ENRON dataset has, but counted as a person. This is an outlier. we should exclude this because it's not a data that we have attention too. Next I begin to observe an outlier, and I have 2 out of 4 outlier that identified as POI. Since this is the data that we're paying attention, we don't exclude the outlier. 

**What features did you end up using in your POI identifier, and what selection process did you use to pick them? Did you have to do any scaling? Why or why not? As part of the assignment, you should attempt to engineer your own feature that does not come ready-made in the dataset -- explain what feature you tried to make, and the rationale behind it. (You do not necessarily have to use it in the final analysis, only engineer and test it.) In your feature selection step, if you used an algorithm like a decision tree, please also give the feature importances of the features that you use, and if you used an automated feature selection function like SelectKBest, please report the feature scores and reasons for your choice of parameter values.  [relevant rubric items: “create new features”, “properly scale features”, “intelligently select feature”]**

I add new features such as fraction in which this person sent email to POI persons, and fraction POI persons send emails to this persons. The reason behind this is because there's could be that if this person have higher frequencies of sending and receiving email with POI persons, this person could end up being POI himself.

I scaled any numerical features. The reason behind this because the algorithm that I'm using NaiveBayes consider the features to both dependent of each other. It doesn't like linear regression where features is independent of each other (based on coefficient), or like decision tree (where it split only based on 1 feature).

I select features based on the 21 percentile using SelectPercentile. I tried variety of percentiles that maximize both precision and recall. When both are deliver some trade-off, I determine the highest based on given F1 score.

**What algorithm did you end up using? What other one(s) did you try? How did model performance differ between algorithms?  [relevant rubric item: “pick an algorithm”]**

I ended up choosing Gaussian Naive Bayes, as it gives the default best performance compared to any other classifier that I tried. The performance default for each of the algorithm are as follows:

```Python
from sklearn.naive_bayes import GaussianNB ##Default: Precision: 0.50158	Recall: 0.39600, BEST!
from sklearn.tree import DecisionTreeClassifier ##Default: Precision: 0.14830	Recall: 0.05450
from sklearn.ensemble import RandomForestClassifier ##Default: Precision: 0.47575	Recall: 0.20600, Longer time
from sklearn.linear_model import SGDClassifier ##Default: Precision: 0.29148	Recall: 0.22400
```

**What does it mean to tune the parameters of an algorithm, and what can happen if you don’t do this well?  How did you tune the parameters of your particular algorithm? (Some algorithms do not have parameters that you need to tune -- if this is the case for the one you picked, identify and briefly explain how you would have done it for the model that was not your final choice or a different model that does utilize parameter tuning, e.g. a decision tree classifier).  [relevant rubric item: “tune the algorithm”]**

Since the algorithm that I ended up choosing doesn't require any tuning for the algorithm. I haven't use them. If I'm using Decision Tree classifier, I will choose the criterion entropy, as this is the kind of criterion that maximize information gain, and choose higher min_samples_split, since it will avoid overfitting.

**What is validation, and what’s a classic mistake you can make if you do it wrong? How did you validate your analysis?  [relevant rubric item: “validation strategy”]**

Validation is importance when we want to test the model against future data. While the drawback is we have smaller to trained, but it's useful to the the performance. We can't train the model using whole data and test it with the same one, as the model will already know what it's against and will perform excellently, and this called ***cheating*** in machine learning. I will use train test split with 70:30, and validate the performance again precision and recall.

Give at least 2 evaluation metrics and your average performance for each of them.  Explain an interpretation of your metrics that says something human-understandable about your algorithm’s performance. [relevant rubric item: “usage of evaluation metrics”]

I will use precision and recall for my evaluation metrics. As this metrics can identify the accuracy of skewed data. From the performance that I got, I have good precision and low recall. That means of all the time POI shows up, I am able to identify him or her. But I flag non-POI as POI when it shouldn't be.
