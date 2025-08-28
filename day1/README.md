# 🐍 Day 1: Hello Tkinter – My First GUI Window

Welcome to Day 1 of my Tkinter learning journey! This project marks the beginning of building desktop GUI apps using Python’s built-in Tkinter library.

## 📌 What I Learned

- How to create a root window using `tk.Tk()`
- Setting window title, size, and position with `.title()` and `.geometry()`
- Making the window resizable or fixed with `.resizable()`
- Customizing background color using `.configure(bg=...)`
- Adding a simple `Label` widget and placing it with `.pack()`
- Running the GUI loop with `.mainloop()`

## 🧪 Features Demonstrated

| Feature         | Method Used              | Description                                  |
|----------------|--------------------------|----------------------------------------------|
| Title          | `root.title("...")`      | Sets the window title                        |
| Size & Position| `root.geometry("WxH+X+Y")`| Defines window dimensions and screen position|
| Resizability   | `root.resizable(w, h)`   | Enables/disables resizing                    |
| Background     | `root.configure(bg="...")`| Sets background color                        |
| Label Widget   | `tk.Label()`             | Displays static text                         |
| Layout Manager | `.pack()`                | Places widget in the window                  |
| Main Loop      | `root.mainloop()`        | Keeps the window running                     |

# 🧱 Window Attributes – Customizing Behavior

Let's explore `root.attributes()` to control how the window behaves at the OS level. These tweaks are especially useful for creating splash screens, tool windows, or immersive fullscreen apps.

## 🔧 Attributes Used

| Attribute         | Purpose                                | Value Example     |
|------------------|----------------------------------------|-------------------|
| `-alpha`         | Sets transparency                      | `0.9`             |
| `-topmost`       | Keeps window above others              | `True`            |
| `-fullscreen`    | Enables fullscreen mode                | `True`            |
| `-transparentcolor` | Makes a color invisible (Windows)   | `"white"`         |
| `-toolwindow`    | Removes minimize/maximize buttons      | `True`            |
| `-disabled`      | Disables interaction (Windows)         | `True`            |
