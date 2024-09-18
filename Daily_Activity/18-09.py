import tkinter as tk  # GUI

root = tk.Tk()

root.title("Anonymous")
root.geometry("400x300")

def show_input():
    user_input = entry.get()
    print("User Input:",user_input)

label = tk.Label(root, text="Enter Address")
label.pack(pady=20)

entry = tk.Entry(root, width=100)
entry.pack(pady=10)

button = tk.Button(root, text="Details")
button.pack(pady=10)

root.mainloop()