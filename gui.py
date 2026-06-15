import tkinter as tk
from tkinter import filedialog
import pandas as pd
import pywhatkit
import time

root = tk.Tk()
root.title("WhatsApp Automation Tool")
root.geometry("400x350")

# Title
label = tk.Label(root, text="WhatsApp Automation Tool", font=("Arial", 14))
label.pack(pady=10)

# Message box
msg_label = tk.Label(root, text="Enter Message:")
msg_label.pack()

msg_entry = tk.Entry(root, width=40)
msg_entry.pack(pady=5)

# store file path
file_path = ""

# FUNCTION: upload CSV
def upload_csv():
    global file_path
    file_path = filedialog.askopenfilename(
        filetypes=[("CSV Files", "*.csv")]
    )
    print("Selected file:", file_path)

# FUNCTION: send messages
def send_message():
    message = msg_entry.get()

    if file_path == "":
        print("Please upload CSV first!")
        return

    data = pd.read_csv(file_path)

    for index, row in data.iterrows():
        name = row["name"]
        number = str(row["phone"]).strip()

        if not number.startswith("+"):
            number = "+91" + number

        print("Sending to:", name)

        pywhatkit.sendwhatmsg_instantly(
            number,
            message,
            wait_time=10,
            tab_close=True
        )

        time.sleep(15)

    print("All messages sent!")

# BUTTON: upload CSV
upload_btn = tk.Button(root, text="Upload CSV File", command=upload_csv)
upload_btn.pack(pady=10)

# BUTTON: send message
send_btn = tk.Button(root, text="Send Messages", command=send_message)
send_btn.pack(pady=10)

root.mainloop()