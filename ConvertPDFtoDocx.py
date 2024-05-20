import tkinter as tk
from tkinter import filedialog, messagebox
from pdf2docx import Converter

def select_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        pdf_path_var.set(file_path)

def convert_pdf_to_word():
    pdf_path = pdf_path_var.get()
    if not pdf_path:
        messagebox.showerror("Error", "Por favor, seleccione un archivo PDF.")
        return
    
    save_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word files", "*.docx")])
    if save_path:
        try:
            cv = Converter(pdf_path)
            cv.convert(save_path, start=0, end=None)
            cv.close()
            messagebox.showinfo("Éxito", f"Archivo convertido y guardado en: {save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo convertir el archivo: {e}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Convertidor de PDF a Word")

# Variable para guardar la ruta del PDF
pdf_path_var = tk.StringVar()

# Etiqueta y campo de entrada para la ruta del PDF
tk.Label(root, text="Archivo PDF:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=pdf_path_var, width=50).grid(row=0, column=1, padx=10, pady=10)

# Botón para seleccionar el archivo PDF
tk.Button(root, text="Seleccionar PDF", command=select_pdf).grid(row=0, column=2, padx=10, pady=10)

# Botón para iniciar la conversión
tk.Button(root, text="Convertir a Word", command=convert_pdf_to_word).grid(row=1, columnspan=3, pady=20)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
