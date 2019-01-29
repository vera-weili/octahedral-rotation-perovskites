import sys
import os
from os.path import dirname, realpath
import shutil
import operator
import numpy as np
from numpy import dot
from numpy.linalg import norm

#


def write_poscar(i_value):
    # write the POSCAR for one bond angle by moving the Zr and S position
    file = open("POSCAR", "w")
    file.write(
        "Ba Zr S\n"
        "1.000000000\n"
        "6.9192722370057664    0.0000000000000000    0.0000000000000000\n"
        "-0.0000000000000000    6.9192722370057664   -0.0000000000000000\n"
        "0.0000000000000000    0.0000000000000000   10.1651300682595469\n"
        "Ba Zr S\n"
        "  4  4  12\n"
        "Direct\n"
        "0.5000000000000000  0.0000000000000000  0.2500000000000000 Ba\n"
        "0.0000000000000000  0.5000000000000000  0.2500000000000000 Ba\n"
        "0.0000000000000000  0.5000000000000000  0.7500000000000000 Ba\n"
        "0.5000000000000000  0.0000000000000000  0.7500000000000000 Ba\n"
        "0.5000000000000000  0.5000000000000000  0.0000000000000000 Zr\n"
        "0.0000000000000000  0.0000000000000000  0.0000000000000000 Zr\n"
        "0.0000000000000000  0.0000000000000000  0.5000000000000000 Zr\n"
        "0.5000000000000000  0.5000000000000000  0.5000000000000000 Zr\n"
        + str(0.75+i_value) + " " + str(0.25+i_value) + " 0.0000000000000000 S\n"
        + str(0.75-i_value) + " " + str(0.75+i_value) + " 0.0000000000000000 S\n"
        + str(0.25+i_value) + " " + str(0.25-i_value) + " 0.0000000000000000 S\n"
        + str(0.25-i_value) + " " + str(0.75-i_value) + " 0.0000000000000000 S\n"
        "0.0000000000000000  0.0000000000000000  0.2500000000000000 S\n"
        "0.5000000000000000  0.5000000000000000  0.2500000000000000 S\n"
        "0.5000000000000000  0.5000000000000000  0.7500000000000000 S\n"
        "0.0000000000000000  0.0000000000000000  0.7500000000000000 S\n"
        + str(0.25+i_value) + " " + str(0.75+i_value) + " 0.5000000000000000 S\n"
        + str(0.25-i_value) + " " + str(0.25+i_value) + " 0.5000000000000000 S\n"
        + str(0.75+i_value) + " " + str(0.75-i_value) + " 0.5000000000000000 S\n"
        + str(0.75-i_value) + " " + str(0.25-i_value) + " 0.5000000000000000 S\n"
    )
    print(file)
    file.close()


def value(num):
    num = int(num)
    i_value = 0.001

    for _ in range(1, num):

        # creat and cd to the i_value directory
        try:
            os.mkdir("{0:.3f}".format(i_value))
        except:
            print("{0:.3f} already exists.".format(i_value))
        os.chdir("{0:.3f}".format(i_value))

        # Copy input files to the created directory
        curr_folder = dirname(realpath(__file__))
        # print('current is:', curr_folder)
        curr_folder_list = curr_folder.split('/')
        # print(curr_folder_list)
        parent_folder = '/'.join(curr_folder_list[:-1])
        # print('parent_folder is:', parent_folder)

        # shutil.copyfile(parent_folder+'/INCAR', curr_folder+'/INCAR')
        # shutil.copyfile(parent_folder+'/POTCAR', curr_folder+'/POTCAR')
        # shutil.copyfile(parent_folder+'/KPOINTS', curr_folder+'/KPOINTS')
        # shutil.copyfile(parent_folder + '/bandgap.sh', curr_folder + '/bandgap.sh')

        write_poscar(i_value)

        # calculate Zr-S-Zr bond angle
        zr1_vector = [0.0000000000000000,  0.0000000000000000]
        zr2_vector = [0.5000000000000000,  0.5000000000000000]
        s_vector = [i_value+0.25, 0.25-i_value]
        zr1_s_vector = list(map(operator.sub,zr1_vector,s_vector))
        zr2_s_vector = list(map(operator.sub,zr2_vector,s_vector))
        cos_sim = dot(zr1_s_vector, zr2_s_vector)/(norm(zr1_s_vector)*norm(zr2_s_vector))
        bond_angle = np.arccos(cos_sim)*360/np.pi/2

        # write the bond angle to a file so that I can cat it later
        fh = open("bond_angle","w")
        fh.write(str(bond_angle))

        # end of one calculation, start the loop
        os.chdir('..')
        i_value += 0.001

        if i_value >= 0.20:
            break

    return i_value

print(value(sys.argv[1]))




