import os
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
sys.path.append(BASE_DIR)
import indoor3d_util_original

#anno_paths = [line.rstrip() for line in open(os.path.join(BASE_DIR, 'meta/anno_paths.txt'))]
#anno_paths = [os.path.join(indoor3d_util.DATA_PATH, p) for p in anno_paths]

output_folder = os.path.join(ROOT_DIR, 'data/dso_indoor3d') 
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# Note: there is an extra character in the v1.2 data in Area_5/hallway_6. It's fixed manually.
#for anno_path in anno_paths:
print(indoor3d_util_original.DATA_PATH)
try:
    elements = indoor3d_util_original.DATA_PATH.split('/')
    out_filename = elements[-2]+'_'+elements[-1]+'.npy' # Area_1_hallway_1.npy
    #print out_filename;
    indoor3d_util_original.collect_point_label(indoor3d_util_original.DATA_PATH, os.path.join(output_folder, out_filename), 'numpy')
except:
    print(indoor3d_util_original.DATA_PATH, 'ERROR!!')
