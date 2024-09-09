from datetime import datetime

# Function to load categories from a file
def load_categories(file_path):
    try:
        with open(file_path, 'r') as file:
            categories = [line.strip() for line in file.readlines()]
        return categories
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return []

# Initialize an empty list for tickets
tickets = []

# Function to display the main menu
def display_menu():
    print("\nWelcome to the Support Ticketing System")
    print("1. Create a new ticket")
    print("2. View all tickets")
    print("3. Update ticket status")
    print("4. Add a note to a ticket")
    print("5. See ticket history")
    print("6. Exit")

# Function to log changes in a ticket's history
def log_change(ticket, change_description):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ticket['history'].append(f"[{timestamp}] {change_description}")

# Function to create a new ticket
def create_ticket():
    while True:
        print("\nCreate a New Ticket")
        
        # Display categories to choose from
        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category}")
        
        category_choice = int(input("Select a category number or 0 to go back: ")) - 1
        
        if category_choice == -1:
            break  # Go back to the main menu
        elif 0 <= category_choice < len(categories):
            selected_category = categories[category_choice]
            issue_description = input("Describe the issue: ")
            
            # Create a ticket (as a dictionary)
            ticket = {
                'category': selected_category,
                'description': issue_description,
                'status': 'Open',
                'history': []  # Initialize history
            }
            
            # Log the ticket creation
            log_change(ticket, f"Ticket created with description: '{issue_description}'")
            
            tickets.append(ticket)
            print("Ticket created successfully!")
        else:
            print("Invalid category selected!")

# Function to view all tickets (basic details only)
def view_tickets():
    while True:
        if tickets:
            print("\nAll Tickets:")
            for i, ticket in enumerate(tickets, start=1):
                print(f"{i}. [{ticket['status']}] {ticket['category']}: {ticket['description']}")
            break
        else:
            print("No tickets available!")
        break

# Function to view the history of a specific ticket
def view_ticket_history():
    while True:
        if tickets:
            print("\nView Ticket History")
            
            # Display tickets
            for i, ticket in enumerate(tickets, start=1):
                print(f"{i}. [{ticket['status']}] {ticket['category']}: {ticket['description']}")
            
            ticket_choice = input("Select a ticket number to view history or 0 to go back: ")
            
            if ticket_choice == '0':
                break  # Go back to the main menu
            
            try:
                ticket_choice = int(ticket_choice) - 1
                if 0 <= ticket_choice < len(tickets):
                    print("\nTicket History:")
                    for log in tickets[ticket_choice]['history']:
                        print(f"   {log}")
                else:
                    print("Invalid ticket selected!")
            except ValueError:
                print("Invalid input!")
        else:
            print("No tickets available to view history.")
            break

# Function to update the status of a ticket
def update_ticket_status():
    while True:
        if tickets:
            print("\nUpdate Ticket Status")
            
            # Display tickets
            for i, ticket in enumerate(tickets, start=1):
                print(f"{i}. [{ticket['status']}] {ticket['category']}: {ticket['description']}")
            
            ticket_choice = input("Select a ticket number to update or 0 to go back: ")
            
            if ticket_choice == '0':
                break  # Go back to the main menu
            
            try:
                ticket_choice = int(ticket_choice) - 1
                if 0 <= ticket_choice < len(tickets):
                    # Show status options
                    print("\nChoose a new status:")
                    print("1. Open")
                    print("2. In Progress")
                    print("3. Closed")
                    
                    status_choice = input("Select the new status or 0 to go back: ")
                    
                    if status_choice == '0':
                        continue  # Go back to ticket selection
                    
                    old_status = tickets[ticket_choice]['status']
                    
                    if status_choice == '1':
                        tickets[ticket_choice]['status'] = 'Open'
                    elif status_choice == '2':
                        tickets[ticket_choice]['status'] = 'In Progress'
                    elif status_choice == '3':
                        tickets[ticket_choice]['status'] = 'Closed'
                    else:
                        print("Invalid status selected!")
                        continue

                    # Log the status change
                    new_status = tickets[ticket_choice]['status']
                    log_change(tickets[ticket_choice], f"Status changed from '{old_status}' to '{new_status}'")
                    
                    print("Ticket status updated successfully!")
                else:
                    print("Invalid ticket selected!")
            except ValueError:
                print("Invalid input!")
        else:
            print("No tickets available to update.")
            break

# Function to add a note to a ticket's history
def add_ticket_note():
    while True:
        if tickets:
            print("\nAdd a Note to Ticket History")
            
            # Display tickets
            for i, ticket in enumerate(tickets, start=1):
                print(f"{i}. [{ticket['status']}] {ticket['category']}: {ticket['description']}")
            
            ticket_choice = input("Select a ticket number to add a note to or 0 to go back: ")
            
            if ticket_choice == '0':
                break  # Go back to the main menu
            
            try:
                ticket_choice = int(ticket_choice) - 1
                if 0 <= ticket_choice < len(tickets):
                    note = input("Enter the note: ")
                    
                    # Log the note addition
                    log_change(tickets[ticket_choice], f"Note added: '{note}'")
                    
                    print("Note added successfully!")
                else:
                    print("Invalid ticket selected!")
            except ValueError:
                print("Invalid input!")
        else:
            print("No tickets available to add notes to.")
            break

# Main program loop
def run_ticket_system():
    while True:
        display_menu()
        choice = input("Please choose an option: ")
        
        if choice == '1':
            create_ticket()
        elif choice == '2':
            view_tickets()
        elif choice == '3':
            update_ticket_status()
        elif choice == '4':
            add_ticket_note()
        elif choice == '5':
            view_ticket_history()
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

# Load categories and run the system
categories = load_categories('categories.txt')
run_ticket_system()
