from moviepy import VideoFileClip

def mp4_to_compressed_gif(input_mp4: str, output_gif: str, fps: int = 10, scale: float = 0.25):
    """
    Converts the first 30 seconds of an MP4 file into a compressed animated GIF.
    
    Args:
        input_mp4 (str): Path to the input MP4 file.
        output_gif (str): Path to save the output GIF.
        fps (int): Frames per second for the GIF. Default is 5.
        scale (float): Scale factor for resizing the GIF. Default is 0.25 (25% size).
    """
    try:
        # Load the video file
        clip = VideoFileClip(input_mp4).subclipped(0, 30)  # Select the first 30 seconds
        
        # Resize the clip for compression
        clip_resized = clip.resized(scale)  # Scale the video size
        
        # Write the GIF file
        clip_resized.write_gif(output_gif, fps=fps)
        print(f"GIF successfully created: {output_gif}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
mp4_to_compressed_gif("in.mp4", "out.gif")
