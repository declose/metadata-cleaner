import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os


def choose_file():
    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[
            ("Images", "*.jpg *.jpeg *.png"),
            ("All Files", "*.*")
        ]
    )

    if file_path:
        selected_file.set(file_path)


def clean_metadata():
    file_path = selected_file.get()

    if not file_path:
        messagebox.showwarning(
            "No File",
            "Please select an image first"
        )
        return

    try:
        image = Image.open(file_path)

        cleaned_image = Image.new(image.mode, image.size)
        cleaned_image.putdata(image.get_flattened_data())

        folder = os.path.dirname(file_path)
        filename = os.path.basename(file_path)

        name, extension = os.path.splitext(filename)

        output_file = os.path.join(
            folder,
            name + "_cleaned" + extension
        )

        cleaned_image.save(output_file)

        status.set("Metadata removed!")
        messagebox.showinfo(
            "Done",
            f"The cleaned up file has been saved here:\n\n{output_file}"
        )

    except Exception as error:
        messagebox.showerror(
            "Error",
            f"Something went wrong:\n\n{error}"
        )

window = tk.Tk()
window.iconbitmap("icon.ico")
window.title("Metadata Cleaner by declose")
window.geometry("500x350")
window.resizable(False, False)

selected_file = tk.StringVar()
status = tk.StringVar(value="No file has been selected yet")


title = tk.Label(
    window,
    text="Metadata Cleaner",
    font=("Arial", 24, "bold")
)
title.pack(pady=25)


description = tk.Label(
    window,
    text="Select an image and remove its metadata.",
    font=("Arial", 11)
)
description.pack(pady=5)


select_button = tk.Button(
    window,
    text="Select a file",
    bg="#D8A6BD",
    command=choose_file,
    width=25,
    height=2
)
select_button.pack(pady=20)


file_label = tk.Label(
    window,
    textvariable=selected_file,
    wraplength=430,
    fg="gray"
)
file_label.pack()


clean_button = tk.Button(
    window,
    text="EXECUTE METADATA",
    command=clean_metadata,
    width=25,
    height=2,
    bg="#46AC37",
    fg="white",
    font=("Arial", 11, "bold")
)
clean_button.pack(pady=25)


status_label = tk.Label(
    window,
    textvariable=status,
    fg="green"
)
status_label.pack()

window.mainloop()