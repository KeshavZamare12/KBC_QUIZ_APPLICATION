# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 11:22:49 2023

@author: Admin
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 08:45:10 2023

@author: Admin
"""

import tkinter as tk
import random
import sys
import time
from db_conn import conn_db,update_money
nm=[]
# List of questions with their options and correct answers
questions = [
    {
        'question': ' Who is the father of Computers?',
        'options': [" a)James Gosling",
        "b) Charles Babbage",
        "c) Dennis Ritchie",
        "d) Bjarne Stroustrup"],
        'answer': 1
    },
    {'question':'What is a relation in RDBMS?',
     'options': ['Key',
                 'Table',
                 'Row',
                 'Data Types'],
     'answer':2
        
    },
    {
        'question': ' What is the full form of CPU?',
        'options': ['a) Computer Processing Unit',
                    'b) Computer Principle Unit',
                    'c) Central Processing Unit',
                    'd) Control Processing Unit'],
        'answer': 2
    },
    {'question':" Which of the following language does the computer understand?",
     'options':['a) Computer understands only C Language',
        'b) Computer understands only Assembly Language',
        'c) Computer understands only Binary Language',
        'd) Computer understands only BASIC'],
     'answer':2
     },
    
{
'question': 'A data structure in which linear sequence is maintained by pointers is known as',
'options':[ ' Array', ' Stack', ' Linked list', ' Pointer-based data structure'],
'answer': 2
},
{
'question': ' Which of the following data structure works on the principle of First Come First Serve? '
,
'options': [' Priority queue', ' Heap', ' Stack', 'Queue'], 'answer': 3
},
{
'question': ' A ____ is a linear collection of self-referential structures, called nodes, connected by pointer links. ',
'options': [' Queue', ' Linked list', ' Tree', ' Stack'], 'answer': 1
},
{
'question': ' A queue where all elements have equal priority is a',
'options': [' ILFO data structure', ' LILO data structure', ' FIFO data structure', ' LIFO data structure'],
'answer': 2}
,
{
'question': ' A file that is only read by a program is known as ____',
'options':[ ' Input file', ' Temporary file', ' Work file', ' Input/output file'],
'answer': 0}

]

# Global variables
current_question = 0
money_won = 0
double_dip_used = False
fifty_fifty_used = False
audience_poll_used = False
flip_question_used = False

# Create the main window
window = tk.Tk()
window.title('KBC Game')
window.config(bg='pink')

def submit():
    name = name_entry.get()
    email = email_entry.get()
    college = college_entry.get()
    phoneno = phoneno_entry.get()
    if name.isalpha():
        if ("@"and "." in list(email) ) and (" " not in list(email)):
            
            if(not college.isdigit())and(" " in list(college)):
                if(phoneno.isdigit()) and(len(phoneno)==10):
                    conn_db(name,email,college,phoneno)
                    tk.messagebox.showinfo('congratulations','Your information Saved Sucessfully\nWELCOME TO KBC GAME')
                    frame.destroy()
                    show_game_frame()
                else:
                    tk.messagebox.showerror('Error', 'Please enter valid phoneno!')
            else:
                tk.messagebox.showerror('Error', 'Please enter valid college name!')
        else:
            tk.messagebox.showerror('Error', 'Please enter valid email address!')
                    
    else:
        tk.messagebox.showerror('Error', 'Please enter valid name!')



# Function to display the game frame
def show_game_frame():
    global current_question, money_won
    
    game_frame.pack()
    
    if current_question < len(questions):
        question_label.config(text=questions[current_question]['question'])
        money_label.config(text=f'Current Money:₹{money_won}',font='Algerian 15')
        options = questions[current_question]['options']
        for i in range(len(options)):
            option_buttons[i].config(text=options[i],state="normal",padx=len(options[i])+30)
    else:
        tk.messagebox.showinfo('Congratulations!', f'You have won ₹{money_won}!')
        time.sleep(5)
        window.destroy()
    
        

# Function to check the answer and move to the next question
def show_lifeline():
    if double_dip_used:
        double_dip_button.config(state="disabled")
    else:
        double_dip_button.config(state="normal")

    # Fifty-Fifty button state
    if fifty_fifty_used:
        fifty_fifty_button.config(state="disabled")
    else:
        fifty_fifty_button.config(state="normal")

    # Flip button state
    if flip_question_used:
        flip_question_button.config(state="disabled")
    else:
        flip_question_button.config(state="normal")
def check_answer(answer):
    global current_question, money_won
    if current_question>len(questions):
        clear_frame()   
    elif answer == questions[current_question]['answer']:
        money_won += 1000
        update_money(money_won)
        tk.messagebox.showinfo('Correct', 'Congratulations, your answer is correct!')
        current_question += 1
        show_lifeline()
        show_game_frame()
    else:
        tk.messagebox.showerror('Incorrect', 'Oops, your answer is incorrect! Game over.')
        window.destroy()
        clear_frame()

# Function to handle the Double Dip functionality
def double_dip():
    global double_dip_used
    if not double_dip_used:
        double_dip_used = True
        correct_answer = questions[current_question]['answer']
        options = [0, 1, 2, 3]
        options.remove(correct_answer)
        random.shuffle(options)
        options.remove(options[0])
        for option in options:
            option_buttons[option].config(state=tk.DISABLED)

# Function to handle the Fifty-Fifty functionality
def fifty_fifty():
    global fifty_fifty_used
    if not fifty_fifty_used:
        fifty_fifty_used = True
        correct_answer = questions[current_question]['answer']
        options = [0, 1, 2, 3]
        options.remove(correct_answer)
        random.shuffle(options)
        options = options[:2]
        for option in options:
            option_buttons[option].config(state=tk.DISABLED)

# Function to handle the Audience Poll functionality
def audience_poll():
    global audience_poll_used
    if not audience_poll_used:
        audience_poll_used = True
        correct_answer = questions[current_question]['answer']
        options = [0, 1, 2, 3]
        options.remove(correct_answer)
        random.shuffle(options)
        percentage = random.randint(40, 100)
        audience_result = f'Option {correct_answer + 1}: {percentage}%\n'
        for option in options:
            percentage = random.randint(0, 60)
            audience_result += f'Option {option + 1}: {percentage}%\n'
        tk.messagebox.showinfo('Audience Poll', 'Audience Poll Result:\n\n' + audience_result)

# Function to handle the Flip Question functionality
def flip_question():
    global flip_question_used
    if not flip_question_used:
        flip_question_used = True
        tk.messagebox.showinfo('Flip Question', 'The question has been flipped! A new question will be displayed.')
        next_question()
def clear_frame():
	for widget in game_frame.winfo_children():
		widget.destroy()
# Function to move to the next question
def next_question():
    global current_question
    current_question += 1
    show_game_frame()
tk.Label(window, text="Quiz App",
      font="calibre 40 bold",
       background="cyan",
      padx=10, pady=9).pack()
# Create a frame to hold the input fields
frame = tk.Frame(window)
frame.pack(pady=20)

# Create labels and entry fields for name, email, college, and date of birth
name_label = tk.Label(frame, text="Name:",font="calibre 17 bold")
name_label.grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(frame,bg='orange',fg='blue',font="calibre 17 bold")
name_entry.grid(row=0, column=1)

email_label = tk.Label(frame, text="Email:",font="calibre 17 bold")
email_label.grid(row=1, column=0, sticky="w")
email_entry = tk.Entry(frame,bg='orange',fg='blue',font="calibre 17 bold")
email_entry.grid(row=1, column=1)

college_label = tk.Label(frame, text="College:",font="calibre 17 bold")
college_label.grid(row=2, column=0, sticky="w")
college_entry = tk.Entry(frame,bg='orange',fg='blue',font="calibre 17 bold")
college_entry.grid(row=2, column=1)

phoneno_label = tk.Label(frame, text="Mobile no:",font="calibre 17 bold")
phoneno_label.grid(row=3, column=0, sticky="w")
phoneno_entry = tk.Entry(frame,bg='orange',fg='blue',font="calibre 17 bold")
phoneno_entry.grid(row=3, column=1)

# Create a button to submit the form
submit_button = tk.Button(frame, text="Submit", command=submit)
submit_button.grid(row=4,column=1)

# Create the game frame
game_frame = tk.Frame(window,bg='pink')
#show name

#showing question
question_label = tk.Label(game_frame, text='',font="calibre 17 bold")
question_label.pack(pady=10)
option_buttons = []
for i in range(4):
    option_button = tk.Button(game_frame, text='', width=30, command=lambda i=i: check_answer(i),font="calibre 17 bold")
    option_button.pack(pady=5)
    option_buttons.append(option_button)
money_label = tk.Label(game_frame, text='')
money_label.pack(pady=10)
double_dip_button = tk.Button(game_frame, text='Double Dip', command=double_dip,fg='red',bg='white',font="calibre 17 bold")
double_dip_button.pack(side=tk.LEFT, padx=5)
fifty_fifty_button = tk.Button(game_frame, text='Fifty-Fifty', command=fifty_fifty,fg='red',bg='white',font="calibre 17 bold")
fifty_fifty_button.pack(side=tk.LEFT, padx=5)
audience_poll_button = tk.Button(game_frame, text='Audience Poll', command=audience_poll,fg='red',bg='white',font="calibre 17 bold")
audience_poll_button.pack(side=tk.LEFT, padx=5)
flip_question_button = tk.Button(game_frame, text='Flip Question', command=flip_question,fg='red',bg='white',font="calibre 17 bold")
flip_question_button.pack(side=tk.LEFT, padx=5)


# Start the GUI main loop
window.mainloop()
