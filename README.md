Phonebook App

Version: 0.1.0
Author: Dennis Major
License: MIT

---

Overview

A simple command-line Phonebook application built in Python for practicing dictionary data structures and file I/O operations. The project focuses on reinforcing core Python concepts such as in-memory data handling and persistent storage using text files.

---

Installation

Option 1: Clone Repository

git clone <https://github.com/Major-tech/phonebook>
cd phonebook
python main.py

Option 2: Install via pip (planned structure)

pip install phonebook

---

Usage

The application runs as a menu-driven CLI:

1. Add Contact
2. Search Contact
3. Update Contact
4. Delete Contact
0. Exit

- Follow on-screen prompts
- Search results are indexed for easy selection
- Press "Enter" during updates to skip fields

---

VERSION AND FEATURES

[0.1.0] - 2026-04-27

- Add Contact
  
  - Store a contact name with up to 3 phone numbers
  - Supports partial input (1–3 numbers)
  - Prevents duplicate phone numbers across contacts

- Search Contacts
  
  - Search by name (partial or full match)
  - Search by phone number(s) (partial or full match)
  - Displays matching results in a selectable list

- Update Contact
  
  - Modify name and/or phone numbers
  - Skip fields to retain existing values
  - Prevents assigning numbers already linked to other contacts
  - Rewrites the storage file after updating 

- Delete Contact
  
  - Remove a contact permanently
  - Rewrites the storage file after deletion

- Data Persistence
  
  - Uses plain text file storage
  - Append on add, full rewrite on update/delete

---

Tech Stack

- Language: Python (3.10+ recommended, tested on 3.13)
- Dependencies: Standard Library only (no external packages)

---

Architecture Overview

This project follows a layered architecture to ensure separation of concerns and maintainability:

- Presentation Layer ("cli/")
  • Handles all user interactions, input processing, and output display.

- Application Layer ("services/")
  • Contains core business logic and orchestrates operations between layers.

- Domain Layer ("domain/")
  • Defines core rules and custom exceptions.

- Infrastructure Layer ("repository/")
  • Manages data persistence and file operations.

- Cross-Cutting Concerns ("validators/")
  • Handles validation logic reused across the application.

- Core ("core/")
  • Stores shared state and constants used throughout the app.

- Composition Root ("main.py")
  • Entry point where components are initialized and wired together.

---
  
Project Structure

phonebookproject/
├── CHANGELOG.md
├── README.md
├── pyproject.toml
│
├── src/
│   └── phonebook/
│       ├── main.py
│
│       ├── cli/
│       │   ├── dispatcher.py
│       │   ├── menu.py
│       │   ├── display.py
│       │   └── input_handlers.py
│
│       ├── services/
│       │   ├── contact_service.py
│       │   ├── auth_service.py
│       │   └── formatters.py
│
│       ├── domain/
│       │   └── exceptions.py
│
│       ├── repository/
│       │   └── contact_repository.py
│
│       ├── validators/
│       │   ├── input_validator.py
│       │   └── phone_validator.py
│
│       └── core/
│           ├── state.py
│           └── constants.py
│
└── tests/
    ├── test_input_handlers/
    ├── test_repository/
    ├── test_services/
    └── test_validators/ 

---
    
Data Handling

- Contacts are stored in a text file
- Internally managed using Python dictionaries
- Missing phone numbers are stored as "None"

---

Current Limitations

- No JSON-based persistence (planned)
- No automated tests yet (test structure in place)

---

Roadmap

- [ ] Add JSON-based storage
- [ ] Implement unit tests
- [ ] Improve input validation
- [ ] Package for full pip distribution

---

Design Notes

- Emphasis on data integrity (no duplicate phone numbers)
- Flexible search with partial matching
- Clean separation of CLI and service logic for future scalability

---

License

This project is licensed under the MIT License.

---

Author

Dennis Major
