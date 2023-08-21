
import json
import os 

images_dir = "result_vis_copy"
results_file = "test/stream_petr_vov_flash_800_bs2_seq_24e/Mon_Aug_14_21_03_56_2023/pts_bbox/results_nusc.json"
order_file = "frames_meta.json"

# Read order file json and get list of tokens
with open(order_file, 'r') as file: 
    line = file.readline()
result = line.split('"token": ')

i = 0
for imagename in result: 
    imagename = imagename.split(",")[0].strip('""')
    for filename in os.listdir(images_dir):
        print(filename)
        if imagename in filename: 
            print("found it")
            new_name = os.path.join(images_dir, f"{i}.png")
            os.rename(os.path.join(images_dir, filename), new_name)
            i += 1