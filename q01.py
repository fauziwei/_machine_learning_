import sys
import qrcode
from cStringIO import StringIO
import binascii
import string
import platform
if platform.system() is 'Windows': import Image
else: from PIL import Image


#hexa = '91278c4bfb3cbb95ffddc668d995bfe0'
#binary = bin(int(hexa, 16))[2:]
#print binary
#hexa_dec = hex(int(binary, 2))[2:]
#print hexa_dec


#data = ""
#while len(h) > 0:
#    data = data + chr(int(h[0:2], 16))
#    h = h[2:]
#print h


def ascii2bin(a):
	ai = ord(a)
	return ''.join('01'[(ai >> x) & 1] for x in xrange(7, -1, -1))
	''' to use:
		aa = ''
		for i in xrange(len(fulldata)):
			aa += ascii2bin(fulldata[i])
		print aa
	'''

def hex2bin(str):
	bin = ['0000','0001','0010','0011',
		'0100','0101','0110','0111',
		'1000','1001','1010','1011',
		'1100','1101','1110','1111']
	aa = ''
	for i in xrange(len(str)):
		aa += bin[string.atoi(str[i], base=16)]
	return aa


# https://github.com/lincolnloop/python-qrcode/blob/master/qrcode/tests/test_qrcode.py

#device_id = 'A1111111'
device_id = 'A2222222'
#qr = qrcode.QRCode(
#    version=1,
#    error_correction=qrcode.constants.ERROR_CORRECT_L,
#    box_size=10,
#    border=4,
#)
qr = qrcode.QRCode(
	version=1,
	error_correction=qrcode.constants.ERROR_CORRECT_L,
	border=0)
qr.add_data(device_id)
qr.make(fit=True)
matrixs = qr.get_matrix()[0:len(qr.get_matrix())]
#print matrixs
serialize = ''
for matrix in matrixs:
	for m in matrix:
		m = 1 if m == False else 0
		serialize += str(m)
print serialize
print sys.getsizeof(serialize)
#m_hex = hex(int(serialize, 2))
#m_hex = m_hex.replace('0x', '')
#m_hex = m_hex.rstrip('L').lstrip('0x') or 0
#print m_hex


#matrix = [row[1:-1] for row in qr.get_matrix()[1:-1]]
#print matrix

#img = qr.make_image()
#img.save(device_id+'.jpeg')

#buffer = StringIO()
#img.save(buffer, 'JPEG')
#img_hex = binascii.b2a_hex(buffer.getvalue())
#print img_hex

# 1st
#aa = ''
#for i in xrange(len(img_hex)):
#	aa += ascii2bin(img_hex[i])
#print aa

#f = open('file.txt', 'w')
#f.write('%s' % aa)
#f.close()

# 2nd
#print hex2bin(img_hex)