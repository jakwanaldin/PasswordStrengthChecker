import re
import random
import string
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

  # For adding icons


# Function to check password strength
def check_password_strength(event=None):
    password = password_entry.get()
    strength = 0
    suggestions = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Increase the password length to at least 8 characters.")

    # Uppercase, lowercase, number, special character checks
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    if re.search(r'\d', password):
        strength += 1
    else:
        suggestions.append("Add at least one number.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        suggestions.append("Add at least one special character.")

    # Determine strength rating and color
    if strength <= 2:
        rating = "Weak"
        color = "red"
    elif strength == 3:
        rating = "Moderate"
        color = "orange"
    else:
        rating = "Strong"
        color = "green"

    # Update feedback label and progress bar
    feedback_label.config(text=f"Password Strength: {rating}", fg=color)
    progress_bar["value"] = strength * 20  # Scale strength to 0-100

    # Display suggestions
    suggestions_text.set("\n".join(suggestions) if suggestions else "Your password looks good!")


# Function to generate a strong password
def generate_password():
    length = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    check_password_strength()


# Function to display tooltip
def show_tooltip(widget, text):
    tooltip = tk.Toplevel(widget)
    tooltip.wm_overrideredirect(True)
    tooltip.geometry(f"+{widget.winfo_rootx() + 20}+{widget.winfo_rooty() + 20}")
    label = tk.Label(tooltip, text=text, font=("Arial", 10), bg="yellow", relief="solid", borderwidth=1)
    label.pack()
    widget.tooltip = tooltip


def hide_tooltip(widget):
    if hasattr(widget, "tooltip"):
        widget.tooltip.destroy()
        del widget.tooltip


# Create the GUI
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("600x500")
root.config(bg="#f0f4f8")  # Light background color

# Add title label
title_label = tk.Label(root, text="Password Strength Checker", font=("Arial", 20, "bold"), bg="#f0f4f8", fg="#333")
title_label.pack(pady=10)

# Add a frame for the input section
input_frame = tk.Frame(root, bg="#f0f4f8")
input_frame.pack(pady=20)

# Add a label and entry field for the password
label = tk.Label(input_frame, text="Enter your password:", font=("Arial", 14), bg="#f0f4f8", fg="#333")
label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

password_entry = tk.Entry(input_frame, show="*", font=("Arial", 14), width=30)
password_entry.grid(row=0, column=1, padx=10, pady=5)
password_entry.bind("<KeyRelease>", check_password_strength)  # Real-time feedback

# Add a progress bar
progress_bar = ttk.Progressbar(root, length=400, mode="determinate", maximum=100)
progress_bar.pack(pady=10)

# Add feedback label
feedback_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f4f8", fg="#333")
feedback_label.pack(pady=5)

# Add a suggestions section
suggestions_text = tk.StringVar()
suggestions_label = tk.Label(root, textvariable=suggestions_text, font=("Arial", 12), fg="#555", bg="#f0f4f8",
                             wraplength=500, justify="left")
suggestions_label.pack(pady=10)

# Add a frame for buttons
button_frame = tk.Frame(root, bg="#f0f4f8")
button_frame.pack(pady=20)

# Add icons to buttons
generate_icon = ImageTk.PhotoImage(Image.open("generate_icon.png").resize((20, 20)))
clear_icon = ImageTk.PhotoImage(Image.open("clear_icon.png").resize((20, 20)))

# Add a button to generate a strong password
generate_button = tk.Button(button_frame, text=" Generate Password", image=generate_icon, compound="left",
                            command=generate_password, font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=5,
                            relief="flat")
generate_button.grid(row=0, column=0, padx=10)
generate_button.bind("<Enter>", lambda e: show_tooltip(generate_button, "Click to generate a strong password"))
generate_button.bind("<Leave>", lambda e: hide_tooltip(generate_button))

# Add a button to clear the input
clear_button = tk.Button(button_frame, text=" Clear", image=clear_icon, compound="left",
                         command=lambda: password_entry.delete(0, tk.END), font=("Arial", 12), bg="#f44336", fg="white",
                         padx=10, pady=5, relief="flat")
clear_button.grid(row=0, column=1, padx=10)
clear_button.bind("<Enter>", lambda e: show_tooltip(clear_button, "Click to clear the password field"))
clear_button.bind("<Leave>", lambda e: hide_tooltip(clear_button))

# Run the application
root.mainloop()
