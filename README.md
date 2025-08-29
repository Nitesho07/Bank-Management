# 🏦 Bank Management System  

## 📘 About The Project

This project is a straightforward, terminal-based Bank Management System developed entirely in Python. It was built to apply and demonstrate a solid understanding of **Object-Oriented Programming (OOP)** principles and Python fundamentals.

The system utilizes a simple **JSON file for data persistence**, showcasing practical skills in file I/O and data management within an application. The main goal was to build a functional and clear command-line application that simulates core banking operations, effectively demonstrating proficiency with concepts like **classes, objects, and methods** in a practical scenario.  

---

## ✨ Features  

- **Create New Account:** Securely create a new bank account with essential user details and a unique, auto-generated account number.
      
    <img width="847" height="869" alt="image" src="https://github.com/user-attachments/assets/6ba24461-5834-4e76-8f3e-635edc366057" />

- **Deposit Funds:** Easily deposit money into an existing account, with the new balance instantly saved.
      
    <img width="753" height="610" alt="image" src="https://github.com/user-attachments/assets/f105ef9f-39e2-4706-bfaf-205fdeb779b7" />

- **Withdraw Funds:** Safely withdraw money from an account, with built-in checks to prevent insufficient balance.
      
    <img width="650" height="654" alt="image" src="https://github.com/user-attachments/assets/a4992896-47f0-4479-b0f2-392df7cf45db" />
 
- **View Account Details:** Display all information associated with a specific account, such as name, email, balance, and account number.
      
    <img width="660" height="735" alt="image" src="https://github.com/user-attachments/assets/3af86a73-170b-40be-a3c9-ad85d5df91e5" />

- **Update Information:** Modify account details, including the user's name, email, or PIN, after successful verification.
      
    <img width="789" height="706" alt="image" src="https://github.com/user-attachments/assets/8b92aefd-9e21-4bd9-b54a-fda9337d61c9" />

- **Delete Account:** Permanently and securely remove a bank account and all its associated data from the system.
      
    <img width="812" height="683" alt="image" src="https://github.com/user-attachments/assets/57b5ddc9-e79d-4477-b9e4-5486246269b4" />

---

## ⚙️ Installation  

Follow these steps to set up the project locally:  

```bash
# 1. Clone the repository
git clone https://github.com/your-username/bank-management-system.git

# 2. Navigate to the project directory
cd bank-management-system

# 3. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

# 4. Install dependencies (none external, just ensure Python 3.8+)
pip install -r requirements.txt
```

---

## 🚀 Usage  

Run the program from the terminal:  

```bash
python bank_app.py
```

You will see a menu like this:  

```text
Press 1 for Creating an account
Press 2 for Depositing the money in the bank
Press 3 for Withdrawing the money
Press 4 for Details
Press 5 for Updating the details
Press 6 for Deleting your account
Press 0 to exit
```

👉 Enter the number corresponding to the operation you want, and follow the prompts.  

---

## 📜 Note  

This project was built for **learning purposes only** and is not intended for real-world banking use.  
All data is stored locally in a JSON file (`data.json`).  
Unauthorized use, modification, or redistribution is not permitted.
