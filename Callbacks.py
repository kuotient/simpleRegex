import tkinter as tk
from tkinter import messagebox as msg
from tkinter import filedialog as fd


class Callbacks():
    def __init__(self, simpleRegex):
        self.srx = simpleRegex

    def defaultFileEntries(self):
        self.srx.loadBrowseEntry.delete(0, tk.END)
        self.srx.loadBrowseEntry.insert(0, self.srx.fDir)
        if len(self.srx.fDir) > 36:
            #             self.fileEntry.config(width=len(fDir) + 3)
            self.srx.loadBrowseEntry.config(width=35)  # limit width to adjust GUI
            self.srx.loadBrowseEntry.config(state='readonly')

        self.srx.saveBrowseEntry.delete(0, tk.END)
        self.srx.saveBrowseEntry.insert(0, self.srx.saveDir)
        if len(self.srx.saveDir) > 36:
            #             self.netwEntry.config(width=len(netDir) + 3)
            self.srx.saveBrowseEntry.config(width=35)  # limit width to adjust GUI

    # Display a Exit Box
    def _msgBoxExit(self):
        answer = msg.askyesnocancel(self.srx.i18n.exit, self.srx.i18n.exitDescription)
        if answer is True:
            self.srx.main.quit()
            self.srx.main.destroy()
            exit()

    # Display an 'About' message Box
    def _msgBoxAbout(self):
        global VERSION
        msg.showinfo(self.srx.i18n.about, self.srx.i18n.aboutTitle + self.srx.VERSION + self.srx.i18n.aboutDescription)

    def _run(self):
        txt2 = self.srx.scrlInputText.get("1.0", tk.END)
        print(txt2)
        self.srx.scrlOutputText.insert(tk.INSERT, txt2 + '\n')

    def _runProgressBar(self):
        self.srx.progressBar['maximum'] = 100
        from time import sleep
        for i in range(101):
            sleep(0.05)
            self.srx.progressBar['value'] = i
            self.srx.progressBar.update()
        self.srx.progressBar['value'] = 0


    def _getFileName(self):
        fName = fd.askopenfilename(parent=self.srx.main, initialdir=self.srx.fDir, filetypes=self.srx.ftypes)
        self.srx.loadBrowseEntry.config(state='enabled')
        self.srx.loadBrowseEntry.delete(0, tk.END)
        self.srx.loadBrowseEntry.insert(0, fName)

        if len(fName) > 36:
            self.srx.loadBrowseEntry.config(width=35)

    def _saveFile(self):
        print('HELLO')
