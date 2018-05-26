import tkinter as tk


# Create root window
root = tk.Tk()
root.wm_title('PageRank')

# Create Label for a-value entry
tk.Label(root, text="a value").grid(row=0)

# Create entry for a-value
aEntry = tk.Entry(root)
aEntry.grid(row=0, column=1)
aEntry.insert(10, ".85")

# Create Text box to inform user
editor = tk.Text(root, width=20, height=5)
editor.grid(column=0, row=1, rowspan=2)
editor.config(state=tk.DISABLED)

# Make the window
root.mainloop()