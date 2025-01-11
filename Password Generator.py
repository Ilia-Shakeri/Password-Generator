import random, string
import tkinter as tk
import pyperclip, subprocess

class PasswordGeneratorApp:
    def __init__(self):
        #creating the main window
        self.window = tk.Tk()
        self.window.title("Password Generator")
        self.window.geometry("380x240")
        
        #creating the length input
        length_label = tk.Label(
            self.window, text="Password length: ", font=("",12))
        length_label.grid(row=0, column=0, sticky=tk.W)

        #creating the spinbox for length
        self.length_var = tk.IntVar(value=8)
        self.length_spinbox = tk.Spinbox(self.window, from_=1, to=100, width=5, font=("",12), textvariable=self.length_var)
        self.length_spinbox.grid(row=0, column=1)

        #creating the lowercase set checkbox
        self.lowercase_var = tk.BooleanVar()
        lowercase_checkbox = tk.Checkbutton(self.window, text="Lowercase", variable=self.lowercase_var, font=("",12))
        lowercase_checkbox.grid(row=1, column=0, sticky=tk.W)

        #creating the uppercase set checkbox
        self.uppercase_var =tk.BooleanVar()
        uppercase_checkbox = tk.Checkbutton(self.window, text="Uppercase", variable=self.uppercase_var, font=("",12))
        uppercase_checkbox.grid(row=2, column=0, sticky=tk.W)

        #creating the digit set checkbox
        self.digits_var = tk.BooleanVar()
        digits_checkbox = tk.Checkbutton(self.window, text="Digits", variable=self.digits_var, font=("", 12))
        digits_checkbox.grid(row=3, column=0, sticky=tk.W)

        #creating the symbol set checkbox
        self.symbols_var = tk.BooleanVar()
        symbols_checkbox = tk.Checkbutton(self.window, text="Symbols", variable=self.symbols_var, font=("",12))
        symbols_checkbox.grid(row=4, column=0, sticky=tk.W)
        
        #creating the generate button
        generate_button = tk.Button(self.window, text="Generate", command=self.generate_password, font=("",12), width= 18)
        generate_button.grid(row=6, column=0, sticky=tk.W)

        #creating the password display box
        #self.password_display = tk.Entry(self.window, show=".")
        self.password_display = tk.Entry(self.window, width=40,justify="center")
        self.password_display.grid(row=5, columnspan=2)

        #creating the copy button
        copy_button = tk.Button(self.window, text="Copy To Clipboard", command=self.copy_password, font=("",12), width=18)
        copy_button.grid(row=6, column=1, )

        #start the main loop
        self.window.mainloop()

    def generate_password(self):
        #generate a password with current settings and display it
        length = int(self.length_var.get())
        lowercase = self.lowercase_var.get()
        uppercase = self.uppercase_var.get()
        digits = self.digits_var.get()
        symbols = self.symbols_var.get()
        try:
            #generate a password with given parameters
            characters = ""
            if lowercase:
                characters += string.ascii_lowercase
            if uppercase:
                characters += string.ascii_uppercase
            if digits:
                characters += string.digits
            if symbols:
                characters += string.punctuation
            if not characters:
                raise ValueError("At least one character set must be selected")
            password = "".join(random.choice(characters) 
                               for x in range(length))
            
            self.password_display.delete(0, tk.END)
            self.password_display.insert(0, password)
        except ValueError as error:
            self.password_display.delete(0, tk.END)
            self.password_display.insert(0, str(error))

    def copy_password(self):
        #copy the password displayed in the password display to clipboard
        password = self.password_display.get()
        if password:
            #windows
            pyperclip.copy(password)
            #linux:
            #subprocess.run(["xclip", "-selection", "clipboard"], input=password.encode("utf-8"))

if __name__ == "__main__":
    app = PasswordGeneratorApp()
