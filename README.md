# 🏨 Hotel Booking CLI System

A simple Python-based **Hotel Booking System** that runs in the terminal.
The program allows users to **view rooms, search rooms using natural language, and book available rooms** for a selected number of nights.

This project demonstrates:

* JSON file handling
* Command-line interaction
* Input validation
* Room filtering and booking logic
* Natural language style room search

---

## ✨ Features

### 1. View Rooms

Displays all rooms with details such as:

* Room number
* Room type
* Price
* Availability

### ### 2. Smart Room Search

One of the most important features of this project is the **search system**.

Instead of selecting rigid menu options, users can type **simple human-like queries**, and the program extracts the useful filters automatically.

Example searches:

* show all deluxe rooms
* show all available deluxe rooms
* show all deluxe rooms under 5000
* show standard rooms under 3000
* show all available rooms




The program automatically detects:

* Room type (Deluxe / Standard)
* Availability
* Price limit

---

## 🧠 Search Feature Highlight

Example user input:

Search: show all available deluxe rooms under 5000

The program parses the text and extracts:

* "available"
* "deluxe"
* "under 5000"

It then filters the rooms based on those conditions and displays matching results.

---

## 📁 Project Structure

hotel-booking-project/
│
├── main.py
├── rooms.json
└── README.md

---

## 📄 Sample rooms.json

{
"rooms": [
{
"room_no": 101,
"type": "Deluxe",
"price": 4500,
"occupied": false
},
{
"room_no": 102,
"type": "Standard",
"price": 2500,
"occupied": true
}
]
}

---

## 💻 Example Usage

### View Rooms

1 room
101 - Deluxe
price - 4500

2 room
102 - Standard
price - 2500

---

### Search Rooms

User input:

Search: show all available deluxe rooms under 5000

Possible output:

Room No: 101
Type: Deluxe
Price: 4500
Available: Yes

---

### Booking a Room

Guest Name: Rahul
Enter the Nights: 3

Your total will be 13500 for 3 nights.
Room booked successfully.

---

## ⚙️ How to Run

Clone the repository:

git clone https://github.com/yourusername/hotel-booking-project.git

Navigate into the folder:

cd hotel-booking-project

Run the program:

python main.py

---

## 🛠 Technologies Used

Python
JSON
Command Line Interface (CLI)

---

## 🎯 Learning Outcomes

This project helped practice:

* File handling with JSON
* Data filtering and searching
* Building interactive CLI applications
* Basic booking logic
* Input validation
* Parsing simple natural language queries

---

## 🚀 Future Improvements

Possible improvements:

* Add check-out functionality
* Store booking history
* Improve search parsing with regular expressions
* Add a GUI using Tkinter or Streamlit
* Use a database like SQLite instead of JSON

---

## 👨‍💻 Author

Sahil Sah
