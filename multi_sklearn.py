import numpy as np
from sklearn.linear_model import LinearRegression


# X_train = np.matrix([[1], [3], [5]])
# y_train = np.matrix([[2], [4], [6]])
# X_test  = np.matrix([[1], [3], [5]])

X_train = np.matrix([[1, 2], [3, 4], [5, 6]])
y_train = np.matrix([[2], [4], [6]])
X_test  = np.matrix([[1, 2], [3, 4], [5, 6]])

# X_train = np.matrix([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
# y_train = np.matrix([[2], [4], [6]])
# X_test = np.matrix([[1, 2, 3], [3, 4, 5], [5, 6, 7]])

# X_train = np.matrix([[4.0], [4.5], [5.0], [5.5], [6.0], [6.5], [7.0]])
# y_train = np.matrix([[33], [42], [45], [51], [53], [61], [62]])
# X_test = np.matrix([[4.0], [4.5], [5.0], [5.5], [6.0], [6.5], [7.0]])

# X_train = np.matrix([[6], [7], [8], [9], [7]])
# y_train = np.matrix([[1], [2], [3], [3], [4]])
# X_test = np.matrix([[6], [7], [8], [9], [7]])



clf = LinearRegression()
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
print (predictions)