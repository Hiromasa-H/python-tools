import cv2
import argparse

def downsample_video(input_video_path, output_video_path, original_resolution, downscaled_resolution):
    # Open the video file
    video_capture = cv2.VideoCapture(input_video_path)
    
    # Get the original frame width and height
    original_width, original_height = original_resolution
    
    # Create a VideoWriter object to save the downscaled video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, 20.0, downscaled_resolution)
    
    while True:
        # Read a frame from the video
        ret, frame = video_capture.read()
        if not ret:
            break
        
        # Resize the frame to the downscaled resolution
        frame = cv2.resize(frame, downscaled_resolution)
        
        # Write the downscaled frame to the output video file
        out.write(frame)
        
    # Release the VideoCapture and VideoWriter objects
    video_capture.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Downsample a video")
    parser.add_argument("input_video", type=str, help="Path to the input video")
    parser.add_argument("output_video", type=str, help="Path to save the output video")
    parser.add_argument("original_resolution", type=int, nargs=2, help="Original resolution of the video (width height)")
    parser.add_argument("downscaled_resolution", type=int, nargs=2, help="Resolution to downscale the video to (width height)")
    args = parser.parse_args()

    downsample_video(args.input_video, args.output_video, tuple(args.original_resolution), tuple(args.downscaled_resolution))
