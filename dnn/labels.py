import os
import tables as tb
from invisible_cities.io import mcinfo_io

def labeling(event):

	return label


dirname = '/home/adriana/Petalo_dnn/data/'
input_file = dirname + os.listdir(dirname)[0]

# Abrir el archivo h5 como una tabla
mytable = tb.open_file(input_file, mode='r')

# Abrir la tabla usando mcinfo
mcinfo = mcinfo_io.read_mcinfo(mytable)

print(type(mcinfo))
