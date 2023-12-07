import csv
import tkinter as tk
from tkinter import ttk
import winsound
import time

class MorseCodeConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Morse Code Converter")
        self.root.geometry("400x240")

        self.pitch = tk.IntVar(value=1000)
        self.morse_code_dict = self.load_morse_code_mapping('morse_code_mapping.csv')

        self.create_widgets()

    def load_morse_code_mapping(self, file_path):
        morse_code_dict = {}
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                char, morse_code = row
                morse_code_dict[char] = morse_code
        return morse_code_dict

    def create_widgets(self):
        text_label = ttk.Label(self.root, text="Enter text:", font=('S', 16))
        text_entry = ttk.Entry(self.root, font=('Verdana', 12))
        convert_button = ttk.Button(self.root, text="Convert", command=self.text_to_morse, style="TButton")
        morse_output = ttk.Label(self.root, text="", wraplength=400, font=("Verdana", 16))
        slider_label = ttk.Label(self.root, text="Pitch", font=('Verdana', 10))
        slider = ttk.Scale(self.root, variable=self.pitch, from_=500, to=2000, orient=tk.HORIZONTAL, length=200)

        text_label.place(relx=0.15, rely=0.2)
        text_entry.place(relx=0.4, rely=0.2)
        convert_button.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
        morse_output.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
        slider_label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
        slider.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

        self.text_entry = text_entry
        self.morse_output = morse_output

        # Bind Enter key to Convert button
        self.root.bind("<Return>", lambda event: convert_button.invoke())

    def text_to_morse(self):
        text_input = self.text_entry.get().upper()
        morse_result = []

        for char in text_input:
            if char in self.morse_code_dict:
                morse_sequence = self.morse_code_dict[char]
                morse_result.append(morse_sequence)

        self.morse_output.configure(text=' '.join(morse_result))

        for morse_sequence in morse_result:
            for symbol in morse_sequence:
                if symbol == '.':
                    winsound.Beep(self.pitch.get(), 200)  # Play a short beep (1000 Hz) for 200 milliseconds
                    time.sleep(0.2)  # Short beep duration
                elif symbol == '-':
                    winsound.Beep(self.pitch.get(), 500)  # Play a long beep (1000 Hz) for 500 milliseconds
                    time.sleep(0.5)  # Long beep duration
                else:
                    time.sleep(0.2)  # Space between symbols
            time.sleep(0.4)  # Space between letters

if __name__ == "__main__":
    root = tk.Tk()
    app = MorseCodeConverterApp(root)
    root.mainloop()
