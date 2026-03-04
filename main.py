import threading
import tkinter.messagebox as mb
import customtkinter
from customtkinter import filedialog
from customtkinter import *
import replacefiles

# Set appearance and color theme of the GUI
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

OPTIONS = {
    "Replace Files": replacefiles.replace_files,
    "Copy Files": replacefiles.copy_files,
}


class ReplacioGUI:
    def __init__(self, master):
        self.master = master
        self.master.geometry("750x700")
        self.master.title("Replacio")
        self.master.resizable(True, True)
        self.master.minsize(600, 600)

        # StringVars for folder paths
        self.source_folder_path = StringVar()
        self.destination_folder_path = StringVar()

        self._running = False

        self.create_widgets()

    def create_widgets(self):
        # ── Top bar: appearance mode toggle ──────────────────────────────────
        self.topbar = customtkinter.CTkFrame(master=self.master, fg_color="transparent")
        self.topbar.pack(side="top", fill="x", padx=20, pady=(10, 0))

        self.appearance_label = customtkinter.CTkLabel(
            master=self.topbar, text="Appearance:", anchor="w"
        )
        self.appearance_label.pack(side="left", padx=(0, 6))

        self.appearance_menu = customtkinter.CTkOptionMenu(
            master=self.topbar,
            values=["System", "Dark", "Light"],
            width=110,
            command=self._change_appearance,
        )
        self.appearance_menu.pack(side="left")

        # ── Source Folder ─────────────────────────────────────────────────────
        self.frame1 = customtkinter.CTkFrame(master=self.master)
        self.frame1.pack(side="top", pady=(14, 6), padx=40, fill="x")

        self.label1 = customtkinter.CTkLabel(
            master=self.frame1, text="Source Folder", font=("Arial", 24, "bold")
        )
        self.label1.pack(pady=(12, 4), padx=10)

        entry_frame1 = customtkinter.CTkFrame(master=self.frame1, fg_color="transparent")
        entry_frame1.pack(fill="x", padx=16, pady=(0, 12))

        self.entry1 = customtkinter.CTkEntry(
            master=entry_frame1,
            textvariable=self.source_folder_path,
            placeholder_text="Select source folder...",
        )
        self.entry1.pack(side="left", fill="x", expand=True, padx=(0, 8))

        self.button1 = customtkinter.CTkButton(
            master=entry_frame1, text="Browse", width=90, command=self.browse_source
        )
        self.button1.pack(side="left")

        # ── Destination Folder ────────────────────────────────────────────────
        self.frame2 = customtkinter.CTkFrame(master=self.master)
        self.frame2.pack(side="top", pady=6, padx=40, fill="x")

        self.label2 = customtkinter.CTkLabel(
            master=self.frame2, text="Destination Folder", font=("Arial", 24, "bold")
        )
        self.label2.pack(pady=(12, 4), padx=10)

        entry_frame2 = customtkinter.CTkFrame(master=self.frame2, fg_color="transparent")
        entry_frame2.pack(fill="x", padx=16, pady=(0, 12))

        self.entry2 = customtkinter.CTkEntry(
            master=entry_frame2,
            textvariable=self.destination_folder_path,
            placeholder_text="Select destination folder...",
        )
        self.entry2.pack(side="left", fill="x", expand=True, padx=(0, 8))

        self.button2 = customtkinter.CTkButton(
            master=entry_frame2, text="Browse", width=90, command=self.browse_destination
        )
        self.button2.pack(side="left")

        # ── Action section ────────────────────────────────────────────────────
        self.frame3 = customtkinter.CTkFrame(master=self.master)
        self.frame3.pack(side="top", pady=6, padx=40, fill="x")

        self.label3 = customtkinter.CTkLabel(
            master=self.frame3,
            text="Operation",
            font=("Arial", 24, "bold"),
        )
        self.label3.pack(pady=(12, 4), padx=10)

        action_row = customtkinter.CTkFrame(master=self.frame3, fg_color="transparent")
        action_row.pack(padx=16, pady=(0, 12))

        self.optionmenu1 = customtkinter.CTkOptionMenu(
            master=action_row,
            values=["Replace Files", "Copy Files"],
            width=160,
        )
        self.optionmenu1.pack(side="left", padx=(0, 12))

        self.start_button = customtkinter.CTkButton(
            master=action_row, text="Start", width=100, command=self.run
        )
        self.start_button.pack(side="left", padx=(0, 8))

        self.clear_button = customtkinter.CTkButton(
            master=action_row,
            text="Clear",
            width=80,
            fg_color="gray40",
            hover_color="gray30",
            command=self.clear,
        )
        self.clear_button.pack(side="left")

        # ── Log / status area ─────────────────────────────────────────────────
        log_frame = customtkinter.CTkFrame(master=self.master)
        log_frame.pack(side="top", pady=(6, 14), padx=40, fill="both", expand=True)

        log_label = customtkinter.CTkLabel(
            master=log_frame, text="Log", font=("Arial", 16, "bold"), anchor="w"
        )
        log_label.pack(pady=(8, 2), padx=12, anchor="w")

        self.log_box = customtkinter.CTkTextbox(master=log_frame, state="disabled", wrap="word")
        self.log_box.pack(fill="both", expand=True, padx=12, pady=(0, 10))

    # ── Helpers ───────────────────────────────────────────────────────────────

    def _change_appearance(self, mode: str):
        customtkinter.set_appearance_mode(mode)

    def _log(self, message: str):
        """Append a line to the log textbox (thread-safe via after())."""
        def _append():
            self.log_box.configure(state="normal")
            self.log_box.insert("end", message + "\n")
            self.log_box.see("end")
            self.log_box.configure(state="disabled")
        self.master.after(0, _append)

    def browse_source(self):
        path = filedialog.askdirectory()
        if path:
            self.source_folder_path.set(path)

    def browse_destination(self):
        path = filedialog.askdirectory()
        if path:
            self.destination_folder_path.set(path)

    def clear(self):
        self.source_folder_path.set("")
        self.destination_folder_path.set("")
        self.log_box.configure(state="normal")
        self.log_box.delete("1.0", "end")
        self.log_box.configure(state="disabled")
        self.start_button.configure(text="Start", state="normal")

    def run(self):
        if self._running:
            return

        source = self.source_folder_path.get().strip()
        destination = self.destination_folder_path.get().strip()

        if not source or not destination:
            mb.showerror(
                "Missing folders",
                "Please select both a source folder and a destination folder before starting.",
            )
            return

        option = self.optionmenu1.get()
        func = OPTIONS.get(option)
        if not func:
            return

        self._running = True
        self.start_button.configure(text="Running...", state="disabled")
        self._log(f"-- Starting: {option} --")
        self._log(f"Source      : {source}")
        self._log(f"Destination : {destination}")

        def _worker():
            try:
                count, skipped = func(
                    source_dir_var=self.source_folder_path,
                    destination_dir_var=self.destination_folder_path,
                    log_func=self._log,
                )
                self._log(f"-- Done: {count} file(s) processed, {skipped} skipped --")
            except Exception as exc:
                self._log(f"Unexpected error: {exc}")
            finally:
                self._running = False
                self.master.after(0, lambda: self.start_button.configure(
                    text="Start", state="normal"
                ))

        threading.Thread(target=_worker, daemon=True).start()


if __name__ == "__main__":
    root = customtkinter.CTk()
    ReplacioGUI(root)
    root.mainloop()
