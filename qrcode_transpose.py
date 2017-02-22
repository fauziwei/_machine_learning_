import qrcode
import numpy as np

device_id = 'A2222222'

qr = qrcode.QRCode(
	version=1,
	error_correction=qrcode.constants.ERROR_CORRECT_L,
	border=0,
)
qr.add_data(device_id)
qr.make(fit=True)
matrixs = qr.get_matrix()[0:len(qr.get_matrix())]
#print matrixs

m = np.array(matrixs)
m_trans = m.transpose()
#print m
#print m_trans

serialize = ''
for matrix in m_trans:
	for m in matrix:
		m = 1 if m == False else 0
		serialize += str(m)
print serialize