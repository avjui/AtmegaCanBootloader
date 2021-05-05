import os
import shutil

dir_path = os.path.dirname(os.path.realpath(__file__))
working_path = os.path.join(dir_path, "bootloader_atmega32_16Mhz_mcp2515_8MHz_CS_B2")
bin_path = os.path.join(dir_path, "bin")
output_path = os.path.join(dir_path, "output")

shutil.rmtree(output_path, ignore_errors=True)
os.makedirs(output_path)

for files in os.listdir(bin_path):
    with open(os.path.join(bin_path, files)) as fp:
        lines_fp = fp.readlines()
        lines_fp = lines_fp[:-1]
        for directory in os.listdir(working_path):
            if directory.startswith("ID_"):
                print(directory)
                with open(os.path.join(working_path, directory, "bootloader.hex")) as fb:
                    lines_fb = fb.readlines()
                os.makedirs(os.path.join(output_path, directory))
                with open(os.path.join(output_path, directory, files[:-4] + "_with_bootloader.hex"), "w") as ff:
                    for l in lines_fp:
                        ff.write(l)
                    for lb in lines_fb:
                        ff.write(lb)
