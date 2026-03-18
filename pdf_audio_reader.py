# Import GUI components from tkinter
from tkinter import *
from tkinter import filedialog
import threading

# Updated import (PdfFileReader is deprecated)
from PyPDF2 import PdfReader

# Text-to-speech engine
import pyttsx3


# -----------------------------
# FUNCTION: Extract text from PDF
# -----------------------------
def extract_text():
    """
    Opens a file dialog to select a PDF file,
    reads all pages, and stores the extracted text globally.
    """

    # Ask user to select a PDF file
    file_path = filedialog.askopenfilename(
        parent=root,
        filetypes=[('PDF file', '*.pdf')],
        title='Select PDF file'
    )

    # If user selects a file
    if file_path:
        global text_extracted
        text_extracted = ""

        # Open file in binary mode
        with open(file_path, "rb") as file:
            reader = PdfReader(file)

            # Loop through all pages
            for page in reader.pages:
                # Extract text from each page
                text_extracted += page.extract_text() or ""


# -----------------------------
# FUNCTION: Convert text to speech
# -----------------------------
def speak_text():
    """
    Runs text-to-speech in a separate thread
    so GUI stays responsive.
    """

    def run_speech():
        try:
            rate_value = int(rate_entry.get())
        except:
            rate_value = 150

        engine.setProperty('rate', rate_value)

        voices = engine.getProperty('voices')
        selected_voice = voices[0].id

        if female_var.get() == 1 and len(voices) > 1:
            selected_voice = voices[1].id

        engine.setProperty('voice', selected_voice)

        if text_extracted:
            engine.say(text_extracted)
            engine.runAndWait()

    # Run speech in a new thread
    threading.Thread(target=run_speech).start()


# -----------------------------
# FUNCTION: Stop speech
# -----------------------------
def stop_speaking():
    """Stops the speech immediately"""
    engine.stop()


# -----------------------------
# GUI APPLICATION
# -----------------------------
def Application(root):
    """
    Builds the GUI layout (frames, buttons, inputs)
    """

    root.geometry('700x600')  # Set window size
    root.resizable(False, False)  # Disable resizing
    root.title('PDF to Audio')
    root.configure(background='light blue')

    global rate_entry, male_var, female_var

    # -----------------------------
    # FRAMES
    # -----------------------------
    frame1 = Frame(root, width=500, height=200, bg='indigo')
    frame2 = Frame(root, width=500, height=450, bg='light blue')

    frame1.pack(side='top', fill='both')
    frame2.pack(side='top', fill='y')

    # -----------------------------
    # HEADER LABELS
    # -----------------------------
    Label(frame1, text='PDF to Audio', fg='black', bg='blue',
          font=('Arial', 25, 'bold')).pack()

    Label(frame1, text='Hear your PDF file', fg='indigo', bg='green',
          font=('Calibre', 25, 'bold')).pack()

    # -----------------------------
    # BUTTON: Select PDF
    # -----------------------------
    btn = Button(
        frame2,
        text='Select PDF File',
        activebackground='red',
        command=extract_text,   # ✅ FIXED (no brackets)
        padx=70,
        pady=10,
        fg='black',
        bg='green',
        font=('Calibre', 20, 'bold')
    )
    btn.grid(row=0, columnspan=2, pady=20)

    # -----------------------------
    # SPEECH RATE INPUT
    # -----------------------------
    Label(frame2, text='Enter rate of Speech',
          fg='black', bg='green',
          font=('Calibre', 18, 'bold')).grid(row=1, column=0, pady=15)

    rate_entry = Entry(frame2, bd=5, fg='black', bg='white',
                       font=('Calibre', 18))
    rate_entry.grid(row=1, column=1, pady=15)

    # -----------------------------
    # VOICE SELECTION
    # -----------------------------
    Label(frame2, text='Select Voice',
          fg='black', bg='green',
          font=('Calibre', 18, 'bold')).grid(row=2, column=0, pady=15)

    male_var = IntVar()
    Checkbutton(frame2, text='Male', variable=male_var,
                bg='green').grid(row=2, column=1, sticky=W)

    female_var = IntVar()
    Checkbutton(frame2, text='Female', variable=female_var,
                bg='pink').grid(row=3, column=1, sticky=W)

    # -----------------------------
    # PLAY BUTTON
    # -----------------------------
    Button(
        frame2,
        text='Play PDF File',
        command=speak_text,
        padx=50,
        pady=10,
        bg='green',
        font=('Calibre', 18, 'bold')
    ).grid(row=4, column=0, pady=40)

    # -----------------------------
    # STOP BUTTON
    # -----------------------------
    Button(
        frame2,
        text='Stop Speaking',
        command=stop_speaking,
        padx=50,
        pady=10,
        bg='red',
        font=('Calibre', 18, 'bold')
    ).grid(row=4, column=1, pady=40)


# -----------------------------
# MAIN PROGRAM START
# -----------------------------
if __name__ == '__main__':

    # Initialize text variable
    text_extracted = ""

    # Initialize text-to-speech engine
    engine = pyttsx3.init()

    # Create main window
    root = Tk()

    # Launch application
    Application(root)

    # Start GUI loop
    root.mainloop()