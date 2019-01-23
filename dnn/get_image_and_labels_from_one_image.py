import classification_and_labeling_functions as classif
import os
#import sys
import numpy                   as np
import tables                  as tb
from   invisible_cities.io                import mcinfo_io
from   antea.io                           import mc_io

def get_images_and_labels(num_file):
    dirname='/home/DATA/PETALO/pitch4mm/'
    #num_file = int(sys.argv[1])

    files = os.listdir(dirname)
    input_file= dirname + files[num_file]
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
    file_name="training_file_{}".format(num_file)+"_pitch4mm.npz"
    print('saving file named as ', file_name)
    np.savez_compressed(file_name,labels=labels, images=images, event_number= events)
