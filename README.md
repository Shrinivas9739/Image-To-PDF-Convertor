# **🖼️ Image to PDF Converter**

## **📌 Description**
The **Image to PDF Converter** is a **GUI-based Python application** that allows users to select multiple images and convert them into a **single PDF file**.  
It uses **Tkinter** for the interface, **Pillow (PIL)** for image handling, and **ReportLab** for PDF generation.  

## **✨ Features**
- ✅ **Select multiple images** (PNG, JPG, JPEG, BMP)
- 📝 **Enter a custom name** for the output PDF
- 🖼️ **Automatically resizes images** to fit the PDF page
- 📂 **Saves the generated PDF** in the same directory
- 🖥️ **User-friendly GUI** built with Tkinter  

## **🛠️ Installation**
### **1️⃣ Install Python (if not installed)**
- Download and install **Python 3.x** from [Python's official website](https://www.python.org/downloads/).

- 🚀 How to Use
Run the script
1) **python app.py**
2) **Click "Select Images" and choose multiple images.**
3) **Enter the output PDF name (or leave it blank to use the default name "output.pdf").**
4) **Click "Convert to PDF" and wait for the success message.**
5) **Find your generated PDF in the same directory.**


### **2️⃣ Install Required Dependencies**

📝 Dependencies

1) tkinter → Built-in with Python (Used for GUI)

2) Pillow → Used for image handling (opening, resizing)

3) ReportLab → Generates PDF files from images

Run the following command in your terminal or command prompt:  
```sh
pip install pillow reportlab
