from tkinter import *
from WordSearchLogic import Logic

#Blueprint for empty wordsearch field object:
class LetterField(object):
    def __init__(self, frame):
        self.entry = Entry(frame, width = 1)
    def __str__(self):
        return "Box has value: %s" % (self.entry.get())

#Class for creating GUI:
class WordSearchGUI(object):
    #Callback function to generate rows and columns of wordsearch:
    def setGrid(self, row, column):
        self.getWords()
        self.ws = []
        for r in range(row):
            rlist = []
            for c in range(column):
                rlist += [LetterField(self.centrepiece)]
                rlist[-1].entry.grid(row = r, column = c)
            self.ws += [rlist]
        self.customiser.destroy()

    #Get all the characters typed into the grid:
    def getGrid(self):
        self.fullws = []
        for row in self.ws:
            rowdata = []
            for column in row:
                rowdata += [column.entry.get()]
            self.fullws += [rowdata]
        self.logic.setWordSearch(self.fullws)

    #Get all the words the user typed in the config dialogue:
    def getWords(self):
        wordlist = self.words_box.get().split()
        for word in wordlist:
            self.words[word] = False
        self.logic.setWords(self.words)
        print(self.words)

    #Run via "Solve" button...:
    def solve(self):
        self.getGrid()
        resultdict = self.logic.solve()
        for word in resultdict:
            if resultdict[word]:
                self.ws[resultdict[word][0]][resultdict[word][1]].entry["fg"] = "green"

    #Create View:
    def __init__(self):
        self.logic = Logic()
        self.fullws = []
        self.ws = []
        self.words = {}
        #Create the root window:
        self.root = Tk()
        self.root.minsize(width = 400, height = 300)
        self.root.title("Wordsearch Editor")

        #Divide the root window for "solve" button and wordsearch:
        self.centrepiece = Frame(self.root)
        self.centrepiece.pack()
        self.bottompiece = Frame(self.root)
        self.bottompiece.pack()

        #"solve" button on root window:
        self.solve_button = Button(self.bottompiece, text = "Solve Wordsearch", command = self.solve)
        self.solve_button.pack()

        #Create dialogue box to configure empty wordsearch:
        self.customiser = Toplevel()
        self.customiser.title("Wordsearch Configuration")

        #Widgets of dialogue box
        self.controls = Frame(self.customiser)
        self.controls.pack()
        self.message = LabelFrame(self.customiser, text = "Instructions:")
        self.message.pack()
        self.words_frame = Frame(self.customiser)
        self.words_frame.pack()
        self.row_entry = Scale(self.controls, from_ = 2, to = 20, orient = HORIZONTAL)
        self.row_entry.grid(row = 1, column = 2)
        self.row_label = Label(self.controls, text = "Rows:", justify = RIGHT)
        self.row_label.grid(row = 1, column = 1)
        self.column_entry = Scale(self.controls, from_ = 2, to = 20, orient = HORIZONTAL)
        self.column_entry.grid(row = 1, column = 4)
        self.column_label = Label(self.controls, text = "Columns:", justify = RIGHT)
        self.column_label.grid(row = 1, column = 3)
        self.submit_specs = Button(self.customiser, text = "Generate Grid", command = (lambda: self.setGrid(int(self.row_entry.get()), int(self.column_entry.get()))))
        self.submit_specs.pack()
        self.instructions = Message(self.message, text = "Use the sliders above to define the number of rows and columns for the empty wordsearch. Enter the words to look for below.", width = 350)
        self.instructions.pack()
        self.words_label = Label(self.words_frame, text = "Words to find (separate with a space):")
        self.words_label.grid(row = 1, column = 1)
        self.words_box = Entry(self.words_frame, width = 40)
        self.words_box.grid(row = 1, column = 2)

        self.root.mainloop()

if __name__ == "__main__":
    the_gui = WordSearchGUI()
