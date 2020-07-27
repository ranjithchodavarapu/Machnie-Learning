import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn
from sklearn import datasets
from sklearn.ensemble import ExtraTreesClassifier,RandomForestClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier



iris=pd.read_csv("datasets_17860_23404_IRIS.csv")
print(iris.head(5))

print(iris.describe())
print(iris.info())
print(iris.isnull().sum())

print(iris.corr())

cor=iris.corr()
a=cor.index
plt.figure(figsize=(20,20))
xr=sns.heatmap(iris[a].corr(),annot=True)

x=iris.drop(['species'],axis=1)
y=iris['species']

model=ExtraTreesClassifier()
model.fit(x,y)
print(model.feature_importances_)

fet=pd.Series(model.feature_importances_,index=x.columns)
fet.nlargest(5).plot(kind='barh')
#plt.show()


x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)
print(x_train,y_train)
cls=SVC(kernel='linear')
cls.fit(x_train,y_train)

pre=cls.predict(x_test)
print(y_test)
print(pre)


print(sklearn.metrics.accuracy_score(y_test,pre))
print(sklearn.metrics.classification_report(y_test,pre))
