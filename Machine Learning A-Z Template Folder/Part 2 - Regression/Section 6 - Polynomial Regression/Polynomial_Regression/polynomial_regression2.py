# Polynomial Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values # upper bound of range always excluded, this makes sure it's a matrix and NOT a vector
y = dataset.iloc[:, 2].values

# Splitting the dataset into the Training set and Test set (not needed in this case because so few data points)
"""from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)"""

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Linear Regression to dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Fitting polynomial regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 10) # increasing polynomial degree increases accuracy of regression model
X_poly = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly,y)

# Visualising the linear regression results
plt.scatter(X, y, color = 'red')
plt.plot(X,lin_reg.predict(X), color = 'blue')
plt.title('Truth or Bluff? (Linear Regression)')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()

# Visualising the polynomial regression results
X_grid = np.arange(min(X), max(X), 0.1) # increasing accuracy of graph
X_grid = X_grid.reshape(len(X_grid),1) # converting into vector; need to use this somewhere down below, not sure where, see video for reference
plt.scatter(X, y, color = 'red')
plt.plot(X,lin_reg_2.predict(X_poly), color = 'blue')
plt.title('Truth or Bluff? (Polynomial Regression)')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()

# Predicting a new result with linear regression
print(lin_reg.predict(6.5))

# Predicting a new result with polynomial regression
print(lin_reg_2.predict(poly_reg.fit_transform(6.5)))












