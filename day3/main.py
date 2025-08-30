import tkinter as tk
from tkinter import messagebox

def show_info_window(name, email):
    info_win = tk.Toplevel(root)
    info_win.title("Info Submitted")
    info_win.geometry("300x300")
    tk.Label(info_win, text=f"Name: {name}").pack(pady=5)
    tk.Label(info_win, text=f"Email: {email}").pack(pady=5)
    tk.Button(info_win, text="Close", command=info_win.destroy).pack(pady=10)


def submit():
    name=entry_name.get()
    email=email_entry.get()
    confirmation = messagebox.askyesno("confirm",f"Is this Info correct?\n\n Name: {name} \n Email : {email}")
    if confirmation:
        with open("info.txt","a") as file:
            file.write(f"{name}, {email}\n")
        show_info_window(name=name,email=email)
    else:
        messagebox.showinfo("Cancelled","Submission cancelled.")


root=tk.Tk()
root.title('Day3')
root.geometry("300x500+550+20")
root.attributes("-alpha",0.95)



tk.Label(root,text="Enter your name:").pack(pady=10)
entry_name=tk.Entry(root,width=30)
entry_name.pack()

tk.Label(root,text="Enter Your Email").pack(pady=10)
email_entry=tk.Entry(root,width=30)
email_entry.pack()

tk.Button(root,text="Submit",command=submit).pack(pady=10)




root.mainloop()