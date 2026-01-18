# Password Generator Tool  
### SDLC Project Documentation

## NAME: AKINS-AKINDUNNI YOYINSOLA LILLY 
## MATRIC NO: 24/15016
## DEPARTMENT: COMPUTER SCIENCE 
## COURSE CODE: SEN 201 
## LEVEL: 200

##  Project Overview
This project is a **Python-based Password Generator Tool** developed as part of a Software Development Life Cycle (SDLC) assignment.  
The application generates strong, secure passwords based on user-defined length while ensuring all essential character categories are included.

The project demonstrates the complete SDLC process—from requirement analysis to maintenance—and is version-controlled and hosted on GitHub.

---

##  Project Objectives
- Apply SDLC principles to a real-world mini project
- Design and implement a functional Python application
- Generate secure passwords using standard security practices
- Document the system clearly using a README file
- Push and manage the project using GitHub

---

##  Technologies Used
- **Programming Language:** Python  
- **Libraries:** `random`, `string`  
- **Version Control:** Git & GitHub  

---

##  Requirement Analysis

### Functional Requirements
- User must be able to input a password length.
- The system must generate a password that includes:
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one digit
  - At least one special character
- The system must display the generated password.

### Non-Functional Requirements
- Simple and user-friendly command-line interface.
- Random and reliable password generation.
- Clean, readable, and modular code.

---

##  System Design

### Architecture
The system is implemented as a simple modular Python script:
- **generate_password()** – Handles password creation logic
- **main()** – Handles user input and output

### Design Decisions
- Used Python’s `string` module for character sets.
- Used `random` module for randomness.
- Ensured all character categories appear at least once.
- Shuffled characters to eliminate predictable patterns.

### System Flow
1. User enters password length  
2. Input is validated  
3. Password characters are generated  
4. Characters are shuffled  
5. Final password is displayed  

---

##  Implementation

The program is implemented in `password_generator.py`.

Key implementation details:
- Imported `random` and `string`
- Defined character groups (uppercase, lowercase, digits, special)
- Selected at least one character from each group
- Filled remaining characters randomly
- Used `random.shuffle()` for security
- Returned final password as a string

---

##  Testing

### Manual Test Cases

| Test Case | Input | Expected Result | Status |
|----------|-------|----------------|--------|
| Valid length | 10 | 10-character password | Pass |
| Minimum length | 4 | 4-character password | Pass |
| Invalid length | 2 | Error message | Pass |
| Invalid input | "hello" | Error message | Pass |

### Test Validation
Generated passwords were confirmed to include:
- Uppercase letters 
- Lowercase letters   
- Digits   
- Special characters   

---

##  Deployment
The project is deployed via GitHub:
- Source code is pushed to a public repository
- Users can clone and run the project locally using:
```bash

MY REPO LINK: https://github.com/wh0sthatlilly/password-generator
python password_generator.py
