import tkinter as tk
from tkinter import messagebox

class TokenCalculatorUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ERC20 Token Manager")
        self.root.geometry("400x450")
        
        # Internal "Blockchain" State (Store/Maintain)
        self.ledger = {"Deployer": 1000000}
        self.decimals = 18

        # --- UI ELEMENTS ---
        
        # Title
        tk.Label(root, text="Token Calculator", font=("Arial", 18, "bold")).pack(pady=10)

        # Balance Checker Section
        tk.Label(root, text="Check Account Balance:").pack()
        self.check_entry = tk.Entry(root)
        self.check_entry.pack()
        tk.Button(root, text="Check", command=self.ui_check_balance).pack(pady=5)

        tk.Label(root, text="-"*40).pack()

        # Transfer Section
        tk.Label(root, text="Transfer Tokens", font=("Arial", 12, "bold")).pack(pady=5)
        
        tk.Label(root, text="From:").pack()
        self.from_entry = tk.Entry(root)
        self.from_entry.insert(0, "Deployer")
        self.from_entry.pack()

        tk.Label(root, text="To:").pack()
        self.to_entry = tk.Entry(root)
        self.to_entry.pack()

        tk.Label(root, text="Amount:").pack()
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        tk.Button(root, text="Execute Transfer", bg="green", fg="white", 
                  command=self.ui_transfer).pack(pady=20)

    # --- LOGIC METHODS ---

    def ui_check_balance(self):
        account = self.check_entry.get()
        balance = self.ledger.get(account, 0)
        messagebox.showinfo("Balance", f"Account: {account}\nBalance: {balance} MTK")

    def ui_transfer(self):
        sender = self.from_entry.get()
        receiver = self.to_entry.get()
        try:
            # Maintain: Convert input to integer (Calculator logic)
            amount = int(self.amount_entry.get())
            
            # Logic: Ensure sender has enough balance (Require)
            if self.ledger.get(sender, 0) >= amount:
                self.ledger[sender] -= amount
                self.ledger[receiver] = self.ledger.get(receiver, 0) + amount
                messagebox.showinfo("Success", f"Transferred {amount} to {receiver}")
            else:
                messagebox.showerror("Error", "Insufficient Balance!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

# Run the Application
if __name__ == "__main__":
    root = tk.Tk()
    app = TokenCalculatorUI(root)
    root.mainloop()