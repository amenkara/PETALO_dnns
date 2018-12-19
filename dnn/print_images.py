import classification_functions as clasif
import matplotlib.pyplot       as plt
import os
import tables as tb
from   invisible_cities.io                import mcinfo_io
from   antea.io                           import mc_io

dirname='/home/adriana/Petalo_dnn/data/'
files = os.listdir(dirname)
input_file= dirname + files[0]

mytable = tb.open_file(input_file,mode='r')

print('---------------------read mytable-------------------------')
mcinfo     = mcinfo_io.read_mcinfo(mytable)
pos_dict   = clasif.get_pos_dict(mytable)
en_dict    = clasif.get_evt_energy(mytable)

print('---------------------read waveforms-------------------------')
waveforms = mc_io.read_mcsns_response(input_file)

pos_dict = clasif.get_pos_dict(mytable)

i = 0
for keys in mcinfo.keys():
    i += 1
    if clasif.labeling(mcinfo[keys], clasif.get_evt_energy(mytable)[keys]) is not "None":
        plt.show(clasif.make_2d_image(waveforms[keys], pos_dict))
        print(clasif.labeling(mcinfo[keys], clasif.get_evt_energy(mytable)[keys]))
    if i == 20:
        break
