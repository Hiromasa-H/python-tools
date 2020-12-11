import cv2
import sys, getopt


def main(argv):
    # get arguments for inputfile and directory
    inputfile = ""
    outputfile = ""
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print("test.py -i <inputfile> -o <outputdirectory>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":  # help option
            print("test.py -i <inputfile> -o <outputdirectory>")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputdirectory = arg
    print('Input file is "', inputfile)
    print('Output directory is "', outputdirectory)

    # cut frames.
    vidcap = cv2.VideoCapture(inputfile)
    total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    success, image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite(
            f"{outputdirectory}/frame{count}.jpg", image
        )  # save frame as JPEG file
        success, image = vidcap.read()
        # print("Read a new frame: ", success)

        # progress bar
        sys.stdout.write("\r")
        sp = count / ((total_frames - 1) / 100)
        tp = int(sp / 4)
        sys.stdout.write("[%-25s] %d%%" % ("=" * tp, sp))  # 20s=20spaces
        sys.stdout.flush()

        count += 1
    print("   finished.")


if __name__ == "__main__":
    main(sys.argv[1:])
