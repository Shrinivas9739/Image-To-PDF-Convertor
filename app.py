import tkinter as tk
from tkinter import filedialog, messagebox
import os
from reportlab.pdfgen import canvas
from PIL import Image


class ImageToPDFConverter:
    def __init__(self, root):
        self.root = root
        self.image_paths = []  # Store selected image paths
        self.output_pdf_name = tk.StringVar()
        self.selected_images_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, height=10, width=50)

        self.initialize_ui()

    def initialize_ui(self):
        title_label = tk.Label(self.root, text="Image to PDF Converter", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        select_images_button = tk.Button(self.root, text="Select Images", command=self.select_images)
        select_images_button.pack(pady=(0, 10))

        self.selected_images_listbox.pack(pady=(0, 10), fill=tk.BOTH, expand=True)

        label = tk.Label(self.root, text="Enter output PDF name:")
        label.pack()

        pdf_name_entry = tk.Entry(self.root, textvariable=self.output_pdf_name, width=40, justify='center')
        pdf_name_entry.pack()

        convert_button = tk.Button(self.root, text="Convert to PDF", command=self.convert_images_to_pdf)
        convert_button.pack(pady=(20, 40))

    def select_images(self):
        """Opens file dialog to select multiple images"""
        file_paths = filedialog.askopenfilenames(title="Select Images",
                                                 filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if file_paths:
            self.image_paths = file_paths
            self.update_selected_images_listbox()

    def update_selected_images_listbox(self):
        """Updates the listbox to show selected image file names"""
        self.selected_images_listbox.delete(0, tk.END)
        for image_path in self.image_paths:
            _, file_name = os.path.split(image_path)
            self.selected_images_listbox.insert(tk.END, file_name)

    def convert_images_to_pdf(self):
        """Converts selected images to a single PDF"""
        if not self.image_paths:
            messagebox.showwarning("No Images Selected", "Please select at least one image.")
            return

        output_pdf_name = self.output_pdf_name.get().strip()
        if not output_pdf_name:
            output_pdf_name = "output"

        output_pdf_path = output_pdf_name + ".pdf"

        pdf = canvas.Canvas(output_pdf_path, pagesize=(612, 792))  # Standard A4 size

        for image_path in self.image_paths:
            img = Image.open(image_path)
            img_width, img_height = img.size

            # Fit the image within the PDF page (leaving some margins)
            available_width = 540
            available_height = 720
            scale_factor = min(available_width / img_width, available_height / img_height)
            new_width = int(img_width * scale_factor)
            new_height = int(img_height * scale_factor)

            x_centered = (612 - new_width) / 2
            y_centered = (792 - new_height) / 2

            # Draw the image onto the PDF
            pdf.drawImage(image_path, x_centered, y_centered, width=new_width, height=new_height)
            pdf.showPage()

        pdf.save()
        messagebox.showinfo("Success", f"PDF saved as '{output_pdf_path}'")


def main():
    root = tk.Tk()
    root.title("Image to PDF Converter")
    root.geometry("400x600")
    root.resizable(False, False)

    # Instantiate the ImageToPDFConverter
    ImageToPDFConverter(root)

    root.mainloop()


if __name__ == "__main__":
    main()
