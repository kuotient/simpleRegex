#----------------------------
# imports
#----------------------------
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext, Menu
from tkinter import filedialog as fd
from LanguageResources import I18N
from Callbacks import Callbacks

from os import path, makedirs

from time import sleep



#globals
VERSION = '0.0.1'
fDir = path.dirname(__file__)
saveDir = fDir + 'saved'
if not path.exists(saveDir):
    makedirs(saveDir, exist_ok=True)
ftypes = [
    ('Text files', '*.txt'),
    ('csv,tsv files', '*.csv;*.tsv'),
    ('HTML files', '*.html'),
    ('All files', '*')
]

# class ButtonFactory():
#     def createButton(self, type_):
#         return buttonTypes[type_]()
#
# class ButtonBase():

class ScrollFactory():
    def createScroll(self, type_):
        return scrollTypes[type_]()

class ScrollBase():
    def __init__(self):
        self.width = 30
        self.height = 3
        self.padWidth = 8
        self.padHeight = 2
    def getScrollConfig(self):
        return self.width, self.height, self.padWidth, self.padHeight

class ScrollInput(ScrollBase):
    def __init__(self):
        super().__init__()
        self.width = 40
        self.height = 10

class ScrollOutput(ScrollBase):
    def __init__(self):


        super().__init__()
        self.width = 80
        self.height = 20

scrollTypes = [ScrollInput, ScrollOutput]


