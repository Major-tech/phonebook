CHANGELOG

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog and this project adheres to Semantic Versioning.

---
.
VERSIONS AND FEATURES 

[0.1.0] - 2026-04-27

Added

- Initial release of the Phonebook application
- Menu-driven CLI interface
- Add contact functionality (supports up to 3 phone numbers per contact)
- Search functionality:
  - Search by name (partial and full match)
  - Search by phone number(s) (partial and full match) 
- Update contact functionality with optional field skipping and file rewrite 
- Delete contact functionality with file rewrite
- Duplicate phone number prevention across contacts
- File-based persistence using plain text storage
- Project structure with modular separation ("cli", "services", "core","domain", "validators")
- Initial project scaffolding ("src/", "tests/", "pyproject.toml")

Notes

- Data is currently stored in a plain text file (JSON support planned)
- Test suite structure is in place but not yet implemented
