import tkinter as tk
from tkinter import filedialog

#Create the main window


root = tk.Tk()
root.title("fileOrganizerGui")
root.geometry("600x250")  # Set the window sizeFunction to be called when the button is clicked

label = tk.Label(root, text="Enter The URL of the file to download:")
label.pack(pady=10)  # Add padding around the labelEntry (input block) where user can type text

#creating an entry widget
URLaddress = tk.Entry(root, width=30)
URLaddress.pack(pady=5)

#creating a label widget
FileName = tk.Label(root, text = "Enetr the name of the file to save: ")
FileName.pack(pady = 10)

def buttonfn():
    url = URLaddress.get()
    filename = FileName.get()
    dwld(url,filename)


button = tk.Button(root, text="DOWNLOAD",command=buttonfn)
button.pack(pady=10)#Start the GUI event loop


root.mainloop()