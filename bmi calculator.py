from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("BMI Calculator")
root.geometry("335x235")
root.resizable(FALSE, FALSE)
photo = PhotoImage(file="bmi_logo.png")
root.iconphoto(False, photo)
root.config(padx=20, pady=15)

def calculate():
    # Get the weight entered and convert to an int
    weight = int(weight_entry.get())

    # Get the height entered and convert to an int
    height_cm = int(height_entry.get())

    # Convert from centmetres to metres
    height_m = (height_cm/100)*(height_cm/100)

    # Calculate the bmi and convert to float and round to 1 decimal place
    bmi = float(format(weight/height_m, ".1f"))
    
    if (bmi < 18.5):
        var_1.set(f"Your BMI : {bmi}\n Underweight")
    
    elif (bmi >= 18.5 and bmi <= 24.9):
        var_1.set(f"Your BMI : {bmi}\n Normal")
    
    elif (bmi >= 25 and bmi <= 29.9):
        var_1.set(f"Your BMI : {bmi}\n Overweight")
    
    else:
        var_1.set(f"Your BMI : {bmi}\n Obese")

var_1 = StringVar()

weight_label = customtkinter.CTkLabel(root, text="Weight (kg) :", font=("Roboto",14), text_color="#FFFFFF")
weight_label.place(x=15, y=20)

# Weight entry 
weight_entry = customtkinter.CTkEntry(root, 
    placeholder_text="Weight",
    corner_radius=5)
weight_entry.grid(column=1, row=0, padx=130, pady=20)

height_label = customtkinter.CTkLabel(root, text="Height (cm) :", font=("Roboto",14), text_color="#FFFFFF")
height_label.place(x=15, y=78)

# Height entry
height_entry = customtkinter.CTkEntry(root, 
    placeholder_text="Height",
    corner_radius=5)
height_entry.grid(column=1, row=1, padx=130, pady=10)

# Submit button
submit_button = customtkinter.CTkButton(root, 
    text="Submit",
    font=("Roboto", 14),
    command=calculate)
submit_button.place(x=85, y=130)

# BMI result 
result_label = customtkinter.CTkLabel(root, 
    textvariable=var_1,
    font=("Robot", 14),
    width=150)
result_label.place(x=80, y=165)

root.mainloop()