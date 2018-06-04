from tkinter import *
import PageRank
from tkinter import filedialog
import os.path
import webbrowser

# Based on this validation function:
# https://stackoverflow.com/questions/21205924/restricting-the-value-in-tkinter-entry-widget-why-cant-i-delete-the-first-char

currentFile = r'\\southw-sfps-01.business.mpls.k12.mn.us\Students_A-L\tlin2001\Desktop\PageRank_Pages'


def callback(event):
    webbrowser.open_new(r"https://docs.google.com/document/d/1KSQ1krWpffTXGRc_V4IoGV42lhd-KSnc0zrlHUCGrFs/edit")

class window2:
    def __init__(self, master1):
        self.panel2 = Frame(master1)
        self.panel2.grid()
        self.quitButton = Button(self.panel2, text = "Quit", command = self.panel2.quit)
        self.quitButton.grid(column = 0, row = 0, columnspan = 2)
        vcmd = (master1.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.label1 = Label(self.panel2, text="a value entry: enter 0 through 1")
        self.label1.grid(column = 0, row=1, columnspan = 2)
        self.aEntry = Entry(self.panel2)
        self.aEntry.insert(10, "0.85")
        self.aEntry.config(validate = 'key', validatecommand = vcmd)
        self.aEntry.grid(column = 0, row = 2, columnspan = 2)
        self.aEntry.focus()
        self.runButton = Button(self.panel2, text = "Run", command=self.run)
        self.runButton.grid(column = 0, row = 3)
        self.selectButton = Button(self.panel2, text="Select file", command=selectFile)
        self.selectButton.grid(column=1, row=3)
        self.label2 = Label(root, text = "Link to documentation", cursor="hand2", fg="blue")
        self.label2.grid(column = 0, row = 4, columnspan = 4)
        self.label2.bind("<Button-1>", callback)
        self.output = Text(root, width=20, height=6)
        self.output.grid(column = 2, row = 0)
        self.output.insert('1.0', 'Importance of pages:' + '\n')
        self.output.config(state=DISABLED)

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

    def run(self):
        self.output.config(state=NORMAL)
        self.output.delete(1.0, END)
        try:
            result, htmlPageNames = PageRank.PageRank(float(self.aEntry.get()), currentFile)
            for item in reversed(range(len(result))):
                self.output.insert('1.0', htmlPageNames[item] + ': ' + str(round(float(result[item]), 3)) + '\n')
            # self.output.insert('1.0', result)
            self.output.insert('1.0', 'Importance of pages:' + '\n')
        except:
            self.output.insert('1.0', 'Invalid input.')
        self.output.config(state=DISABLED)


root = Tk()

# A lot of help for this function from:
# https://gist.github.com/Yagisanatode/0d1baad4e3a871587ab1#file-tkinter_filedialog-py-L1


def selectFile():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("html files", "*.html"), ("all files", "*.*")))
    path = os.path.dirname(filename)
    global currentFile
    currentFile = path

root.title('PageRank')
window2(root)



root.mainloop()