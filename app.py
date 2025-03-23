import tkinter as tk
from tkinter import messagebox

# Function to evaluate the disease based on input values
def diagnose_disease():
    # Retrieve input data from the user
    category = disease_category.get()
    age = int(age_entry.get())
    
    # Default messages
    diagnosis_message = ""
    
    # For Diabetes (type 1 or type 2)
    if category == "Diabetes":
        glucose_level = int(glucose_entry.get())
        insulin_level = int(insulin_entry.get())
        blood_pressure = int(blood_pressure_entry.get())
        
        if glucose_level > 180 or insulin_level > 20 or blood_pressure > 140:
            diagnosis_message = "You have Diabetes. Please consult a doctor for further treatment."
        else:
            diagnosis_message = "You do not have Diabetes. However, maintain a healthy lifestyle."
    
    # For Heart Disease
    elif category == "Heart Disease":
        cholesterol = int(cholesterol_entry.get())
        age = int(age_entry.get())
        
        if cholesterol > 240 or age > 50:
            diagnosis_message = "You are at high risk for Heart Disease. Please consult a doctor."
        else:
            diagnosis_message = "You are at a low risk for Heart Disease. Continue maintaining a healthy lifestyle."
    
    # For Lung Disease (like asthma, COPD)
    elif category == "Lung Disease":
        smoking_history = smoking_var.get()
        shortness_of_breath = shortness_var.get()
        
        if smoking_history == "Yes" or shortness_of_breath == "Yes":
            diagnosis_message = "You may have Lung Disease. Consult a specialist for an evaluation."
        else:
            diagnosis_message = "You likely do not have Lung Disease. Keep monitoring your health."
    
    # For Cold/Flu
    elif category == "Cold/Flu":
        fever = fever_var.get()
        cough = cough_var.get()
        fatigue = fatigue_var.get()
        
        if fever == "Yes" and cough == "Yes":
            diagnosis_message = "You might have Cold or Flu. Please rest and stay hydrated."
        else:
            diagnosis_message = "You likely do not have Cold/Flu, but continue monitoring symptoms."

    # Show the diagnosis message
    messagebox.showinfo("Diagnosis Result", diagnosis_message)

# Create the GUI window
root = tk.Tk()
root.title("AI-Powered Medical Diagnosis System")

# Create a label for disease category
category_label = tk.Label(root, text="Select Disease Category:")
category_label.grid(row=0, column=0)

# Dropdown menu to select disease category
disease_category = tk.StringVar()
disease_category.set("Diabetes")  # Default value
categories = ["Diabetes", "Heart Disease", "Lung Disease", "Cold/Flu"]
category_menu = tk.OptionMenu(root, disease_category, *categories)
category_menu.grid(row=0, column=1)

# Create input fields for Diabetes category
age_label = tk.Label(root, text="Enter Age:")
age_label.grid(row=1, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1)

glucose_label = tk.Label(root, text="Glucose Level (mg/dl):")
glucose_label.grid(row=2, column=0)
glucose_entry = tk.Entry(root)
glucose_entry.grid(row=2, column=1)

insulin_label = tk.Label(root, text="Insulin Level (µU/mL):")
insulin_label.grid(row=3, column=0)
insulin_entry = tk.Entry(root)
insulin_entry.grid(row=3, column=1)

blood_pressure_label = tk.Label(root, text="Blood Pressure (mmHg):")
blood_pressure_label.grid(row=4, column=0)
blood_pressure_entry = tk.Entry(root)
blood_pressure_entry.grid(row=4, column=1)

# Create Heart Disease input fields
cholesterol_label = tk.Label(root, text="Cholesterol Level (mg/dL):")
cholesterol_label.grid(row=5, column=0)
cholesterol_entry = tk.Entry(root)
cholesterol_entry.grid(row=5, column=1)

# Create Lung Disease input fields
smoking_label = tk.Label(root, text="Do you smoke? (Yes/No):")
smoking_label.grid(row=6, column=0)
smoking_var = tk.StringVar(value="No")
smoking_entry = tk.Entry(root, textvariable=smoking_var)
smoking_entry.grid(row=6, column=1)

shortness_label = tk.Label(root, text="Do you experience shortness of breath? (Yes/No):")
shortness_label.grid(row=7, column=0)
shortness_var = tk.StringVar(value="No")
shortness_entry = tk.Entry(root, textvariable=shortness_var)
shortness_entry.grid(row=7, column=1)

# Create Cold/Flu input fields
fever_label = tk.Label(root, text="Do you have a fever? (Yes/No):")
fever_label.grid(row=8, column=0)
fever_var = tk.StringVar(value="No")
fever_entry = tk.Entry(root, textvariable=fever_var)
fever_entry.grid(row=8, column=1)

cough_label = tk.Label(root, text="Do you have a cough? (Yes/No):")
cough_label.grid(row=9, column=0)
cough_var = tk.StringVar(value="No")
cough_entry = tk.Entry(root, textvariable=cough_var)
cough_entry.grid(row=9, column=1)

fatigue_label = tk.Label(root, text="Do you feel fatigued? (Yes/No):")
fatigue_label.grid(row=10, column=0)
fatigue_var = tk.StringVar(value="No")
fatigue_entry = tk.Entry(root, textvariable=fatigue_var)
fatigue_entry.grid(row=10, column=1)

# Diagnose button
diagnose_button = tk.Button(root, text="Diagnose", command=diagnose_disease)
diagnose_button.grid(row=11, column=0, columnspan=2)

# Run the main event loop
root.mainloop()
