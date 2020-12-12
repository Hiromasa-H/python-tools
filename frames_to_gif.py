from PIL import Image
import sys, getopt
import os
from os import listdir

def main(argv):
    # get arguments for inputfile and directory
    inputdirectory = "not specified"
    outputfile = "not specified"
    output_fps = 16.5
    try:
        opts, args = getopt.getopt(argv, "hi:o:f:", ["ifile=", "ofile=", "ofps="])
    except getopt.GetoptError:
        print("test.py -i <inputdirectory> -o <outputdirectory> -f <outputfile fps>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":  # help option
            print("frames_to_gif.py -i <inputdirectory path> -o <outputdirectory path> -f <outputfile fps>")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputdirectory = arg
        elif opt in ("-o", "--ofile"):          
            outputfile = arg
        elif opt in ("-f", "--ofps"):            
            output_fps = arg
    print('Input directory is :', inputdirectory)
    print('Output file is :', outputfile)
    print('Ouput file fps is :',output_fps)

    #read and make gif
    images = []
    list_of_files = [file for file in listdir(inputdirectory)]
    list_of_files.sort(key=lambda x: os.path.getmtime(f'{inputdirectory}/{x}'))# = sorted(list_of_files)
    # print(list_of_files)

    for i, frame in enumerate(list_of_files):
      im = Image.open(f"{inputdirectory}/{frame}")
      images.append(im)

      sys.stdout.write("\r")
      sp = i / (len(list_of_files) / 100)
      tp = int(sp / 4)
      sys.stdout.write("[%-25s] %d%% " % ("=" * tp, sp))  # 20s=20spaces
      sys.stdout.flush()

    duration = int(1000 / int(output_fps))

    print("\nsaving gif file...")

    images[0].save(outputfile,
               save_all=True, append_images=images[1:], optimize=False,duration=duration, loop=0)

    print("\nfinished.")


if __name__ == "__main__":
    main(sys.argv[1:])