import classification_and_labeling_functions as classif
import os
import numpy                   as np
import tables                  as tb
from   invisible_cities.io                import mcinfo_io
from   antea.io                           import mc_io


dirname='/home/DATA/PETALO/pitch4mm/'

files = os.listdir(dirname)
input_file= dirname + files[0]
print('The input file is', input_file)

mytable = tb.open_file(input_file,mode='r')

print('---------------------read mytable-------------------------')
mcinfo     = mcinfo_io.read_mcinfo(mytable)
pos_dict   = classif.get_pos_dict(mytable)
en_dict    = classif.get_evt_energy(mytable)

print('---------------------read waveforms-------------------------')
waveforms = mc_io.read_mcsns_response(input_file)

print('----------------getting images with labels------------------')
labels, images, events = classif.get_images_with_labels(mcinfo, en_dict, waveforms, pos_dict)

print('-------------- saving ------------')
training_set_test="training_set_test_pitch4mm_file0.npz"
np.savez_compressed(training_set_test, labels=labels, images=images, event_number= events)