#############################################################################
#############################################################################
class SimpleRegex():
    def __init__(self):
        self.main = tk.Tk()
        self.i18n = I18N('kr')
        self.callBacks = Callbacks(self)
        self.main.title(self.i18n.title)

        self.fDir = fDir
        self.saveDir = saveDir
        self.VERSION = VERSION
        self.ftypes = ftypes

        self.createWidgets()
        self.callBacks.defaultFileEntries()

        # self.main.protocol("WM_DELETE_WINDOW", self.callBacks._msgBoxExit)

    # ---------------------
    # widget Control
    # ---------------------
    def createWidgets(self):
        #==============
        # Tabs
        #==============
        # Create a Tab Bar
        tabControl = ttk.Notebook(self.main)

        # Add Tab items
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text=self.i18n.textEdit)
        tab3 = ttk.Frame(tabControl)
        tabControl.add(tab3, text=self.i18n.fileEdit)
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text=self.i18n.settings)

        # Locate Tabs
        tabControl.pack(expand=1, fill='both')
        # tabControl.pack()

        # Create Global buttons
        self.runB = ttk.Button(self.main, text="RUN", command=self.callBacks._preprocess_files)
        self.runB.pack(side='right')

        # Create status label
        self.status = 'Idle'
        self.statusLabel = ttk.Label(self.main, text= 'Current status: ' + self.status)
        self.statusLabel.pack(side='bottom', anchor='w', padx=1)

        # TAB1
        #==============
        # Labels
        #==============
        # Add LabelFrame items
        self.frame = ttk.LabelFrame(tab1, text=' 문장 변환 ')
        self.frame.grid(column=0, row=0, padx=8, pady=4, sticky='W')

        self.optionsFrame = ttk.LabelFrame(self.frame, text='')
        self.optionsFrame.grid(column=1, row=0, padx=8, pady=1, sticky='E', rowspan=2)

        #Add Label items
        self.inputLabel = ttk.Label(self.frame, text='Input')
        self.inputLabel.grid(column=0, row=0, padx=8, sticky='W')

        self.outputLabel = ttk.Label(self.frame, text='Result')
        self.outputLabel.grid(column=0, row=2, padx=8, sticky='W', columnspan=2)

        # self.optionTest = ttk.Label(self.optionsFrame, text='Test')
        # self.optionTest.grid(column=0,height=10,

        #==============
        # Buttons
        #==============
        # There's an error that can't use height parameter in Button command.
        self.runButton = ttk.Button(self.optionsFrame, text="RUN", command=self.callBacks._run)
        # Use grid's 'ipady' parameter instead.
        self.runButton.grid(column=0, row=0, sticky='E', ipadx=18, ipady=10)
        # self.runButton.configure(state='disabled')

        self.stopButton = ttk.Button(self.optionsFrame, text='STOP', command=self.callBacks._run)
        self.stopButton.grid(column=0, row=1, sticky='E',ipadx=18, ipady=10)

        self.resetButton = ttk.Button(self.optionsFrame, text='RESET', command=self.callBacks._run)
        self.resetButton.grid(column=0, row=2, sticky='E', ipadx=18, ipady=10)

        # self.reset


        #==============
        # CheckButtons
        #==============
        # self.caseChVar = tk.IntVar()
        # self.caseCheck = tk.Checkbutton(self.optionsFrame,
        #                                 text='Case Convertor',
        #                                 variable=self.caseChVar,
        #                                 state='normal')
        # self.caseCheck.grid(column=0, row=1, sticky=tk.W)

        #===============
        # Radio Buttons
        #===============

        #===============
        # ScrollText
        #===============
        self.createScrolls()


        # TAB2
        #==============
        # Labels
        #==============
        # Add LabelFrame items
        self.mngFilesFrame = ttk.LabelFrame(tab2, text= self.i18n.mngFile)
        self.mngFilesFrame.grid(column=0, row=0, padx=8, pady=4, sticky='W')

        self.settingsFrame = ttk.LabelFrame(tab2, text=self.i18n.settings)
        self.settingsFrame.grid(column=0, row=1, padx=8, pady=4, sticky='W')

        self.eliFrame = ttk.LabelFrame(self.settingsFrame, text=self.i18n.eliminate)
        self.eliFrame.grid(column=0, row=0, padx=8, pady=4, sticky='W')

        self.changeFrame = ttk.LabelFrame(self.settingsFrame, text=self.i18n.changeable)
        self.changeFrame.grid(column=1, row=0, padx=8, pady=4, sticky='W')

        # Add Label items
        self.seporatorLabel = ttk.Label(self.changeFrame, text='##########')
        self.seporatorLabel.grid(column=0, row=0, padx=8, sticky='W')

        self.explainLabel = ttk.Label(self.settingsFrame, text=self.i18n.explain)
        self.explainLabel.grid(column=0, row=1, padx=8, pady=4, columnspan=2, sticky='W')

        # ==============
        # Buttons
        # ==============
        #Create button
        self.loadButton = ttk.Button(self.mngFilesFrame, text=self.i18n.browse, width=12, command=self.callBacks._get_file_name)
        self.loadButton.grid(column=0, row=0, sticky=tk.W)

        self.saveButton = ttk.Button(self.mngFilesFrame, text=self.i18n.save, width=12, command=self.callBacks._save_file)
        self.saveButton.grid(column=0, row=1, sticky=tk.E)


        # ==============
        # Entries
        # ==============
        #Create Entry
        self.loadFileDir = tk.StringVar()
        self.loadBrowseEntry = ttk.Entry(self.mngFilesFrame, width=40, textvariable=self.loadFileDir)
        self.loadBrowseEntry.grid(column=1, row=0, sticky=tk.W)

        self.saveFileDir = tk.StringVar()
        self.saveBrowseEntry = ttk.Entry(self.mngFilesFrame, width=40, textvariable=self.saveFileDir)
        self.saveBrowseEntry.grid(column=1, row=1, sticky=tk.W)


        for child in self.mngFilesFrame.winfo_children():
            child.grid_configure(padx=6, pady=4)

        # ==============
        # CheckButtons
        # ==============
        #Create check button
        #빈줄 제거
        self.whiteSpaceChVar = tk.IntVar()
        self.whiteSpaceCheck = tk.Checkbutton(self.eliFrame,
                                              text=self.i18n.blank,
                                              variable=self.whiteSpaceChVar,
                                              state='normal')
        self.whiteSpaceCheck.grid(column=0, row=0, sticky=tk.W)

        #특수 문자 제거
        self.specialChVar = tk.IntVar()
        self.specialCharCheck =  tk.Checkbutton(self.eliFrame,
                                                text=self.i18n.spChar,
                                                variable=self.specialChVar,
                                                state='normal')
        self.specialCharCheck.grid(column=1, row=0, sticky=tk.W)

        #모음 제거
        self.consonantsChVar = tk.IntVar()
        self.consonantsCheck = tk.Checkbutton(self.eliFrame,
                                              text=self.i18n.consonants,
                                              variable=self.consonantsChVar,
                                              state='normal')
        self.consonantsCheck.grid(column=0, row=1, sticky=tk.W)

        #자음 제거
        self.vowelsChVar = tk.IntVar()
        self.vowelsCheck = tk.Checkbutton(self.eliFrame,
                                               text=self.i18n.vowels,
                                               variable=self.vowelsChVar,
                                               state='normal')
        self.vowelsCheck.grid(column=1, row=1, sticky=tk.W)

        # 연속공백 제거
        self.contSpaceChVar = tk.IntVar()
        self.contSpaceCheck = tk.Checkbutton(self.eliFrame,
                                             text= self.i18n.contSpace,
                                             variable=self.contSpaceChVar,
                                             state='normal')
        self.contSpaceCheck.grid(column=0, row=2, sticky=tk.W)

        #한자 제거
        self.chineseChVar = tk.IntVar()
        self.chineseCheck = tk.Checkbutton(self.eliFrame,
                                           text=self.i18n.chinese,
                                           variable=self.chineseChVar,
                                           state='normal')
        self.chineseCheck.grid(column=1, row=2, sticky=tk.W)


        # 특수 숫자 변환
        self.sNumChVar = tk.IntVar()
        self.sNumCheck = tk.Checkbutton(self.changeFrame,
                                        text= '① ➀ ❶ ➊ ⓵ ⒈ ⑴  →  1.',
                                        variable=self.sNumChVar,
                                        state='normal')
        self.sNumCheck.grid(column=0, row=0, sticky=tk.W)

        #낫표, 화살괄호 변환
        self.quoteChVar = tk.IntVar()
        self.quoteCheck = tk.Checkbutton(self.changeFrame,
                                          text="「  」 〈  〉 ′               →  '",
                                          variable=self.quoteChVar,
                                          state='normal')
        self.quoteCheck.grid(column=0, row=1, sticky=tk.W)

        #겹낫표, 겹화살괄호 변환
        self.dQuoteChVar = tk.IntVar()
        self.dQuoteCheck = tk.Checkbutton(self.changeFrame,
                                          text='『  』  《  》  ″             →  "',
                                          variable=self.dQuoteChVar,
                                          state='normal')
        self.dQuoteCheck.grid(column=0, row=2, sticky=tk.W)


        #===============
        # ProgressBar
        #===============

        self.progressBar = ttk.Progressbar(tab2, orient='horizontal', length=370, mode='determinate')
        self.progressBar.grid(column=0,row=2, columnspan=2, padx=8, pady=4, sticky=tk.W)

        ttk.Button(tab2, text='Run ProgressBar', command=self.callBacks._run_progressbar).grid(column=0, row=3,padx=8,pady=4)

        # Tab3
        #===============
        # Labels
        #===============

        # Create LabelFrames
        self.filesFrame = ttk.LabelFrame(tab3, text= self.i18n.mngFile)
        self.filesFrame.grid(column=0, row=0, padx=8, pady=4, ipadx=8, ipady=4, sticky='W')
        # self.scrollFrame = ttk.LabelFrame(self.filesFrame, text='')
        # self.scrollFrame.grid(column=0, row=0, sticky='nsew', columnspan=2)

        #===============
        # Treeviews
        #===============

        # Create Treeview with scrollbar
        self.fileTree = ttk.Treeview(self.filesFrame, columns=['name', 'format', 'path'], show='headings')
        vsb = ttk.Scrollbar(self.filesFrame, orient="vertical", command=self.fileTree.yview)
        hsb = ttk.Scrollbar(self.filesFrame, orient="horizontal", command=self.fileTree.xview)
        self.fileTree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.fileTree.grid(column=0, row=0, sticky='nsew')
        vsb.grid(column=1, row=0, sticky='ns')
        hsb.grid(column=0, row=1, sticky='ew')

        # Create heading of Treeview
        self.fileTree.heading('name', text='Name', anchor=tk.W)
        self.fileTree.heading('format', text='Format', anchor=tk.W)
        self.fileTree.heading('path', text='File path', anchor=tk.W)

        self.scrollFileDir = tk.StringVar()

        #===============
        # Buttons
        #===============
        self.addNewFileButton = ttk.Button(tab3, text=self.i18n.addNewFile, command=self.callBacks._get_file_name)
        self.addNewFileButton.grid(column =0, row=1, pady=6, ipadx=20, ipady=4, sticky='e')

        self.deleteFileButton = ttk.Button(tab3, text=self.i18n.delete, command=self.callBacks._remove_file)
        self.deleteFileButton.grid(column=1, row=1, pady=6, padx=10, ipadx=8, ipady=4, sticky=tk.E)


        #===============
        # Menus
        #===============

        # Creating a Menu Bar
        menuBar = Menu(self.main)
        self.main.config(menu=menuBar)

        # Add menu items
        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu.add_command(label=self.i18n.new)
        fileMenu.add_command(label=self.i18n.settingsMenu)
        fileMenu.add_separator()
        fileMenu.add_command(label=self.i18n.exit, command= self.callBacks._display_msg_exit)
        menuBar.add_cascade(label=self.i18n.file, menu=fileMenu)

        helpMenu = Menu(menuBar, tearoff=0)
        helpMenu.add_command(label=self.i18n.about, command = self.callBacks._display_msg_about)
        menuBar.add_cascade(label=self.i18n.help, menu=helpMenu)


    # def createMenu(self):
    #
    #     factory = MenuFactory()
    #
    #     l = factory.createMenu

    def createScrolls(self):

        factory = ScrollFactory()
        # Create an Input ScrollText item
        w = factory.createScroll(0).getScrollConfig()[0]
        h = factory.createScroll(0).getScrollConfig()[1]
        pW = factory.createScroll(0).getScrollConfig()[2]
        pH = factory.createScroll(0).getScrollConfig()[3]
        self.scrlInputText = scrolledtext.ScrolledText(self.frame,
                                                       width=w,
                                                       height=h,
                                                       wrap=tk.WORD)
        self.scrlInputText.grid(column=0, row=1, padx= pW, pady= pH, sticky='w')


        # Create an Output ScrollText item
        w = factory.createScroll(1).getScrollConfig()[0]
        h = factory.createScroll(1).getScrollConfig()[1]
        pW = factory.createScroll(1).getScrollConfig()[2]
        pH = factory.createScroll(1).getScrollConfig()[3]
        self.scrlOutputText = scrolledtext.ScrolledText(self.frame,
                                                        width=w,
                                                        height=h,
                                                        wrap=tk.WORD)
        self.scrlOutputText.grid(column=0, row=3, padx= pW, pady= pH, sticky='w', columnspan=2)

        self.scrlInputText.focus() # Place cursor into Input text


#---------
# start GUI
#---------
if __name__ == '__main__':
    sRx = SimpleRegex()
    sRx.main.mainloop()


