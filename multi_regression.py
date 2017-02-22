import numpy as np
import traceback

class Miso:

	# Curve fitting
	def fit(self, X, y):
		# B = inv(X'X) * X'Y

		# coeffisien A insert in 1st row
		coef_a = [[1]] * len(X)
		# X = np.insert(X, [0], [[1], [1], [1], [1], [1]], axis=1)
		X = np.insert(X, [0], coef_a, axis=1)
		print('X: %s' % X)

		xt = np.transpose(X)
		print('X\': %s' % xt)

		print('y: %s' % y)

		try:
			xtx = xt * X
			print('xtx: %s' % xtx)
			# xtinv = np.linalg.inv(xtx)
			# print('xtinv: %s' % xtinv)
		except np.linalg.LinAlgError:
			traceback.print_exc()
			return

		# xty = xt * y
		# print('xty: %s' % xty)
		# self.b = xtinv * xty
		# print('b: %s' % self.b)

	# def predict(self, X):
	# 	coef_a = [[1]] * len(X)
	# 	X = np.insert(X, [0], coef_a, axis=1)

	# 	self.predictions = X * self.b
	# 	return self.predictions


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



clf = Miso()
clf.fit(X_train, y_train)
# predictions = clf.predict(X_test)
# print (predictions)