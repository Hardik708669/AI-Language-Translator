import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as tb
from deep_translator import GoogleTranslator
from langdetect import detect

LANGUAGES = {
    "English": "en", "Spanish": "es", "French": "fr", "German": "de", "Chinese": "zh-CN",
    "Hindi": "hi", "Arabic": "ar", "Portuguese": "pt", "Russian": "ru", "Japanese": "ja",
    "Korean": "ko", "Italian": "it", "Turkish": "tr", "Dutch": "nl", "Greek": "el",
    "Hebrew": "he", "Indonesian": "id", "Swedish": "sv", "Polish": "pl", "Thai": "th"
}

LANGUAGE_CODES = {v: k for k, v in LANGUAGES.items()}

root = tb.Window(themename="cyborg")
root.title("AI Language Translator")
root.geometry("600x500")

frame = ttk.Frame(root, padding=15)
frame.pack(pady=10)

title_label = ttk.Label(frame, text="AI Language Translator", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

input_text = tk.Text(frame, height=5, width=50, font=("Arial", 11))
input_text.grid(row=1, column=0, columnspan=2, pady=5)

def detect_language():
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter text to detect language!")
        return
    try:
        detected_code = detect(text)
        detected_lang = LANGUAGE_CODES.get(detected_code, "Unknown")
        messagebox.showinfo("Detected Language", f"Detected Language: {detected_lang} ({detected_code})")
    except Exception as e:
        messagebox.showerror("Error", f"Language detection failed: {str(e)}")

detect_button = tb.Button(frame, text="🌍 Detect Language", bootstyle="info", command=detect_language)
detect_button.grid(row=2, column=0, columnspan=2, pady=5)

ttk.Label(frame, text="Select Target Language:", font=("Arial", 11)).grid(row=3, column=0, pady=5)
selected_lang = tk.StringVar(value="English")
lang_menu = ttk.Combobox(frame, textvariable=selected_lang, values=list(LANGUAGES.keys()), font=("Arial", 11))
lang_menu.grid(row=3, column=1, pady=5)

def translate_text():
    text = input_text.get("1.0", tk.END).strip()
    target_lang = LANGUAGES.get(selected_lang.get(), "en")
    
    if not text:
        messagebox.showwarning("Warning", "Please enter text to translate!")
        return

    try:
        translated_text = GoogleTranslator(source="auto", target=target_lang).translate(text)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated_text)
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {str(e)}")

translate_button = tb.Button(frame, text="🔄 Translate", bootstyle="success", command=translate_text)
translate_button.grid(row=4, column=0, columnspan=2, pady=10)

output_text = tk.Text(root, height=5, width=60, font=("Arial", 11), fg="green")
output_text.pack(pady=10)

root.mainloop()