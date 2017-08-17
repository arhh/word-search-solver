from tkinter import *
from word_search_controller import Logic

class LetterField(object):
    """Class for representing a single cell in word search grid.

       Class for representing a single cell in word search grid allowing for
       a single character to be entered.

       Attributes:
           entry: An entry object with a width of 1 which in where a character
               is typed.
    """

    def __init__(self, frame):
        """Constructor for LetterField object.

           Args:
               frame: tkinter Frame object representing the frame to place the
                   LetterField object.
        """
        self.entry = Entry(frame, width = 1)

    def __str__(self):
        return "Box has value: %s" % (self.entry.get())

class WordSearchGUI(object):
    """Class for representing the word search solver graphical user interface."""
    
    def open_editor(self):
        """Open word search configuration window.
        
           Open word search configuration window which allows a client to
           specify the number of rows and columns in the word search and the
           words to find in the word search.
        """
        #Create dialogue box to configure empty words earch:
        self.customiser = Toplevel(self.root)
        self.customiser.title("Word Search Configuration")
        
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
        self.submit_specs = Button(self.customiser, text = "Generate Grid", command = (lambda: self.set_grid(int(self.row_entry.get()), int(self.column_entry.get()))))
        self.submit_specs.pack()
        self.instructions = Message(self.message, text = "Use the sliders above to define the number of rows and columns for the empty word search. Enter the words to look for below.", width = 350)
        self.instructions.pack()
        self.words_label = Label(self.words_frame, text = "Words to find (separate with a space):")
        self.words_label.grid(row = 1, column = 1)
        self.words_box = Entry(self.words_frame, width = 40)
        self.words_box.grid(row = 1, column = 2)
        
        #Disable action button to prevent multiple configuration windows:
        self.action_button.config(state = DISABLED)
        

    def set_grid(self, rows, columns):
        """Generate empty rows and columns of word search grid.
        
           Generate empty rows and columns of word search grid and re-purpose
           action button on root window into "solve" button.

           Args:
               rows: Integer representing the number of rows in the generated
                   grid.
               columns: Integer representing the number of columns in the generated
                   grid.
        """
        self.get_words()
        self.word_search_grid = []
        for r in range(rows):
            rlist = []
            for c in range(columns):
                rlist += [LetterField(self.centrepiece)]
                rlist[-1].entry.grid(row = r, column = c)
            self.word_search_grid += [rlist]
        self.customiser.destroy()
        
        self.action_button.config(text = "Solve Word Search", command = self.solve, state = NORMAL)

    def get_grid(self):
        """Get all the characters typed into word search grid.

           Get all the characters typed into word search grid and send to word
           search logic.
        """
        self.fullws = []
        for row in self.word_search_grid:
            rowdata = []
            for column in row:
                rowdata += [column.entry.get()]
            self.fullws += [rowdata]
        self.logic.set_grid(self.fullws)

    def get_words(self):
        """Get the words to be found in word search grid."""
        wordlist = self.words_box.get().split()
        for word in wordlist:
            self.words[word] = False
        self.logic.set_words_to_find(self.words)

    def solve(self):
        """Solve the word search.

           Solve the word search and highlight the graphical grid to indicate the
           location of the first letter of each word to find.

        """
        
        self.action_button.config(state = DISABLED)
        
        self.get_grid()
        resultdict = self.logic.solve()
        for word in resultdict:
            if resultdict[word]:
                self.word_search_grid[resultdict[word][0]][resultdict[word][1]].entry["fg"] = "red"

    def __init__(self):
        """Constructor for word search GUI."""
        self.logic = Logic()
        self.fullws = []
        self.word_search_grid = []
        self.words = {}
        #Create the root window:
        self.root = Tk()
        self.root.minsize(width = 400, height = 300)
        self.root.title("Word search Editor")

        #Divide the root window for action button and word search:
        self.centrepiece = Frame(self.root)
        self.centrepiece.pack()
        self.bottompiece = Frame(self.root)
        self.bottompiece.pack()
        
        #Create multi-function action button on root window:
        self.action_button = Button(self.bottompiece, text = "Set up Word Search", command = self.open_editor)
        self.action_button.pack()

        self.root.mainloop()

if __name__ == "__main__":
    the_gui = WordSearchGUI()
