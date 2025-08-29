from tkinter import *

root=Tk()
root.title("Day-2")
root.geometry("400x300+500+200")
root.resizable(False,False)
root.config(bg="#426")

is_fullscreen=False
def toggle_fullscreen():
    global is_fullscreen 

    if is_fullscreen:
        is_fullscreen = False
        fullscreen_btn.config(text="Fullscreen") 
    else:
        is_fullscreen = True
        fullscreen_btn.config(text="Exit") 
    root.attributes("-fullscreen",is_fullscreen)
    print(is_fullscreen)



win_alpha=1.0
def update_win_alpha(ope):
    global win_alpha
    if ope=='+' and win_alpha<1:
        win_alpha+=0.05
    elif ope=='-' and win_alpha>0.35:
        win_alpha-=0.05
    win_alpha=max(0.1,min(1.0,win_alpha))
    transperency_text.config(textvariable=StringVar(value=f"Window Transparency : {win_alpha:.2f}"))
    root.attributes("-alpha",win_alpha)

fullscreen_btn=Button(root,bg="white",fg="#426",text="Fullscreen",command=toggle_fullscreen,font=("Arial",16),cursor="hand2")
fullscreen_btn.grid(row=0,column=0,pady=10)
frame1 = Frame(root).grid(row=2,column=0)
transperency_text = Label(frame1,bg="#426",text="Window Transparency : 1.00",fg="white",font=(14))
transperency_text.grid(row=1,column=0)
Button(frame1,text="Transparency ++",command=lambda:update_win_alpha("+")).grid(row=2,column=0)
Button(frame1,text="Transparency --",command=lambda:update_win_alpha("-")).grid(row=2,column=1)


root.mainloop()