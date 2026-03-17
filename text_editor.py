# -------------------------------------------------------
# ABITON NOTEPAD
# A simple text editor built with Tkinter
# -------------------------------------------------------

# Import Tkinter GUI components
from tkinter import *

# Dialog boxes and utilities
from tkinter.messagebox import askyesno
from tkinter import filedialog
from tkinter.colorchooser import askcolor

# Other useful modules
import datetime
import webbrowser


# -------------------------------------------------------
# MAIN PROGRAM STARTS HERE
# -------------------------------------------------------
if __name__ == "__main__":

    # Create the main application window
    root = Tk()

    # Set window title
    root.title("Abiton Notepad")

    # Allow resizing of the window
    root.resizable(True, True)

    # Create the main menu bar
    Main_Menu = Menu(root)

    # Attach menu bar to the window
    root.config(menu=Main_Menu)

    # -------------------------------------------------------
    # FILE MENU FUNCTIONS
    # -------------------------------------------------------

    def Save_As():
        """
        Save the current text to a file chosen by the user.
        """
        filename = filedialog.asksaveasfilename(defaultextension=".txt")

        if filename:
            # Get all text from the editor
            all_text = text.get("1.0", END)

            # Write text to the selected file
            with open(filename, "w") as file:
                file.write(all_text)


    def New_File():
        """
        Ask the user to save current work before clearing the editor.
        """
        if askyesno("Abiton Notepad", "Do you want to save this file?"):
            Save_As()

        # Clear the editor
        text.delete("1.0", END)


    def Open_File():
        """
        Open a text file and load its contents into the editor.
        """
        filepath = filedialog.askopenfilename()

        if filepath:
            with open(filepath, "r") as file:
                content = file.read()

            # Clear existing text
            text.delete("1.0", END)

            # Insert file content
            text.insert(INSERT, content)


    def Close():
        """
        Ask to save work before closing the program.
        """
        if askyesno("Abiton Notepad", "Do you want to save this file?"):
            Save_As()

        # Close the application
        root.destroy()


    # -------------------------------------------------------
    # EDIT MENU FUNCTIONS
    # -------------------------------------------------------

    def Cut():
        """Cut selected text to clipboard."""
        text.clipboard_clear()
        text.clipboard_append(text.selection_get())
        text.delete(SEL_FIRST, SEL_LAST)


    def Copy():
        """Copy selected text to clipboard."""
        text.clipboard_clear()
        text.clipboard_append(text.selection_get())


    def Paste():
        """Paste text from clipboard."""
        try:
            clipboard_text = text.selection_get(selection="CLIPBOARD")
            text.insert(INSERT, clipboard_text)
        except:
            pass


    def Erase():
        """Delete selected text."""
        text.delete(SEL_FIRST, SEL_LAST)


    def Clear_Screen():
        """Clear all text from the editor."""
        text.delete("1.0", END)


    # -------------------------------------------------------
    # INSERT MENU FUNCTIONS
    # -------------------------------------------------------

    def Date():
        """Insert today's date at the cursor position."""
        today = datetime.date.today()
        text.insert(INSERT, today)


    # -------------------------------------------------------
    # FORMAT MENU FUNCTIONS
    # -------------------------------------------------------

    def Text_Color():
        """Change the color of the text."""
        (rgb, color) = askcolor()

        if color:
            text.config(foreground=color)


    def No_Format():
        """Reset text formatting."""
        text.config(font=("Arial", 10))


    def Bold():
        """Apply or remove bold formatting."""
        current_tags = text.tag_names("sel.first")

        if "bold" in current_tags:
            text.tag_remove("bold", "sel.first", "sel.last")
        else:
            text.tag_add("bold", "sel.first", "sel.last")
            text.tag_config("bold", font=("Arial", 10, "bold"))


    def Underline():
        """Apply or remove underline formatting."""
        current_tags = text.tag_names("sel.first")

        if "underline" in current_tags:
            text.tag_remove("underline", "sel.first", "sel.last")
        else:
            text.tag_add("underline", "sel.first", "sel.last")
            text.tag_config("underline", font=("Arial", 10, "underline"))


    def Italic():
        """Apply or remove italic formatting."""
        current_tags = text.tag_names("sel.first")

        if "italic" in current_tags:
            text.tag_remove("italic", "sel.first", "sel.last")
        else:
            text.tag_add("italic", "sel.first", "sel.last")
            text.tag_config("italic", font=("Arial", 10, "italic"))


    def Font():
        """Placeholder for font selection feature."""
        pass


    # -------------------------------------------------------
    # PERSONALIZATION FUNCTIONS
    # -------------------------------------------------------

    def Background():
        """Change the background color of the editor."""
        (rgb, color) = askcolor()

        if color:
            text.config(bg=color)


    # -------------------------------------------------------
    # HELP FUNCTIONS
    # -------------------------------------------------------

    def Online_Help():
        """Open help page in the web browser."""
        webbrowser.open("https://google.com")


    # -------------------------------------------------------
    # FILE MENU
    # -------------------------------------------------------

    File_Menu = Menu(Main_Menu, tearoff=0)
    Main_Menu.add_cascade(label="File", menu=File_Menu)

    File_Menu.add_command(label="New File", command=New_File)
    File_Menu.add_command(label="Open", command=Open_File)
    File_Menu.add_command(label="Save As", command=Save_As)
    File_Menu.add_separator()
    File_Menu.add_command(label="Close", command=Close)


    # -------------------------------------------------------
    # EDIT MENU
    # -------------------------------------------------------

    Edit_Menu = Menu(Main_Menu, tearoff=0)
    Main_Menu.add_cascade(label="Edit", menu=Edit_Menu)

    Edit_Menu.add_command(label="Cut", command=Cut)
    Edit_Menu.add_command(label="Copy", command=Copy)
    Edit_Menu.add_command(label="Paste", command=Paste)
    Edit_Menu.add_command(label="Erase", command=Erase)
    Edit_Menu.add_separator()
    Edit_Menu.add_command(label="Clear Screen", command=Clear_Screen)


    # -------------------------------------------------------
    # INSERT MENU
    # -------------------------------------------------------

    Insert_Menu = Menu(Main_Menu, tearoff=0)
    Main_Menu.add_cascade(label="Insert", menu=Insert_Menu)

    Insert_Menu.add_command(label="Current Date", command=Date)


    # -------------------------------------------------------
    # FORMAT MENU
    # -------------------------------------------------------

    Format_Menu = Menu(Main_Menu, tearoff=0)
    Main_Menu.add_cascade(label="Change Format", menu=Format_Menu)

    Format_Menu.add_command(label="Font", command=Font)
    Format_Menu.add_separator()
    Format_Menu.add_command(label="Text Color", command=Text_Color)
    Format_Menu.add_command(label="No Format", command=No_Format)
    Format_Menu.add_command(label="Bold", command=Bold)
    Format_Menu.add_command(label="Underline", command=Underline)
    Format_Menu.add_command(label="Italic", command=Italic)


    # -------------------------------------------------------
    # PERSONALIZE MENU
    # -------------------------------------------------------

    Personalize_Menu = Menu(Main_Menu, tearoff=0)
    Main_Menu.add_cascade(label="Personalize", menu=Personalize_Menu)

    Personalize_Menu.add_command(label="Background", command=Background)


    # -------------------------------------------------------
    # HELP MENU
    # -------------------------------------------------------

    Help_Menu = Menu(Main_Menu, tearoff=0)
    Main_Menu.add_cascade(label="Help", menu=Help_Menu)

    Help_Menu.add_command(label="Online Help", command=Online_Help)


    # -------------------------------------------------------
    # TEXT EDITOR AREA
    # -------------------------------------------------------

    # Main text editing widget
    text = Text(root, width=100, height=40, font=("Arial", 10))

    # Vertical scrollbar
    scroll = Scrollbar(root)

    # Connect scrollbar with text widget
    scroll.config(command=text.yview)
    text.config(yscrollcommand=scroll.set)

    # Layout widgets
    scroll.pack(side=RIGHT, fill=Y)
    text.pack(side=LEFT, fill=BOTH, expand=True)


    # Start the GUI event loop
    root.mainloop()