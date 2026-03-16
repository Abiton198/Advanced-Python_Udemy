# Import everything from tkinter
from tkinter import *

# Program starts here
if __name__ == "__main__":

    # Create main window
    root = Tk()

    # Set window title
    root.title("Abiton Notepad")

    # Allow window resizing control
    root.resizable(True, True)

    # Create the main menu bar
    Main_Menu = Menu(root)

    # Attach menu bar to window
    root.config(menu=Main_Menu)

    # -------------------------
    # FUNCTIONS (placeholders)
    # -------------------------

    # File menu functions
    def Save_As():
        pass  # will add file saving later

    def New_File():
        pass  # clear text area later

    def Open_File():
        pass  # open file later

    def Close():
        root.quit()  # close application


    # Edit menu functions
    def Cut():
        pass

    def Copy():
        pass

    def Paste():
        pass

    def Erase():
        pass

    def Clear_Screen():
        text.delete("1.0", END)  # clear text widget


    # Insert menu functions
    def Date():
        pass


    # Format functions
    def No_Format():
        pass

    def Bold():
        pass

    def Underline():
        pass

    def Italic():
        pass


    # Personalize
    def Background():
        pass


    # Help functions
    def Help():
        pass

    def Online_Help():
        pass

    def Font():
        pass

    # -------------------------
    # FILE MENU
    # -------------------------

    File_Menu = Menu(Main_Menu, tearoff=0)

    Main_Menu.add_cascade(label="File", menu=File_Menu)

    File_Menu.add_command(label='New File', command=New_File)
    File_Menu.add_command(label='Open', command=Open_File)
    File_Menu.add_command(label='Save As', command=Save_As)
    File_Menu.add_separator()
    File_Menu.add_command(label='Close', command=Close)


    # -------------------------
    # EDIT MENU
    # -------------------------

    Edit_Menu = Menu(Main_Menu, tearoff=0)

    Main_Menu.add_cascade(label="Edit", menu=Edit_Menu)

    Edit_Menu.add_command(label='Cut', command=Cut)
    Edit_Menu.add_command(label='Copy', command=Copy)
    Edit_Menu.add_command(label='Paste', command=Paste)
    Edit_Menu.add_command(label='Erase', command=Erase)
    Edit_Menu.add_separator()
    Edit_Menu.add_command(label='Clear Screen', command=Clear_Screen)


    # -------------------------
    # INSERT MENU
    # -------------------------

    Insert_Menu = Menu(Main_Menu, tearoff=0)

    Main_Menu.add_cascade(label="Insert", menu=Insert_Menu)

    Insert_Menu.add_command(label='Current Date', command=Date)


    # -------------------------
    # FORMAT MENU
    # -------------------------

    Format_Menu = Menu(Main_Menu, tearoff=0)

    Main_Menu.add_cascade(label="Change Format", menu=Format_Menu)
    Format_Menu.add_command(label='Font', command=Font)
    Format_Menu.add_separator()
    Format_Menu.add_command(label='No Format', command=No_Format)
    Format_Menu.add_command(label='Bold', command=Bold)
    Format_Menu.add_command(label='Underline', command=Underline)
    Format_Menu.add_command(label='Italic', command=Italic)


    # -------------------------
    # PERSONALIZE MENU
    # -------------------------

    Personalize_Menu = Menu(Main_Menu, tearoff=0)

    Main_Menu.add_cascade(label="Personalize", menu=Personalize_Menu)

    Personalize_Menu.add_command(label='Background', command=Background)


    # -------------------------
    # HELP MENU
    # -------------------------

    Help_Menu = Menu(Main_Menu, tearoff=0)

    Main_Menu.add_cascade(label="Help", menu=Help_Menu)

    Help_Menu.add_command(label='Help', command=Help)
    Help_Menu.add_command(label='Online Help', command=Online_Help)


    # -------------------------
    # TEXT EDITOR AREA
    # -------------------------

    # Text widget (main typing area)
    text = Text(root, width=100, height=40, font=('Arial', 10))

    # Scrollbar for the text widget
    scroll = Scrollbar(root)

    # Connect scrollbar to text
    scroll.config(command=text.yview)
    text.config(yscrollcommand=scroll.set)

    # Pack widgets into window
    scroll.pack(side=RIGHT, fill=Y)
    text.pack(side=LEFT, fill=BOTH, expand=True)


    # Start GUI loop
    root.mainloop()