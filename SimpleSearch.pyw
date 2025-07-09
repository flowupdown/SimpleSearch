""" 
SimpleSearch.py just simple search
"""

Version = 1.0
import sys, os
from tkinter import *
from PP4E.Gui.ShellGui.formrows import makeFormRow

class SimpleSearch(Frame):
    def __init__(self, parent=None, startdir='', filename=''):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.parent = parent
        self.startdir = startdir
        self.filename = filename
        self.text = ''
        parent.title('SimpleSearch %s' % Version)
        self.makeSearchWidget()
        self.makeOutputWidget()
        
    def makeSearchWidget(self):
        searchbar = Frame(self)
        searchbar.pack(side=TOP, fill=BOTH) 
        var1 = makeFormRow(searchbar, label='Directory root', width=20, browse=False)
        var2 = makeFormRow(searchbar, label='File to Find', width=20, browse=False)
        var1.set(self.startdir)
        var2.set(self.filename)
        #self.parent.bind('<Key-Return>', lambda event: self.onSearch(var1.get(), var2.get()))
        cb = lambda: self.onSearch(var1.get(), var2.get())
        Button(searchbar, text='Search', command=cb).pack(side=BOTTOM, fill=X)
        
    def onSearch(self, directory, file):
        self.text = self.Search(directory, file)
        self.onRefresh()
        
    def Search(self, directory, file):
        self.startdir = directory
        self.filename = file
        file_list = []
        for (dir, folds, names) in os.walk(directory):
            for name in names:
                if name == file or file in name.split('.'):
                    f_name = os.path.join(dir, name)
                    f_name = os.path.normpath(f_name)
                    file_list.append(f_name)
        return file_list
    
    def makeOutputWidget(self):
        text_frame = Frame(self)
        text_frame.pack(side=TOP, expand=YES, fill=BOTH)
        text = Text(text_frame)
        text.pack(side=TOP, expand=YES, fill=BOTH)
        self.text_widget = text
        
    def onRefresh(self):
        import subprocess
        browser = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        if self.text == []:
            self.text_widget.insert('end', 'there is no %s in %s'
                                   % (self.filename, self.startdir) + '\n')
            self.text_widget.see(END)
            self.text_widget.update()
        else:
            for p in self.text:
                string = str(p)
                link = string.replace("\\", '')
                self.text_widget.tag_bind(link, '<Double-1>',
                                lambda event, string=string: subprocess.run([browser, string]))
                self.text_widget.insert('end', string + '\n', link)
                self.text_widget.update()
                self.text_widget.see(END)
        self.text = ''

    
if __name__ == '__main__':
    parent = Tk()
    SimpleSearch(parent, startdir='d:\\programming\\python')
    mainloop()
