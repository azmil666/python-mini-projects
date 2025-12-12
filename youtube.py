from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def download_video(url,save_path):
    try:
        yt=YouTube(url)
        streams = yt.streams.filter(progressive=True,file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded sucessfully")

    except Exception as e:    
        print(e)


#url="https://www.youtube.com/watch?v=tF89Y-4S6Wk"

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder    


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Enter a youtube url : ")
    save_dir = open_file_dialog()
    if not save_dir:
        print("Invalid save location...")
    else:
        print("Started downloading...")
        download_video(video_url,save_dir)

    