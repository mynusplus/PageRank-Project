import tkinter as tk

# Based on this validation function:
# https://stackoverflow.com/questions/21205924/restricting-the-value-in-tkinter-entry-widget-why-cant-i-delete-the-first-char

class window2:
    def __init__(self, master1):
        self.panel2 = tk.Frame(master1)
        self.panel2.grid()
        self.quitButton = tk.Button(self.panel2, text = "Quit", command = self.panel2.quit)
        self.quitButton.grid()
        vcmd = (master1.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.label1 = tk.Label(self.panel2, text="a value entry: enter 0 through 1").grid(row=1)
        self.aEntry = tk.Entry(self.panel2)
        self.aEntry.insert(10, "0.85")
        self.aEntry.config(validate = 'key', validatecommand = vcmd)
        self.aEntry.grid()
        self.aEntry.focus()
        self.runButton = tk.Button(self.panel2, text = "Run", command = self.panel2.quit)
        self.runButton.grid(column = 0, row = 3)
        self.output = tk.Text(root, width=20, height=5)
        self.output.grid(column=1, row=0, rowspan=2)
        self.output.config(state=tk.DISABLED)

    def validate(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if len(value_if_allowed) == 0:
            return True
        elif text in '0123456789.':
            try:
                float(value_if_allowed)
                if float(0 <= float(value_if_allowed) <= 1):
                    return True
                else:
                    return False
            except ValueError:
                return False
        else:
            return False

root = tk.Tk()
window2(root)



root.mainloop()