import cv2
import numpy as np
import glob
import sys, getopt
import os
from os import listdir
from utils import natural_keys

def main(argv):
    # get arguments for inputdirectory and outputfile
    inputdirectory = "not specified"
    outputfile = "not specified"
    output_fps_default = 30
    output_fps = output_fps_default
    try:
        opts, args = getopt.getopt(argv, "hi:o:f:", ["ifile=", "ofile=", "ofps="])
    except getopt.GetoptError:
        print("test.py -i <inputdirectory> -o <outputfile> -f <outputfile fps>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":  # help option
            print("frames_to_gif.py -i <indirectory path> -o <outputfile path> -f <outputfile fps>")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputdirectory = arg
        elif opt in ("-o", "--ofile"):          
            outputfile = arg
        elif opt in ("-f", "--ofps"):            
            output_fps = int(arg)
    print('Input directory is :', inputdirectory)
    print('Output file is :', outputfile)
    print('Ouput file fps is :',output_fps)

    print("collecting image frames...")

    # images = [img for img in os.listdir(inputdirectory)]
    # frame = cv2.imread(os.path.join(inputdirectory, images[0]))
    # height, width, layers = frame.shape

    # fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    # video = cv2.VideoWriter(outputfile, fourcc, 1, frameSize=(width,height), fps=output_fps)

    # for image in images:
    #     video.write(cv2.imread(os.path.join(inputdirectory, image)))

    # cv2.destroyAllWindows()
    # video.release()


    img_array = []
    cntr = 0
    list_of_files = [file for file in listdir(inputdirectory)]
    list_of_files.sort(key=natural_keys)
    # list_of_files.sort(key=lambda x: os.path.getmtime(f'{inputdirectory}/{x}'))
    # print(list_of_files)
    
    for filename in list_of_files:#glob.glob(f'{inputdirectory}/*.jpg'):
        if cntr % (output_fps*60) == 0: #30 fps, 1800 frames per min
            print(f"collected {cntr/1800} minutes worth of frames. frame name is: {filename}")
        img = cv2.imread(f"{inputdirectory}/{filename}")
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
        cntr += 1
    if outputfile.split(".")[1]=="mp4":
        fourcc='mp4v'
    elif outputfile.split(".")[1]=="avi":
        fourcc='DIVX'

    out = cv2.VideoWriter(outputfile,cv2.VideoWriter_fourcc(*fourcc), fps=output_fps, frameSize=size)
    
    print("making video...")
    for i, image in enumerate(img_array):
        out.write(image)

        #progress bar
        sys.stdout.write('\r')
        sp = i/((len(img_array)-1)/100)
        tp = int(sp/4)
        sys.stdout.write("[%-25s] %d%%" % ('='*tp, sp)) #25s=25spaces
        sys.stdout.flush()

    out.release()
    print("\nvideo is done")

    # if not output_fps_default == output_fps:
    #     print(f"since the specified output fps was not the default {output_fps_default}fps, this additional step will run.\nNote that this method is not efficient, and will be fixed later")
    #     cap = cv2.VideoCapture(outputfile)
    #     cap.set(cv2.CAP_PROP_FPS, 10)
    #     prev = 0
    #     while capturing:

    #         time_elapsed = time.time() - prev
    #         res, image = cap.read()

    #         if time_elapsed > 1./output_fps:
    #             prev = time.time()

    #             # Do something with your image here.
    #             process_image()


if __name__ == "__main__":
    main(sys.argv[1:])