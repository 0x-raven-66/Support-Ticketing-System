# Support-Ticketing-System
## Overview

The Support Ticketing System is a command-line application designed to manage and track support tickets. It allows users to create, view, update, and manage tickets and their associated history. This system is useful for managing support requests and ensuring that issues are tracked and resolved efficiently.

## Features

- **Create a New Ticket**: Allows users to create a new ticket by selecting a category and describing the issue.
- **View All Tickets**: Displays a list of all existing tickets with their status and description.
- **Update Ticket Status**: Enables users to update the status of a ticket (Open, In Progress, Closed).
- **Add a Note to a Ticket**: Allows users to add notes to a ticket's history for additional context or updates.
- **View Ticket History**: Provides a detailed history of changes and notes for a specific ticket.
- **Exit**: Terminates the application.

## Getting Started

To use the Support Ticketing System, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/0x-raven-66/Support-Ticketing-System

2. **Prepare the Categories File**
Create a file named categories.txt in the project directory. Add the categories for your tickets, each on a new line.

3. **Run the Application**
   ```python 
   python ticketing_system.py

## Usage
When you run the application, you will be presented with a menu offering the following options:

**Create a New Ticket**
Select a category from the list provided.
Enter a description of the issue.
The ticket will be created and logged.

**View All Tickets**
View a list of all tickets with their status and description.

**Update Ticket Status**
Select a ticket and choose a new status (Open, In Progress, Closed).
The status change will be logged in the ticket's history.

**Add a Note to a Ticket**
Select a ticket and enter a note.
The note will be added to the ticket's history.

**View Ticket History**
Select a ticket to view its history, including status changes and notes.

**Exit**
Exit the application.
