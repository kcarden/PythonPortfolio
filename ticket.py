import tkinter as tk
from tkinter import messagebox

class TicketingSystemGUI:
    def __init__(self):
        self.tickets = []

        self.window = tk.Tk()
        self.window.title("Ticketing System")

        self.create_ticket_widgets()
        self.display_tickets()

        self.window.mainloop()

    def create_ticket_widgets(self):
        # Ticket creation widgets
        tk.Label(self.window, text="Title:").grid(row=0, column=0, sticky=tk.W)
        self.title_entry = tk.Entry(self.window, width=30)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.window, text="Description:").grid(row=1, column=0, sticky=tk.W)
        self.description_entry = tk.Entry(self.window, width=30)
        self.description_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.window, text="Priority:").grid(row=2, column=0, sticky=tk.W)
        self.priority_entry = tk.Entry(self.window, width=30)
        self.priority_entry.grid(row=2, column=1, padx=5, pady=5)

        create_button = tk.Button(self.window, text="Create Ticket", command=self.create_ticket)
        create_button.grid(row=3, columnspan=2, padx=5, pady=5)

        # Ticket display widgets
        self.ticket_listbox = tk.Listbox(self.window, width=60)
        self.ticket_listbox.grid(row=4, columnspan=2, padx=5, pady=5)

        self.refresh_button = tk.Button(self.window, text="Refresh", command=self.display_tickets)
        self.refresh_button.grid(row=5, columnspan=2, padx=5, pady=5)

        # Right-click context menu
        self.context_menu = tk.Menu(self.window, tearoff=0)
        self.context_menu.add_command(label="Complete Ticket", command=self.complete_ticket)

        self.ticket_listbox.bind("<Button-3>", self.show_context_menu)

    def show_context_menu(self, event):
        self.ticket_listbox.selection_clear(0, tk.END)  # Clear previous selections
        self.ticket_listbox.activate(tk.ACTIVE)  # Set current item as active
        self.ticket_listbox.selection_set(self.ticket_listbox.nearest(event.y))  # Select the item under the cursor

        self.context_menu.post(event.x_root, event.y_root)

    def create_ticket(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        priority = self.priority_entry.get()

        if title and description and priority:
            ticket = {
                'title': title,
                'description': description,
                'priority': priority,
                'completed': False
            }
            self.tickets.append(ticket)
            messagebox.showinfo("Ticketing System", "Ticket created successfully.")
            self.clear_ticket_entries()
            self.display_tickets()
        else:
            messagebox.showerror("Ticketing System", "Please fill in all the fields.")

    def display_tickets(self):
        self.ticket_listbox.delete(0, tk.END)

        for index, ticket in enumerate(self.tickets, start=1):
            status = "Complete" if ticket['completed'] else "Pending"
            self.ticket_listbox.insert(tk.END, f"Ticket {index}: {ticket['title']} ({ticket['priority']}) - {status}")

    def complete_ticket(self):
        selected_index = self.ticket_listbox.curselection()[0]
        ticket = self.tickets[selected_index]
        ticket['completed'] = True

        log_entry = f"Ticket {selected_index + 1}: {ticket['title']} ({ticket['priority']}) - Completed\n"
        self.log_ticket(log_entry)

        self.tickets.pop(selected_index)
        self.display_tickets()

    def log_ticket(self, log_entry):
        with open('ticket_log.txt', 'a') as log_file:
            log_file.write(log_entry)

    def clear_ticket_entries(self):
        self.title_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)

# Example usage
ticketing_system_gui = TicketingSystemGUI()
