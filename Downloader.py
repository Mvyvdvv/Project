import tkinter as tk
from pytube import YouTube
from tkinter import messagebox

root = tk.Tk()
root.title("Downloader")
root.geometry("600x500")
root.config(bg="black")

label = tk.Label(root, text="Enter Your Youtube Link Here:", font="Tahoma 13 bold", fg="white", bg="black")
label.pack(pady=20)
entry = tk.Entry(root, width=100)
entry.pack()

def download_video(url, quality):
    try:
        yt = YouTube(url)
        if quality == 'high':
            stream = yt.streams.filter(progressive=True, file_extension='mp4', res="1080p").first()
        elif quality == 'low':
            stream = yt.streams.filter(progressive=True, file_extension='mp4', res="360p").first()
        elif quality == "audio":
            stream = yt.streams.filter(only_audio=True).first()
        else:
            messagebox.showerror("Error", "Invalid quality selection. Choose 'high', 'low', or 'audio'.")
            return
        messagebox.showinfo("Download Started", f"Downloading '{yt.title}'...")
        stream.download()
        messagebox.showinfo("Success", "Download complete!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

button1 = tk.Button(root, text="Download in High Quality", fg="black", bg="pink",
                     font="Helvetica 10 bold", padx=8, pady=2,
                     command=lambda: download_video(entry.get(), 'high'))
button1.pack(pady=10)

button2 = tk.Button(root, text="Download in Low Quality", fg="black", bg="pink",
                     font="Helvetica 10 bold", padx=7, pady=2,
                     command=lambda: download_video(entry.get(), 'low'))
button2.pack(pady=10)

button3 = tk.Button(root, text="Download Audio Only", fg="black", bg="pink",
                     font="Helvetica 10 bold", padx=19, pady=1,
                     command=lambda: download_video(entry.get(), 'audio'))
button3.pack(pady=10)

button4 = tk.Button(root, text="Exit", fg="black", bg="pink", font="Helvetica 10 bold",
                     command=root.destroy, activeforeground="red")
button4.pack(side=tk.BOTTOM, pady=20)

root.mainloop()