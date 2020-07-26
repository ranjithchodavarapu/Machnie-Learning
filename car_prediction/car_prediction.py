import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import ExtraTreesRegressor,RandomForestRegressor
import pickle


data=pd.read_csv("datasets_33080_1320127_car data.csv")
data.drop(['Car_Name'],axis=1,inplace=True)
data["Current_year"]=2020
data['No of Years']=data['Current_year']-data['Year']

data.drop(['Year','Current_year'],axis=1,inplace=True)

data=pd.get_dummies(data,drop_first=True)

print(data.corr())

#print(sns.pairplot(data))

cor=data.corr()
fe=cor.index
plt.figure(figsize=(15,15))
g=sns.heatmap(data[fe].corr(),annot=True)
#print(g)
print(data.head(5))



x=data.drop(['Selling_Price'],axis=1)
y=data['Selling_Price']

print(x.head())

print(y.head())

model=ExtraTreesRegressor()
model.fit(x,y)
print(model.feature_importances_)

fet=pd.Series(model.feature_importances_,index=x.columns)
fet.nlargest(5).plot(kind='barh')
plt.show()

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)
print(x_train,y_train)


cls=RandomForestRegressor(n_estimators=100)

cls.fit(x_train,y_train)

pre=cls.predict(x_test)
print(pre)

print(sns.distplot((y_test,pre)))

plt.scatter(y_test,pre)
plt.show()

print(sklearn.metrics.mean_squared_error(y_test,pre))
print(sklearn.metrics.mean_absolute_error(y_test,pre))
print(cls.score(x_test,y_test))

file=open("random.pickel","wb")
pickle.dump(cls,file)
