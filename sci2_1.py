import os
import numpy as np
import matplotlib
matplotlib.use('WxAgg')
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from 	 sklearn.linear_model import LinearRegression
from   sklearn.neighbors import KNeighborsClassifier
from   sklearn.svm import SVC
from   sklearn.naive_bayes import GaussianNB

basedir = os.path.abspath(os.path.dirname(__file__))

# time  hightempr  lowtempr  avgtempr   humidity  rainlevel
filedata1 = os.path.join(basedir, 'data', 'data1.txt')
filedata2 = os.path.join(basedir, 'data', 'data2.txt')

# time  hightempr  lowtempr  avgtempr   humidity  rainlevel
filedata3 = os.path.join(basedir, 'data', 'data3.txt')
filedata4 = os.path.join(basedir, 'data', 'data4.txt')

class Helper:

	@staticmethod
	def get_data(filename):
		data = []
		with open(filename) as lines:
			for line in lines:
				data.append(line)
		return data

data1 = Helper.get_data(filedata1)
data2 = Helper.get_data(filedata2)

tempr1 = []
for i, line in enumerate(data1):
	line  = line.split('\t')
	dt_in = line[0]
	hightempr = float(line[1])
	lowtempr  = float(line[2])
	avgtempr  = float(line[3])
	humidity  = float(line[4])
	rainlevel = float(line[5])
	tempr1.append([ hightempr, lowtempr, avgtempr, humidity, rainlevel ])
	# tempr1.append([ hightempr, lowtempr, avgtempr, humidity ])

	# year  = int(dt_in[0:4])
	# tempr4.append(line)
	# print('line: {}'.format(line))



X_train = []
y_train = []
all_data = []

power = []
min_power = []
max_power = []
avg_power = []
diff_power = []
payload_power = []

for i, line in enumerate(data2):
	line = line.split('\t')
	# dt_in = int(line[0])
	dt_in = line[0]
	year = int(dt_in[0:4])
	mon  = dt_in[4:6].zfill(2)
	day  = dt_in[6:8].zfill(2)

	# tempr_line = tempr1[i]
	# hightempr  = float(tempr_line[0])
	# lowtempr   = float(tempr_line[1])
	# avgtempr   = float(tempr_line[2])
	# humidity   = float(tempr_line[3])
	# rainlevel  = float(tempr_line[4])
	# print ('tempr_line: %s' % tempr_line)
	# print ('%s lowtempr: %s' % (i, lowtempr))

	
	for i in range(1, 96):
		power.extend([float(line[i])])


	for p in power:
		min_power.extend([min(power)])
		max_power.extend([max(power)])
		avg_power.extend([np.average(power)])
		diff_power.extend([max(power)-min(power)])
		payload_power.extend([np.mean(power)/max(power)])


		# X_train.append([dt_in, i])
		# X_train.append([dt_in, i, float(line[i]) ])
		# X_train.append([ year, int(mon), int(day), i, float(line[i]) ])
		# X_train.append([ year, int(mon), int(day), i, float(line[i]), hightempr, lowtempr, avgtempr, humidity, rainlevel ])
		# X_train.append([ year, int(mon), int(day), i, float(line[i]), hightempr, lowtempr, avgtempr, humidity ])
		# X_train.append([ year, int(mon), int(day), i, float(line[i]), hightempr, lowtempr, avgtempr ])
		# y_train.append([ float(line[i]) ])


# classifier = 'linear_regression'
# clf = None
# if classifier == 'linear_regression':
# 	clf = LinearRegression()
# clf.fit(X_train, np.array(y_train).ravel())


# Sample X_test
# X_test = ([ 20141230, 2 ])
# X_test = X_train
# predictions = clf.predict(X_test)

# predicted = []
# for i, prediction in enumerate(predictions):
# 	print ('real_output:' + str(y_train[i]) + ' ' + 'prediction: ' +str(prediction))
# 	predicted.append(prediction)


# y_train = [ int(i[0]) for i in y_train ]
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.set_title('Real data 2014')
# ax.set_xlabel('Time, 15 minutes interval')
# ax.set_ylabel('Real data')
# # ax.legend('real data 2014')
# ax.plot(y_train)
# ax.grid(True)
# plt.show()
# predicted = [ int(i) for i in predicted ]
# print('len real: %s' % len(y_train))
# print('len pred: %s' % len(predicted))

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.set_title('Prediction')
# ax.set_xlabel('Time, 15 minutes interval')
# ax.set_ylabel('Real & Prediction')
# ax.grid(True)
# p1 = ax.plot(y_train)
# p2 = ax.plot(predicted)
# ax.legend((p1[0], p2[0]), ('real data', 'predictions'), loc='best', fancybox=True, framealpha=0.5)
# plt.show()


# Question?
# 	20150111
# 	20150112
# 	20150113
# 	20150114
# 	20150115
# 	20150116
# 	20150117
# X_test = []
# for line in X_train:
# 	X_test.append([ 2015, line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9] ])
# 	# if line[0] == 2014 and line[1] == 1 and \
# 	# 	(line[2] == 11 or line[2] == 12 or \
# 	# 		line[2] == 13 or line[2] == 14 or \
# 	# 		line[2] == 15 or line[2] == 16 or line[2] == 17):

# 	# 	X_test.append([ 2015, line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9] ])


# # print ('X_test: %s' % X_test)
# predictions = clf.predict(X_test)

# y_cut = []
# predicted = []
# for i, prediction in enumerate(predictions):
# 	y_cut.append(y_train[i])
# 	# print ('real_output:' + str(y_train[i]) + ' ' + 'prediction: ' +str(prediction))
# 	predicted.append(prediction)

# y_cut = [ int(i[0]) for i in y_cut ]
# predicted = [ int(i) for i in predicted ]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Power')
ax.set_xlabel('Time, 15 minutes interval')
ax.set_ylabel('Power')
ax.grid(True)
p1 = ax.plot(min_power)
p2 = ax.plot(max_power)
p3 = ax.plot(avg_power)
p4 = ax.plot(diff_power)
p5 = ax.plot(payload_power)
p6 = ax.plot(power)
ax.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0]), ('min power', 'max power', 'avg power', 'diff power', 'payload power', 'power'), loc='best', fancybox=True, framealpha=0.5)
plt.show()