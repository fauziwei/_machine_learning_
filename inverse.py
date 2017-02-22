import numpy as np

m = np.matrix('1 2; 3 4')
print(m)

# inv_m = np.linalg.inv(m)
# print(inv_m)
try:
	inv_m = np.linalg.inv(m)
except np.linalg.LinAlgError:
	# Not invertible. Skip
	pass
else:
	# Continue with what you were doing
	pass
finally:
	print (inv_m)