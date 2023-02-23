import argparse
from pytube import YouTube

def download_video(url, output_path=None):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()

        

        print(f"Downloading video: {yt.title} ({stream.resolution})")
        stream.download()
        print("Video downloaded successfully!")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download a video from YouTube.")
    parser.add_argument("url", help="YouTube video URL")
    args = parser.parse_args()

    download_video(args.url)
