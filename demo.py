import tkinter as tk
import os
from utils import emails

    # This Function called when you press Send Email button
def generate_content():
    """Function to send email"""
    contents = text_input.get('1.0',tk.END).strip().split('\n')
    msg = emails.generate_email(reciever=email_input.get(),
                                subject=subject_input.get(),
                                content='<br/>'.join(contents))
    emails.send_email(msg)

    # init tkinter window root
root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=500, bg='#faebd7')
canvas.pack()
    # create frame for div in root window to place widget in it
frame = tk.Frame(root, bg='white')
frame.place(relwidth=.8, relheight=.8, relx=.1, rely=.1)

greeting = tk.Label(frame, text='EMAIL SENDER!', height=4, bg='white')
greeting.pack()

email = tk.Label(frame, text='Destination: ', height=2, bg='white')
email_input = tk.Entry(frame)
subject = tk.Label(frame, text='Subject: ', height=2, bg='white')
subject_input = tk.Entry(frame)
text = tk.Label(frame, text='Content: ', height=2, bg='white')
text_input = tk.Text(frame, width=40, height=5)
email.pack()
email_input.pack()
subject.pack()
subject_input.pack()
text.pack()
text_input.pack()

blank = tk.Label(frame, text='', height=2, bg='white')
blank.pack()
    # send email button to call generate_email function above
button = tk.Button(frame, text='SEND EMAIL', padx=50, pady=3, bg='#bed0b0', fg='black', command=generate_content)
button.pack()

root.title('Email Sender by.Assami Muzaki')
root.resizable(False, False) 
root.mainloop()