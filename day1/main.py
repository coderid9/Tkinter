import tkinter as tk

# create main window
root = tk.Tk()
root.title("My First Tkinter app.")
root.geometry("400x300+200+100")
root.resizable(True,False)
root.configure(bg="#2a1c81")
root.iconbitmap("icon.ico")

root.attributes("-alpha",0.75)
root.attributes("-topmost",True)
# root.attributes("-fullscreen",True)
# root.attributes("-transparentcolor","white")
# root.attributes("-toolwindow",True)
# root.attributes("-disabled",True)

# Add a label(Heading / text)
label = tk.Label(root,text="Hello Tkinter!",font=("Helvetica",16,"bold"))
label.pack(pady=20)

# Run the app
root.mainloop()
