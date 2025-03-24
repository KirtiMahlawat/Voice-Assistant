import tkinter as tk
from tkinter import Scrollbar, Text
from threading import Thread
import time

class VoiceAssistantGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Voice Assistant GUI")
        self.master.geometry("600x400")

        self.output_text = Text(self.master, wrap="word", height=20, width=70)
        self.output_text.pack(pady=10)
        
        scrollbar = Scrollbar(self.master, command=self.output_text.yview)
        scrollbar.pack(side="right", fill="y")
        self.output_text.config(yscrollcommand=scrollbar.set)

        self.command_entry = tk.Entry(self.master, width=50)
        self.command_entry.pack(pady=10)

        self.submit_button = tk.Button(self.master, text="Submit Command", command=self.submit_command)
        self.submit_button.pack()

        # Redirect stdout to the Text widget
        sys.stdout = self

        # Run the assistant in a separate thread
        assistant_thread = Thread(target=self.run_assistant)
        assistant_thread.start()

    def write(self, text):
        self.output_text.insert(tk.END, text)
        self.output_text.see(tk.END)

    def submit_command(self):
        command = self.command_entry.get()
        print(f"User command: {command}")
        # Add logic to handle the command (you may want to communicate with your existing assistant logic here)
        # For simplicity, let's just print the command for now.

    def run_assistant(self):
        # Add your existing assistant code here
        # You may need to modify it to run continuously in the background and handle user input differently.

        # For demonstration, we'll just simulate the assistant responding every 5 seconds.
        while True:
            time.sleep(5)
            self.write("\nAssistant: I'm here to help!\n")

def main():
    root = tk.Tk()
    gui = VoiceAssistantGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
