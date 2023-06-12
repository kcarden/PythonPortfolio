import requests
from tkinter import *
from datetime import datetime, timedelta

class AppointmentGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Appointment Keeping")
        
        # Initialize appointments list
        self.appointments = []
        
        # Create appointment fields
        Label(root, text="Date and Time:").grid(row=0, column=0, sticky=W)
        self.date_var = StringVar()
        self.date_dropdown = OptionMenu(root, self.date_var, *self.get_date_options())
        self.date_dropdown.grid(row=0, column=1, padx=10, pady=5)
        self.date_var.set(self.get_default_date())
        
        Label(root, text="Time:").grid(row=1, column=0, sticky=W)
        self.time_var = StringVar()
        self.time_dropdown = OptionMenu(root, self.time_var, *self.get_time_options())
        self.time_dropdown.grid(row=1, column=1, padx=10, pady=5)
        self.time_var.set(self.get_default_time())
        
        Label(root, text="Vehicle:").grid(row=2, column=0, sticky=W)
        self.year_var = StringVar()
        self.make_var = StringVar()
        self.model_var = StringVar()
        
        self.year_dropdown = OptionMenu(root, self.year_var, *self.get_year_options())
        self.year_dropdown.grid(row=2, column=1, padx=10, pady=5)
        self.year_var.set("Select Year")
        self.year_dropdown.configure(width=10)
        
        self.make_dropdown = OptionMenu(root, self.make_var, "")
        self.make_dropdown.grid(row=3, column=1, padx=10, pady=5)
        self.make_var.set("Select Make")
        self.make_dropdown.configure(width=20, state=DISABLED)
        
        self.model_dropdown = OptionMenu(root, self.model_var, "")
        self.model_dropdown.grid(row=4, column=1, padx=10, pady=5)
        self.model_var.set("Select Model")
        self.model_dropdown.configure(width=30, state=DISABLED)
        
        # Bind make and model dropdowns to year selection
        self.year_var.trace("w", self.update_make_dropdown)
        self.make_var.trace("w", self.update_model_dropdown)
        
        Label(root, text="Name:").grid(row=5, column=0, sticky=W)
        self.name_entry = Entry(root)
        self.name_entry.grid(row=5, column=1, padx=10, pady=5)
        
        Label(root, text="Phone Number:").grid(row=6, column=0, sticky=W)
        self.phone_entry = Entry(root)
        self.phone_entry.grid(row=6, column=1, padx=10, pady=5)
        
        Label(root, text="Dealership:").grid(row=7, column=0, sticky=W)
        self.dealership_entry = Entry(root)
        self.dealership_entry.grid(row=7, column=1, padx=10, pady=5)
        
        # Create appointment button
        self.add_btn = Button(root, text="Add Appointment", command=self.add_appointment)
        self.add_btn.grid(row=8, column=0, columnspan=2, pady=10)
        
        # Create appointments listbox
        self.appointments_listbox = Listbox(root, width=60)
        self.appointments_listbox.grid(row=9, column=0, columnspan=2, padx=10)
        
    def add_appointment(self):
        # Get appointment details from entry fields
        date = self.date_var.get()
        time = self.time_var.get()
        year = self.year_var.get()
        make = self.make_var.get()
        model = self.model_var.get()
        name = self.name_entry.get()
        phone_number = self.phone_entry.get()
        dealership = self.dealership_entry.get()
        
        # Validate input
        if not self.validate_input(date, time, year, make, model, name, phone_number, dealership):
            return
        
        # Format date and time
        date_time = datetime.strptime(date, "%Y-%m-%d").strftime("%B %d, %Y") + " " + time
        
        # Add appointment to the list
        appointment = {
            "Date and Time": date_time,
            "Vehicle": f"{year} {make} {model}",
            "Name": name,
            "Phone Number": phone_number,
            "Dealership": dealership
        }
        self.appointments.append(appointment)
        
        # Clear entry fields
        self.name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.dealership_entry.delete(0, END)
        
        # Update appointments listbox
        self.update_appointments_listbox()
        
    def update_appointments_listbox(self):
        # Clear the listbox
        self.appointments_listbox.delete(0, END)
        
        # Populate the listbox with appointments
        for appointment in self.appointments:
            appointment_str = f"Date and Time: {appointment['Date and Time']}\n" \
                              f"Vehicle: {appointment['Vehicle']}\n" \
                              f"Name: {appointment['Name']}\n" \
                              f"Phone Number: {appointment['Phone Number']}\n" \
                              f"Dealership: {appointment['Dealership']}\n"
            self.appointments_listbox.insert(END, appointment_str)
        
    def get_date_options(self):
        date_options = []
        for i in range(3):
            date = datetime.now() + timedelta(days=i)
            date_str = date.strftime("%Y-%m-%d")
            date_options.append(date_str)
        return date_options
    
    def get_default_date(self):
        default_date = datetime.now().strftime("%Y-%m-%d")
        return default_date
    
    def get_time_options(self):
        time_options = []
        start_time = datetime.strptime("08:00 AM", "%I:%M %p")
        end_time = datetime.strptime("05:00 PM", "%I:%M %p")
        time_interval = timedelta(minutes=15)
        current_time = start_time
        while current_time <= end_time:
            time_str = current_time.strftime("%I:%M %p")
            time_options.append(time_str)
            current_time += time_interval
        return time_options
    
    def get_default_time(self):
        default_time = datetime.now().strftime("%I:%M %p")
        return default_time
    
    def get_year_options(self):
        current_year = datetime.now().year
        year_options = [str(year) for year in range(current_year - 20, current_year + 1)]
        return year_options
    
    def update_make_dropdown(self, *args):
        year = self.year_var.get()
        
        if year != "Select Year":
            make_options = self.get_make_options(year)
            self.make_dropdown.configure(state=NORMAL)
            self.make_dropdown['menu'].delete(0, END)
            
            for make in make_options:
                self.make_dropdown['menu'].add_command(label=make, command=lambda value=make: self.make_var.set(value))
        else:
            self.make_var.set("Select Make")
            self.make_dropdown.configure(state=DISABLED)
            self.model_var.set("Select Model")
            self.model_dropdown.configure(state=DISABLED)
            
    def update_model_dropdown(self, *args):
        year = self.year_var.get()
        make = self.make_var.get()
        
        if make != "Select Make":
            model_options = self.get_model_options(year, make)
            self.model_dropdown.configure(state=NORMAL)
            self.model_dropdown['menu'].delete(0, END)
            
            for model in model_options:
                self.model_dropdown['menu'].add_command(label=model, command=lambda value=model: self.model_var.set(value))
        else:
            self.model_var.set("Select Model")
            self.model_dropdown.configure(state=DISABLED)
            
    def get_make_options(self, year):
        url = f"https://the-vehicles-api.herokuapp.com/models?year={year}"
        response = requests.get(url)
        data = response.json()
        make_options = list(set([item["brand"]["brand"] for item in data]))
        make_options.sort()
        return make_options
    
    def get_model_options(self, year, make):
        url = f"https://the-vehicles-api.herokuapp.com/models?year={year}&brand={make}"
        response = requests.get(url)
        data = response.json()
        model_options = [item["model"] for item in data]
        return model_options
        
    def validate_input(self, date, time, year, make, model, name, phone_number, dealership):
        # Check if any field is empty
        if not all([date, time, year, make, model, name, phone_number, dealership]):
            messagebox.showerror("Error", "All fields must be filled.")
            return False
        
        return True

# Create the main window
root = Tk()

# Create the appointment GUI
appointment_gui = AppointmentGUI(root)

# Start the main event loop
root.mainloop()
