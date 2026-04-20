import tkinter as tk
from tkinter import filedialog, messagebox

def save_file():
    file = filedialog.asksaveasfile(defaultextension=".txt", 
                                    filetypes=[("Text Documents", "*.txt")])
    if file:
        content = text_area.get(1.0, tk.END)
        file.write(content)
        file.close()
        messagebox.showinfo("Success", "Note saved successfully!")

def open_file():
    file = filedialog.askopenfile(filetypes=[("Text Documents", "*.txt")])
    if file:
        content = file.read()
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, content)
        file.close()

# ആപ്പിന്റെ വിൻഡോ സെറ്റപ്പ്
root = tk.Tk()
root.title("Dhan's Digital Notepad")
root.geometry("400x400")

# ടെക്സ്റ്റ് ഏരിയ
text_area = tk.Text(root, wrap='word')
text_area.pack(expand=True, fill='both')

# മെനു ബാർ
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()