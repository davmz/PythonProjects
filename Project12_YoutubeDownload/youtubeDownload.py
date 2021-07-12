"""
Name: David Montanez
Reason: YouTube MP4 Downloader
Created: July 10, 2021
Updated: July 12, 2021
"""

import time

# pytube documentation: https://pytube.io/en/latest/index.html
# pip install pytube
from pytube import YouTube

print("YouTube Video Download")
print("Please enter the URL of the video you want to download...")
time.sleep(1)

youtubeVideoURL = input("\nYouTube Video Link: ")

try:
    downloadVideo = YouTube(youtubeVideoURL)
    videoTitle = downloadVideo.title
    videoThumbnail = downloadVideo.thumbnail_url
    
    downloadVideo.streams.first().download()
    time.sleep(2)

    print(f"\nVideo Title: {videoTitle}")
    print(f"VideoThumbnail: {videoThumbnail}")

    print("\nVideo Downloaded! Enjoy :)")
except:
    print("\nThat is not a valid YouTube URL!")

