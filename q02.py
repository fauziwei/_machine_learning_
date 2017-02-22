import string
import random
import qrcode
# import cv2
from PIL import Image
from numpy import transpose
import numpy
from cStringIO import StringIO
import binascii
import pyqrcode
import qrtools
import zbar

# TEST python2 (env) in mongo40

# sudo apt-get install python-qrtools
# pip install qrtools --trusted-host mirrors.aliyun.com
# pip install zbar --trusted-host mirrors.aliyun.com
# pip install pyqrcode --trusted-host mirrors.aliyun.com
# pip install qrcode --trusted-host mirrors.aliyun.com
# pip install pillow --trusted-host mirrors.aliyun.com
# pip install numpy --trusted-host mirrors.aliyun.com

def generateDeviceId(new_device_id):
	device_id = ''
	strg = string.uppercase
	num = ''.join(str(i) for i in range(10))
	if new_device_id[0] == 'A':
		device_id = 'A'
		for i in range(7):
			device_id += str(random.choice(strg+num))
	elif new_device_id[0] == 'B':
		device_id = 'B'
		for i in range(7):
			device_id += str(random.choice(strg+num))
	else: pass
	return device_id

def generateQrCode21x21(device_id):
	qr = qrcode.QRCode(
		version=1,
		error_correction=qrcode.constants.ERROR_CORRECT_L,
		border=0,
	)
	qr.add_data(device_id)
	qr.make(fit=True)
	# print 'matrix: %s' % qr.get_matrix()
	matrixs = qr.get_matrix()[0:len(qr.get_matrix())]
	serialize = ''
	for matrix in transpose(matrixs):
		for m in matrix:
			m = 1 if m == False else 0
			serialize += str(m)
	return serialize


d = generateDeviceId('AAAAAAAA')
q = generateQrCode21x21(d)
print len(q)

# f = open('qr.jpg', 'rb').read()
# im = cv2.imread('qr.jpg')
# print im
# I = numpy.asarray(Image.open('qr.jpg'))
# print I

# def hex2bin(str):
# 	bin = ['0000','0001','0010','0011',
# 				'0100','0101','0110','0111',
# 				'1000','1001','1010','1011',
# 				'1100','1101','1110','1111']
# 	aa = ''
# 	for i in range(len(str)):
# 		aa += bin[string.atoi(str[i],base=16)]
# 	return aa

# buffer = StringIO()
# im = Image.open('qr.jpg')
# im.save(buffer, 'JPEG')
# h = binascii.hexlify(buffer.getvalue())
# buffer.close()
# # print hex2bin(h)

qr = qrtools.QR()
qr.decode('qr.jpg')
print qr.data
d = generateQrCode21x21(qr.data)
print len(d)