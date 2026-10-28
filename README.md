# 🏦 Bank Fraud Detection System (Python Tkinter)

A beginner-friendly, rule-based desktop application for evaluating financial transaction risk levels in real time. Built strictly with standard Python libraries (`tkinter`), requiring zero external dependencies.

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![GUI](https://img.shields.io/badge/GUI-Tkinter-orange.svg)

---

##✨ Key Features
- **Real-Time Fraud Scoring:** Calculates risk scores instantly using deterministic rules.
- **Visual Risk Classification:**
  - 🟢 **LOW RISK (Score 0-1):** Normal operational transfers.
  - 🟠 **MEDIUM RISK (Score 2-3):** Flagged for manual verification.
  - 🔴 **HIGH RISK (Score 4+):** Severe multi-factor risk detection.
- **Interactive Session Ledger:** Appends checked transactions into a dynamic `ttk.Treeview` table.
- **Robust Input Validation:** Built-in error handling for missing fields and non-numeric inputs via `messagebox` pop-ups.
- **Zero Third-Party Dependencies:** Runs natively on any computer with standard Python installed.

---

## 📐 Rule-Based Risk Matrix

| Risk Rule | Condition | Score Weight |
| :--- | :--- | :--- |
| **High Transaction Amount** | Amount $\ge$ Rs. 50,000 | **+2 Points** |
| **Cross-Border Transfer** | International = "Yes" | **+2 Points** |
| **High Daily Frequency** | Transactions Today $\ge$ 10 | **+2 Points** |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher installed on your system.

### Installation & Execution
1. Clone this repository:
   ```bash
   git clone https://github.com/sushmita/bank-fraud-detection-gui.git
   cd bank-fraud-detection-gui
   ```

2. Run the application:
   ```bash
   python bank_fraud_detection_gui.py
   ```

---

## 📁 Project Structure
```text
bank-fraud-detection-gui/
├── bank_fraud_detection_gui.py   # Main Python desktop script
├── README.md                      # Project documentation
└── report/                        # Mini project report documents
```

---

## 🧪 Test Scenarios for Demonstration

Try these inputs in the application to demonstrate all risk categories:

1. **Low Risk Test:**
   - *Customer:* Ananya Sharma | *Account:* 10982345 | *Amount:* 4500 | *Intl:* No | *Count:* 2  
   - **Result:** `LOW RISK` (Score: 0)

2. **Medium Risk Test:**
   - *Customer:* Rajesh Kumar | *Account:* 45982103 | *Amount:* 75000 | *Intl:* No | *Count:* 3  
   - **Result:** `MEDIUM RISK` (Score: 2)

3. **High Risk Test:**
   - *Customer:* Vikram Singh | *Account:* 33021948 | *Amount:* 120000 | *Intl:* Yes | *Count:* 12  
   - **Result:** `HIGH RISK` (Score: 6)

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📜 License
This project is open-source under the [MIT License](LICENSE).
