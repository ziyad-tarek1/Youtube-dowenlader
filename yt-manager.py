import os
from yt_dlp import YoutubeDL

def download_video(url, download_dir):
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Download completed successfully for: {url}")
    except Exception as e:
        print(f"An error occurred while downloading {url}: {str(e)}")

def main():
    print("Enter the path to save the videos: ")
    download_dir = input().strip()

    print("Choose an option:\n1) Download a playlist\n2) Download a single video")
    choice = input("Enter 1 or 2: ").strip()

    if choice == '1':
        print("Enter the Playlist URL: ")
        url = input().strip()
        download_video(url, download_dir)
    elif choice == '2':
        print("Enter the Video URL: ")
        url = input().strip()
        download_video(url, download_dir)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
