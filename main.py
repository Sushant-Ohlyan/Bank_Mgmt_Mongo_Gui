
from tkinter import *
from tkinter import messagebox
from account_manager import add_account, list_accounts, update_account, delete_account
from mongo_conn_util import close_connection
root = Tk()
root.title("Bank Management App")
root.geometry("600x400")


def list_accounts_gui():
    accounts = list_accounts()
    accounts_list.delete(0, END)
    for account in accounts:
        accounts_list.insert(END, f"ID: {account['_id']} | Name: {account['name']} | Balance: ${account['balance']}")


def add_account_gui():
    name = entry_name.get()
    balance = entry_balance.get()
    if name and balance:
        add_account(name, balance)
        entry_name.delete(0, END)
        entry_balance.delete(0, END)
        list_accounts_gui()
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")


def update_account_gui():
    account_id = entry_id.get()
    name = entry_name.get()
    balance = entry_balance.get()
    if account_id and name and balance:
        update_account(account_id, name, balance)
        entry_id.delete(0, END)
        entry_name.delete(0, END)
        entry_balance.delete(0, END)
        list_accounts_gui()
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")


def delete_account_gui():
    account_id = entry_id.get()
    if account_id:
        delete_account(account_id)
        entry_id.delete(0, END)
        list_accounts_gui()
    else:
        messagebox.showwarning("Input Error", "Please enter an account ID.")


# GUI components
frame = Frame(root)
frame.pack(pady=20)

label_id = Label(frame, text="Account ID:")
label_id.grid(row=0, column=0, padx=5, pady=5)
entry_id = Entry(frame, width=50)  # Increase the width
entry_id.grid(row=0, column=1, padx=5, pady=5)

label_name = Label(frame, text="Account Holder's Name:")
label_name.grid(row=1, column=0, padx=5, pady=5)
entry_name = Entry(frame, width=50)  # Increase the width
entry_name.grid(row=1, column=1, padx=5, pady=5)

label_balance = Label(frame, text="Balance:")
label_balance.grid(row=2, column=0, padx=5, pady=5)
entry_balance = Entry(frame, width=50)  # Increase the width
entry_balance.grid(row=2, column=1, padx=5, pady=5)

button_add = Button(frame, text="Add Account", command=add_account_gui)
button_add.grid(row=3, column=0, padx=5, pady=5)

button_update = Button(frame, text="Update Account", command=update_account_gui)
button_update.grid(row=3, column=1, padx=5, pady=5)

button_delete = Button(frame, text="Delete Account", command=delete_account_gui)
button_delete.grid(row=4, column=0, padx=5, pady=5)

button_list = Button(frame, text="List All Accounts", command=list_accounts_gui)
button_list.grid(row=4, column=1, padx=5, pady=5)

accounts_list = Listbox(root, width=80)
accounts_list.pack(pady=20)


list_accounts_gui()

root.mainloop()


close_connection()
