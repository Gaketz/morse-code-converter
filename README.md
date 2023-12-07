Morse Code Converter
This simple Python application converts text to Morse code and plays the corresponding beep sounds. It provides a graphical user interface (GUI) built using the Tkinter library.
Features
Convert text to Morse code
Play Morse code as beep sounds
Adjust pitch with a slider
Getting Started
Prerequisites
Python 3.x
Tkinter library (usually included in Python installations)
Installation
Clone the repository:
bash
git clone https://github.com/Gaketz/morse-code-converter.git
cd morse-code-converter

Run the application:
bash
python main.py

Usage
Enter the desired text in the provided text entry field.
Press the "Convert" button or hit Enter to convert the text to Morse code.
Adjust the pitch using the slider.
Listen to the Morse code as beep sounds.
Morse Code Mapping
The application reads Morse code mappings from the morse_code_mapping.csv file. You can customize this file to add or modify Morse code mappings for different characters.
Morse Code Mapping CSV Format
The CSV file should have two columns: one for characters and another for corresponding Morse code. The format should be as follows:
css
A,-.
B,-...
C,-.-.
...

Author
Gabriel Beronja
GitHub: Gaketz
LinkedIn: Gabriel Beronja
License
This project is licensed under the MIT License - see the LICENSE file for details.
