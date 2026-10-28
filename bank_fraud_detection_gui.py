import tkinter as tk
from tkinter import ttk, messagebox

# Data storage for history
history_data = []

def check_transaction():
    customer = name_entry.get().strip()
    account = account_entry.get().strip()
    amount_text = amount_entry.get().strip()
    count_text = count_entry.get().strip()
    international = location_choice.get()

    # Input Validation
    if not customer or not account:
        messagebox.showerror("Error", "Please fill in Customer Name and Account Number.")
        return

    try:
        amount = float(amount_text)
        count = int(count_text)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number and Count must be a whole number.")
        return

    if amount <= 0 or count < 0:
        messagebox.showerror("Error", "Amount must be greater than zero and Count cannot be negative.")
        return

    # Rule-Based Fraud Detection Logic
    risk_score = 0
    reasons = []

    if amount >= 50000:
        risk_score += 2
        reasons.append("High Amount (>= Rs. 50,000)")

    if international == "Yes":
        risk_score += 2
        reasons.append("International Transaction")

    if count >= 10:
        risk_score += 2
        reasons.append("Frequent Transactions (>= 10 today)")

    # Status Determination
    if risk_score >= 4:
        status = "HIGH RISK"
        result_label.config(text=f"Result: HIGH RISK (Score: {risk_score})", fg="red")
    elif risk_score >= 2:
        status = "MEDIUM RISK"
        result_label.config(text=f"Result: MEDIUM RISK (Score: {risk_score})", fg="orange")
    else:
        status = "LOW RISK"
        result_label.config(text=f"Result: LOW RISK (Score: {risk_score})", fg="green")

    reason_text = ", ".join(reasons) if reasons else "No risk rules triggered"
    reason_label.config(text="Reason: " + reason_text)

    # Insert into Treeview Table
    table.insert("", "end", values=(customer, account, f"Rs. {amount:.2f}", international, count, risk_score, status))

def clear_fields():
    name_entry.delete(0, tk.END)
    account_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    count_entry.delete(0, tk.END)
    count_entry.insert(0, "1")
    location_choice.set("No")
    result_label.config(text="Result: Waiting for input...", fg="black")
    reason_label.config(text="Reason: None")

def exit_app():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()

# Main Window Setup
root = tk.Tk()
root.title("Bank Fraud Detection System")
root.geometry("750x600")
root.minsize(700, 550)

# Header Label
tk.Label(
    root, 
    text="Bank Fraud Detection System", 
    font=("Arial", 16, "bold"), 
    bg="#17365D", 
    fg="white", 
    pady=10
).pack(fill="x")

# Transaction Details Form Frame
form_frame = tk.LabelFrame(root, text="Transaction Details", padx=10, pady=10)
form_frame.pack(padx=15, pady=10, fill="x")

tk.Label(form_frame, text="Customer Name:").grid(row=0, column=0, sticky="w", pady=5)
name_entry = tk.Entry(form_frame, width=20)
name_entry.grid(row=0, column=1, pady=5)

tk.Label(form_frame, text="Account Number:").grid(row=0, column=2, sticky="w", pady=5, padx=(10, 0))
account_entry = tk.Entry(form_frame, width=20)
account_entry.grid(row=0, column=3, pady=5)

tk.Label(form_frame, text="Amount (Rs.):").grid(row=1, column=0, sticky="w", pady=5)
amount_entry = tk.Entry(form_frame, width=20)
amount_entry.grid(row=1, column=1, pady=5)

tk.Label(form_frame, text="Transactions Today:").grid(row=1, column=2, sticky="w", pady=5, padx=(10, 0))
count_entry = tk.Entry(form_frame, width=20)
count_entry.insert(0, "1")
count_entry.grid(row=1, column=3, pady=5)

tk.Label(form_frame, text="International:").grid(row=2, column=0, sticky="w", pady=5)
location_choice = ttk.Combobox(form_frame, values=["No", "Yes"], state="readonly", width=17)
location_choice.set("No")
location_choice.grid(row=2, column=1, pady=5)

# Action Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

tk.Button(
    btn_frame, 
    text="Check Transaction", 
    command=check_transaction, 
    bg="#17365D", 
    fg="white", 
    padx=10
).pack(side="left", padx=5)

tk.Button(
    btn_frame, 
    text="Clear Form", 
    command=clear_fields, 
    padx=10
).pack(side="left", padx=5)

tk.Button(
    btn_frame, 
    text="Exit", 
    command=exit_app, 
    padx=10
).pack(side="left", padx=5)

# Detection Output Frame
result_frame = tk.LabelFrame(root, text="Detection Output", padx=10, pady=5)
result_frame.pack(padx=15, pady=5, fill="x")

result_label = tk.Label(result_frame, text="Result: Waiting for input...", font=("Arial", 11, "bold"))
result_label.pack(anchor="w")

reason_label = tk.Label(result_frame, text="Reason: None", font=("Arial", 10))
reason_label.pack(anchor="w")

# Transaction History Table Frame
table_frame = tk.LabelFrame(root, text="Transaction History", padx=10, pady=5)
table_frame.pack(padx=15, pady=10, fill="both", expand=True)

cols = ("Customer", "Account", "Amount", "International", "Count", "Score", "Status")
table = ttk.Treeview(table_frame, columns=cols, show="headings", height=5)

for col in cols:
    table.heading(col, text=col)
    table.column(col, width=95, anchor="center")

scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
table.configure(yscrollcommand=scrollbar.set)

table.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Execute Application Window
root.mainloop()