import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import database  # Ensure this module contains the required functions

app = customtkinter.CTk()
app.title('Apartment Rental Application System')
app.geometry('1360x645')
app.config(bg='#161C25')
app.resizable(False, False)

font1 = ('Arial', 21, 'bold')
font2 = ('Arial', 13, 'bold')


def add_to_treeview():
    applicants = database.fetch_applicants()
    tree.delete(*tree.get_children())
    for applicant in applicants:
        tree.insert('', END, values=applicant)


def clear(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
        tree.focus('')
    entry_number_entry.delete(0, END)
    name_entry.delete(0, END)
    variable1.set('Male')
    date_of_birth_entry.delete(0, END)
    contact_info_entry.delete(0, END)
    occupants_entry.delete(0, END)
    job_entry.delete(0, END)
    variable2.set('Incomplete')


def display_data(event):
    selected_item = tree.focus()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear()
        entry_number_entry.insert(0, row[0])
        name_entry.insert(0, row[1])
        variable1.set(row[2])
        date_of_birth_entry.insert(0, row[3])
        contact_info_entry.insert(0, row[4])
        occupants_entry.insert(0, row[5])
        job_entry.insert(0, row[6])
        variable2.set(row[7])
    else:
        pass


def delete():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error Detected', 'Choose an applicant to remove.')
    else:
        entry_number = entry_number_entry.get()
        database.delete_applicant(entry_number)
        add_to_treeview()
        clear()
        messagebox.showinfo('Done, Target Eliminated', f'Target number {entry_number} has been deleted.')


def update():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error Detected', 'Choose data to update.')
    else:
        entry_number = entry_number_entry.get()
        name = name_entry.get()
        gender = variable1.get()
        date_of_birth = date_of_birth_entry.get()
        contact_info = contact_info_entry.get()
        occupants = occupants_entry.get()
        job = job_entry.get()
        requirements = variable2.get()
        if not (entry_number and name and gender and date_of_birth and contact_info and occupants and job and requirements):
            messagebox.showerror('Error', 'Enter all data.')
        else:
            database.update_applicant(name, gender, date_of_birth, contact_info, job, occupants, requirements, entry_number)
            add_to_treeview()
            clear()
            messagebox.showinfo('Completed your request', 'Data has been updated')


def insert():
    entry_number = entry_number_entry.get()
    name = name_entry.get()
    gender = variable1.get()
    date_of_birth = date_of_birth_entry.get()
    contact_info = contact_info_entry.get()
    occupants = occupants_entry.get()
    job = job_entry.get()
    requirements = variable2.get()
    if not (entry_number and name and gender and date_of_birth and contact_info and occupants and job and requirements):
        messagebox.showerror('Error', 'Enter all data.')
    elif database.entry_number_exists(entry_number):
        messagebox.showerror('Error', 'Entry number already exists')
    else:
        database.insert_applicant(entry_number, name, gender, date_of_birth, contact_info, occupants, job, requirements)
        add_to_treeview()
        clear()
        messagebox.showinfo('Thank You!', 'Your application has been recorded and will be considered')


entry_number_label = customtkinter.CTkLabel(app, font=font1, text='Entry Number:', text_color='#fff', bg_color='#161C25')
entry_number_label.place(x=20, y=20)

entry_number_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
entry_number_entry.place(x=180, y=20)

name_label = customtkinter.CTkLabel(app, font=font1, text='Name:', text_color='#fff', bg_color='#161C25')
name_label.place(x=20, y=73)

name_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
name_entry.place(x=180, y=73)

gender_label = customtkinter.CTkLabel(app, font=font1, text='Gender:', text_color='#fff', bg_color='#161C25')
gender_label.place(x=20, y=126)

options = ['Male', 'Female', 'Other']
variable1 = StringVar()

gender_option = customtkinter.CTkComboBox(app, font=font1, text_color='#000', fg_color='#fff', dropdown_hover_color='#0C9295', button_color='#0C9295', button_hover_color='#0C9295', border_color='#0C9295', width=180, variable=variable1, values=options, state='readonly')
gender_option.set('Male')
gender_option.place(x=180, y=126)

date_of_birth_label = customtkinter.CTkLabel(app, font=font1, text='Birthday:', text_color='#fff', bg_color='#161C25')
date_of_birth_label.place(x=20, y=179)

date_of_birth_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
date_of_birth_entry.place(x=180, y=179)

contact_info_label = customtkinter.CTkLabel(app, font=font1, text='Contact Info:', text_color='#fff', bg_color='#161C25')
contact_info_label.place(x=20, y=232)

contact_info_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
contact_info_entry.place(x=180, y=232)

job_label = customtkinter.CTkLabel(app, font=font1, text='Job:', text_color='#fff', bg_color='#161C25')
job_label.place(x=20, y=285)

job_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
job_entry.place(x=180, y=285)

occupants_label = customtkinter.CTkLabel(app, font=font1, text='Occupant Amt.:', text_color='#fff', bg_color='#161C25')
occupants_label.place(x=20, y=338)

occupants_entry = customtkinter.CTkEntry(app, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
occupants_entry.place(x=180, y=338)

requirements_label = customtkinter.CTkLabel(app, font=font1, text='Requirements:', text_color='#fff', bg_color='#161C25')
requirements_label.place(x=20, y=391)

choices = ['Incomplete', 'Done', 'Late']
variable2 = StringVar()

requirements_choices = customtkinter.CTkComboBox(app, font=font1, text_color='#000', fg_color='#fff', dropdown_hover_color='#0C9295', button_color='#0C9295', button_hover_color='#0C9295', border_color='#0C9295', width=180, variable=variable2, values=choices, state='readonly')
requirements_choices.set('Incomplete')
requirements_choices.place(x=180, y=391)

add_button = customtkinter.CTkButton(app, command=insert, font=font1, text_color='#fff', text='Add Applicant', fg_color='#05A312', hover_color='#00850B', bg_color='#161C25', border_color='#00FF00', cursor='hand2', corner_radius=17, width=265)
add_button.place(x=20, y=504)

clear_button = customtkinter.CTkButton(app, command=lambda: clear(True), font=font1, text_color='#fff', text='New Applicant', fg_color='#161C25', hover_color='#EC9706', bg_color='#161C25', border_color='#EC9706', border_width=1.5, cursor='hand2', corner_radius=17, width=265)
clear_button.place(x=20, y=574)

update_button = customtkinter.CTkButton(app, command=update, font=font1, text_color='#fff', text='Update Applicant', fg_color='#161C25', hover_color='#EC9706', bg_color='#161C25', border_color='#EC9706', border_width=1.5, cursor='hand2', corner_radius=17, width=265)
update_button.place(x=300, y=574)

delete_button = customtkinter.CTkButton(app, command=delete, font=font1, text_color='#fff', text='Delete Applicant', fg_color='#E40404', hover_color='#710C04', bg_color='#161C25', border_color='#710C04', border_width=1.5, cursor='hand2', corner_radius=17, width=265)
delete_button.place(x=580, y=574)

style = ttk.Style(app)

style.theme_use('clam')
style.configure('Treeview', font=font2, foreground='#fff', background='#000', fieldbackground='#313837')
style.map('Treeview', background=[('selected', '#1A8F2D')])

tree = ttk.Treeview(app, height=25)

tree['columns'] = ('Entry Number', 'Name', 'Gender', 'Birthday', 'Contact Info', 'Occupant Amt.', 'Job', 'Requirements')

tree.column('#0', width=0, stretch=tk.NO)
tree.column('Entry Number', anchor=tk.CENTER, width=75)
tree.column('Name', anchor=tk.CENTER, width=220)
tree.column('Gender', anchor=tk.CENTER, width=100)
tree.column('Birthday', anchor=tk.CENTER, width=120)
tree.column('Contact Info', anchor=tk.CENTER, width=123)
tree.column('Occupant Amt.', anchor=tk.CENTER, width=95)
tree.column('Job', anchor=tk.CENTER, width=125)
tree.column('Requirements', anchor=tk.CENTER, width=105)

tree.heading('Entry Number', text='Ent. Number')
tree.heading('Name', text='Name')
tree.heading('Gender', text='Gender')
tree.heading('Birthday', text='Birthday')
tree.heading('Contact Info', text='Contact Info')
tree.heading('Occupant Amt.', text='Occupant Amt.')
tree.heading('Job', text='Job')
tree.heading('Requirements', text='Requirements')

tree.place(x=380, y=25)

tree.bind('<ButtonRelease>', display_data)

add_to_treeview()

app.mainloop()