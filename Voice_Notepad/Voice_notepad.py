import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
import speech_recognition as sr

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Voice Notes")
root.geometry("700x500")

current_file = None 

# Function to start voice input
def start_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        messagebox.showinfo("Info", "Listening... Please speak now.")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            note_text.insert(ctk.END, text + "\n")
        except sr.UnknownValueError:
            messagebox.showerror("Error", "Could not understand the audio")
        except sr.RequestError:
            messagebox.showerror("Error", "Could not request results; check your network connection")

# Function to create and save a new file
def create_new_file():
    global current_file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        current_file = file_path
        update_current_file_label()
        with open(current_file, 'w') as file:
            file.write(note_text.get("1.0", ctk.END))
        messagebox.showinfo("Info", "File saved successfully")

# Function to select and edit an existing file
def select_file():
    global current_file
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        current_file = file_path
        update_current_file_label()
        with open(current_file, 'r') as file:
            content = file.read()
            note_text.delete("1.0", ctk.END)
            note_text.insert(ctk.END, content)
        save_button.configure(command=save_existing_file)

# Function to save changes to an existing file
def save_existing_file():
    if current_file:
        with open(current_file, 'w') as file:
            file.write(note_text.get("1.0", ctk.END))
        messagebox.showinfo("Info", "File updated successfully")

# Function to update the label with the current file name
def update_current_file_label():
    if current_file:
        current_file_label.configure(text=f"Editing File: {os.path.basename(current_file)}")
    else:
        current_file_label.configure(text="No file selected")

# Function to exit the application
def exit_application():
    root.destroy()

create_button = ctk.CTkButton(root, text="Create New File", command=create_new_file, width=200)
create_button.pack(pady=10)

select_button = ctk.CTkButton(root, text="Select File", command=select_file, width=200)
select_button.pack(pady=10)

voice_button = ctk.CTkButton(root, text="Start Voice Input", command=start_voice_input, width=200)
voice_button.pack(pady=10)

note_text = ctk.CTkTextbox(root, wrap=ctk.WORD, width=400, height=200)
note_text.pack(pady=10)

current_file_label = ctk.CTkLabel(root, text="No file selected", font=("Arial", 12))
current_file_label.pack(pady=5)

save_button = ctk.CTkButton(root, text="Save", command=create_new_file, width=200)
save_button.pack(pady=10)

exit_button = ctk.CTkButton(root, text="Exit", command=exit_application, width=200)
exit_button.pack(side="bottom", pady=10)

root.mainloop()
