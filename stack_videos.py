import os
import sys, getopt


def main(argv):
    # get arguments for inputfile and directory
    inputfiles = []
    outputfile = "not specified"
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print(
            "test.py -i <inputfile1 path> <inputfile2 path> [inputfile3 path] [inputfile4 path] -o <outputfile path>"
        )
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":  # help option
            print(
                "video_to_frames.py -i <inputfile1 path> <inputfile2 path> [inputfile3 path] [inputfile4 path]  -o <outputfile path>"
            )
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfiles.append(arg)
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print("Input directories are :", inputfiles)
    print("Output file is :", outputfile)

    if len(inputfiles) == 2:
        cmd = f"ffmpeg -i {inputfiles[0]} -i {inputfiles[1]} -filter_complex '[0]pad=iw+5:color=black[left];[left][1]hstack=inputs=2' {outputfile}"
    elif len(inputfiles) == 4:
        # cmd = f'ffmpeg -i {inputfiles[0]} -i {inputfiles[1]} -i {inputfiles[2]} -i {inputfiles[3]} -filter_complex \
        #         "[0:v][1:v]hstack[top]; \
        #         [2:v][3:v]hstack[bottom]; \
        #         [top][bottom]vstack,format=yuv420p[v]; \
        #         [0:a][1:a][2:a][3:a]amerge=inputs=4[a]" \
        #         -map "[v]" -map "[a]" -ac 2 {outputfile}'
        cmd = f'ffmpeg -i {inputfiles[0]} -i {inputfiles[1]} -i {inputfiles[2]} -i {inputfiles[3]} -filter_complex "[0:v][1:v][2:v][3:v]xstack=inputs=4:layout=0_0|w0_0|0_h0|w0_h0[v]" -map "[v]" {outputfile}'

    else:
        print("The number of inputs files must either be 2 or 4")
        cmd = "pwd"

    os.system(cmd)

    print("done")


# ffmpeg -i efficientdet_0.mp4 -i efficientdet_8.mp4 -filter_complex "[0]pad=iw+5:color=black[left];[left][1]hstack=inputs=2" output

if __name__ == "__main__":
    main(sys.argv[1:])

#for later use
# ffmpeg -i input0 -i input1 -i input2 -i input3 -filter_complex
# "[0]drawtext=text='vid0':fontsize=20:x=(w-text_w)/2:y=(h-text_h)/2[v0];
#  [1]drawtext=text='vid1':fontsize=20:x=(w-text_w)/2:y=(h-text_h)/2[v1];
#  [2]drawtext=text='vid2':fontsize=20:x=(w-text_w)/2:y=(h-text_h)/2[v2];
#  [3]drawtext=text='vid3':fontsize=20:x=(w-text_w)/2:y=(h-text_h)/2[v3];
#  [v0][v1][v2][v3]xstack=inputs=4:layout=0_0|w0_0|0_h0|w0_h0[v]"
# -map "[v]" output