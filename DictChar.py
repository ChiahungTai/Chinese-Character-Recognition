#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 16:30:04 2017

@author: ctai
"""

#
#import os
#import numpy as np
#import struct
#from PIL import Image
#
#
#
#data_dir = 'data'
#test_data_dir = os.path.join(data_dir, 'HWDB1_1tst_gnt')
#
#def read_from_gnt_dir(gnt_dir=test_data_dir):
#    def one_file(f):
#        header_size = 10
#        while True:
#            header = np.fromfile(f, dtype='uint8', count=header_size)
#            if not header.size: break
#            sample_size = header[0] + (header[1]<<8) + (header[2]<<16) + (header[3]<<24)
#            tagcode = header[5] + (header[4]<<8)
#            width = header[6] + (header[7]<<8)
#            height = header[8] + (header[9]<<8)
#            if header_size + width*height != sample_size:
#                break
#            image = np.fromfile(f, dtype='uint8', count=width*height).reshape((height, width))
#            yield image, tagcode
#    for file_name in os.listdir(gnt_dir):
#        if file_name.endswith('.gnt'):
#            file_path = os.path.join(gnt_dir, file_name)
#            with open(file_path, 'rb') as f:
#                for image, tagcode in one_file(f):
#                    yield image, tagcode
#char_set = set()
#
#code_char = {}
#
#for _, tagcode in read_from_gnt_dir(gnt_dir=test_data_dir):
#    print("tagcode=", tagcode)
#    tagcode_unicode = struct.pack('>H', tagcode).decode('gb2312')
#    print("tagcode_unicode=", tagcode_unicode)
#    char_set.add(tagcode_unicode)
#    
#print ("char_set", char_set)
#char_list = list(char_set)
#print ("char_list", char_list)
#
#char_dict = dict(zip(sorted(char_list), range(len(char_list))))
#
#print (char_dict)
#
#for key, value in char_dict.items():
#    code_char[value] = key
#    
#print ("code_char", code_char)

import pickle
#fw = open('code_char_dict', 'wb')
#pickle.dump(code_char, fw)
#fw.close()


#fr = open('code_char_dict', 'rb')
#new_code_char = pickle.load(fr)
#fr.close()

fr = open('char_dict', 'rb')

char_dict = pickle.load(fr)
fr.close()

code_char = {}
fw = open('char_list.txt', 'w')

for key, value in char_dict.items():
    code_char[value] = key
    fw.write("%s\n"%key)

fw.close()
