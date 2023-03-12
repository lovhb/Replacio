import customtkinter
from customtkinter import filedialog
from customtkinter import *
import replacefiles

# Set appearance and color theme of the GUI
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

OPTIONS = {
    "Replace Files": replacefiles.replace_files,
    "Copy Files": replacefiles.copy_files
}
        
class ReplacioGUI:
    def __init__(self, master):
        self.master = master
        self.master.geometry("750x600")
        self.master.title("Replacio")
        
        # Create StringVars to hold the paths of the source and destination folders
        self.source_folder_path = StringVar()
        self.destination_folder_path = StringVar()

        # Call the create_widgets method to build the GUI
        self.create_widgets()

    def create_widgets(self):
        # Create the first frame for the "Source Folder" section
        self.frame1 = customtkinter.CTkFrame(master=self.master)
        self.frame1.pack(side="top", pady=20, padx=60, fill="x", expand=True)

        # Create the label for the "Source Folder" section
        self.label1 = customtkinter.CTkLabel(master=self.frame1, text="Source Folder", font=("Arial", 30))
        self.label1.pack(pady=12, padx=10)

        # Create the entry for the "Source Folder" section
        self.entry1 = customtkinter.CTkEntry(master=self.frame1, textvariable=self.source_folder_path)
        self.entry1.pack(pady=12, padx=100)

        # Create the "Browse" button for the "Source Folder" section
        self.button1 = customtkinter.CTkButton(master=self.frame1, text="Browse", command=self.browse_source)
        self.button1.pack(pady=12, padx=10)

        # Create the second frame for the "Destination Folder" section
        self.frame2 = customtkinter.CTkFrame(master=self.master)
        self.frame2.pack(side="top", pady=20, padx=60, fill="x", expand=True)

        # Create the label for the "Destination Folder" section
        self.label2 = customtkinter.CTkLabel(master=self.frame2, text="Destination Folder", font=("Arial", 30))
        self.label2.pack(pady=12, padx=10)

        # Create the entry for the "Destination Folder" section
        self.entry2 = customtkinter.CTkEntry(master=self.frame2, textvariable=self.destination_folder_path)
        self.entry2.pack(pady=12, padx=10)

        # Create the "Browse" button for the "Destination Folder" section
        self.button2 = customtkinter.CTkButton(master=self.frame2, text="Browse", command=self.browse_destination)
        self.button2.pack(pady=12, padx=10)

        # Create the third frame for the "Replace or copy files" section
        self.frame3 = customtkinter.CTkFrame(master=self.master)
        self.frame3.pack(side="top", pady=20, padx=60, fill="x", expand=True)

        # Create the label for the "Replace or copy files" section
        self.label3 = customtkinter.CTkLabel(master=self.frame3, text="Replace or copy files from source to destination?", font=("Arial", 16))
        self.label3.pack(pady=12, padx=10)

        # Create the OptionMenu for the "Replace or copy files" section
        self.optionmenu1 = customtkinter.CTkOptionMenu(master=self.frame3, values=["Replace Files", "Copy Files"])
        self.optionmenu1.pack(pady=12, padx=10)

        # Create a button labeled "Start" in the frame3 window, with the command "run" assigned to it. 
        self.button3 = customtkinter.CTkButton(master=self.frame3, text="Start", command=self.run)
        self.button3.pack(pady=12, padx=10)

    def browse_source(self):
        source_filename = filedialog.askdirectory()
        self.source_folder_path.set(source_filename)
        print(source_filename)

    def browse_destination(self):
        destination_filename = filedialog.askdirectory()
        self.destination_folder_path.set(destination_filename)
        print(destination_filename)

    def run(self):
        option = self.optionmenu1.get()
        func = OPTIONS.get(option)
        if func:
            func(source_dir_var=self.source_folder_path, destination_dir_var=self.destination_folder_path)
            print("Done!")
            self.button3.configure(text="Done! Click again to start")
        else:
            print("Invalid option selected.")

if __name__ == "__main__":
    root = customtkinter.CTk()
    ReplacioGUI(root)
    root.mainloop()