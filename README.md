# Sugar Mountain Ski Data Entry Automation

## 📌 Overview

This project automates the process of transferring structured employee/customer data from an Excel file into the Sugar Mountain Ski Data entry system.

The script reads data from an Excel spreadsheet stored locally (OneDrive) and uses UI automation to input the data directly into the Ski Data system. This reduces manual entry time, improves accuracy, and streamlines repetitive administrative workflows.

---

## ⚙️ Features

* Reads structured data directly from Excel (`.xlsx`)
* Automates form entry into Ski Data system
* Handles multiple input fields (name, DOB, group information)
* Automates dropdown selection and confirmation dialogs
* Processes multiple rows in a dataset sequentially
* Includes fail-safe protection for mouse control

---

## 🧠 Technologies Used

* Python 3
* pandas (Excel data handling)
* openpyxl (Excel file reading)
* pyautogui (keyboard & mouse automation)
* os (file path handling)
* time (execution control)

---

## 📊 How It Works

1. Loads an Excel file from the user’s local OneDrive directory
2. Assigns column labels: First Name, Last Name, DOB, Group Name
3. Iterates through each row of the dataset
4. Uses screen coordinates to interact with the Ski Data system interface
5. Inputs data into each required field using automated keyboard actions
6. Handles dropdown selections and confirmation prompts
7. Repeats the process until all rows are completed

---

## ⚠️ Important Notes

* Screen coordinates must be calibrated for the specific monitor and resolution
* The application window must remain in a fixed position during execution
* `pyautogui.FAILSAFE = True` is enabled (move mouse to top-left corner to stop script immediately)
* Do not interact with keyboard/mouse while the script is running

---

## 📁 Project Structure

```
Sugar-Mountain-Ski-Data-Automation/
│
├── main.py              # Main automation script
├── Sample.xlsx         # Input data file
└── README.md           # Project documentation
```

---

## 💡 Impact

This tool demonstrates practical automation of real-world administrative workflows by:

* Eliminating repetitive manual data entry
* Reducing human error in operational systems
* Increasing efficiency of data processing tasks
* Applying Python automation to a real business environment

---

## 🚀 Future Improvements

* Replace coordinate-based automation with Selenium or API integration (if available)
* Add logging system for tracking processed rows
* Add error recovery for failed inputs
* Build a GUI for non-technical users
* Package into a standalone executable

---

## 👨‍💻 Author

**Robert Richter**
Mathematics & Actuarial Science
Appalachian State University

GitHub: https://github.com/richterrw

