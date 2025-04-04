import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter import ttk  # Import ttk for Progressbar
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import os
from email import encoders
from tkinter import filedialog 
from dotenv import load_dotenv
load_dotenv()

Attachments=[]  
# Function to handle email sending

def on_hover(event):
    global Attachments
    for i in Attachments:

        if i.endswith(event.widget.cget("text").replace(' ❌','')):
            Attachments.remove(i)
    print("Hovered over:", event.widget.cget("text"))  
    widget = event.widget
    confirm = messagebox.askyesno("Confirm", f"Do you want to remove '{widget.cget('text').replace(' ❌','')}'?")
    if confirm:
        event.widget.destroy()

def send_email():
    global Attachments
    print(Attachments)
    recipients = entry_recipients.get().strip()  # Get recipient emails
    subject = entry_subject.get().strip()  # Get email subject
    body = body_text.get("1.0", tk.END).strip()  # Get email body

    if not recipients or not subject or not body:
        messagebox.showwarning("Warning", "All fields are required!")
        return

    # Show Progress Bar
    progress_bar.pack(pady=20)  
    root.update_idletasks()

    progress_bar["value"] = 0
    root.update_idletasks()


    # Print details in console
    print("Recipients:", recipients)
    print("Subject:", subject)
    print("Body:", body)
    progress_bar["value"] =20 
    root.update_idletasks()
    email_send_logic(recipients.split(','),subject,body,)

 
def select_files():
    filenames = filedialog.askopenfilenames()  
    global Attachments
    if filenames:
        for i in filenames:
            if i not in Attachments:
                Attachments.append(i)
                filename=i.split('/')[-1]
                label_inside = tk.Label(fream, text=f"{filename} ❌", font=("DejaVu Serif", 12), bg="lightgray")
                label_inside.pack(side="left", padx=10, pady=5, fill="x") 
                
                label_inside.bind("<Button-1>", on_hover) 
 


def email_send_logic(recipients,subject,body):
    global Attachments
    
    GMAIL_USER = os.getenv("UserEmail")
    GMAIL_PASSWORD = os.getenv("AppPassword")
    progress_bar["value"] =30
    root.update_idletasks()

    try:
        # Connect to Gmail SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        progress_bar["value"] =40 
        root.update_idletasks()

        for recipient in recipients:
            # Create email message
            if progress_bar["value"]<90:
                progress_bar["value"] +=10 
                root.update_idletasks()


            msg = MIMEMultipart()
            msg["From"] = GMAIL_USER
            msg["To"] = recipient
            msg["Subject"] = subject

            # Attach HTML body
            msg.attach(MIMEText(body))

             # Attach files if provided
            if Attachments:
                for file_path in Attachments:
                    if os.path.exists(file_path):
                        with open(file_path, "rb") as attachment:
                            part = MIMEBase("application", "octet-stream")
                            part.set_payload(attachment.read())
                        
                        encoders.encode_base64(part)
                        part.add_header(
                            "Content-Disposition", f"attachment; filename={os.path.basename(file_path)}"
                        )
                        msg.attach(part)
                    else:
                        print(f"Warning: File {file_path} not found, skipping attachment.")

            # Send email
            server.sendmail(GMAIL_USER, recipient, msg.as_string())

        progress_bar["value"] =100 
        root.update_idletasks()

        # Hide Progress Bar after completion
        progress_bar.pack_forget()

        # Close server connection
        server.quit()

    except Exception as e:
        progress_bar.pack_forget()  
        messagebox.showerror("Error", f"Error in Sending Email Please chack your EmailId Formate.\n\n\nDetails:\n\n{e}.")
    else:
        # Show confirmation message
        messagebox.showinfo("Success", "Email Send Sucessfully.")

        entry_recipients.delete(0, tk.END)
        entry_subject.delete(0,tk.END)
        body_text.delete("1.0",tk.END)
        Attachments = []
        for widget in fream.winfo_children():
            if isinstance(widget, tk.Label):
                widget.destroy()




# Create GUI
root = tk.Tk()
root.title("Email Sender")
root.geometry("900x700")
root.configure(bg="lightblue")

# Email Label
label_email = tk.Label(root, text=f"Your Email Id : {os.getenv('UserEmail')}", bg="lightblue", font=("DejaVu Serif", 14), anchor="w")
label_email.pack(pady=20, padx=20, fill="x")

# Recipient Emails
label_recipient = tk.Label(root, text="Enter Recipient Emails (Comma-Separated):", bg="lightblue", font=("DejaVu Serif", 14), anchor="w")
label_recipient.pack(pady=10, padx=20, fill="x")

entry_recipients = tk.Entry(root, font=("DejaVu Serif", 14), width=40)
entry_recipients.pack(padx=(20, 30), fill="x")

# Email Subject
label_subject = tk.Label(root, text="Enter Email Subject:", bg="lightblue", font=("DejaVu Serif", 14), anchor="w")
label_subject.pack(pady=10, padx=20, fill="x")

entry_subject = tk.Entry(root, font=("DejaVu Serif", 14), width=40)
entry_subject.pack(padx=(20, 30), fill="x")

# Email Body
label_body = tk.Label(root, text="Enter Email Body:", bg="lightblue", font=("DejaVu Serif", 14), anchor="w")
label_body.pack(pady=10, padx=20, fill="x")

body_text = scrolledtext.ScrolledText(root, height=10, width=50, font=("DejaVu Serif", 14), wrap=tk.WORD)
body_text.pack(padx=(20, 30), fill="x")



# File Attachment Section (Entry + Button in One Line)

# File Attachment Section (Entry + Button in One Line)
fream = tk.Frame(root, bg="white", relief="solid")
fream.pack(pady=10, padx=(20,65),fill="x")


tk.Button(fream, text="Select Files", font=("DejaVu Serif", 10), command=select_files).pack(side="right")




# Progress Bar (Initially Hidden)
progress_bar = ttk.Progressbar(root, length=400, mode="determinate")
progress_bar.pack_forget()  # Hide initially


# Send Button (linked to send_email function)
tk.Button(root, text="Send Email", font=("DejaVu Serif", 10), command=send_email).pack(pady=20)

# Run GUI
root.mainloop()