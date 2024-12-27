import sqlite3
import tkinter as tk
from tkinter import messagebox

# Создаем соединение с базой данных (если файл базы данных не существует, он будет создан)
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Создаем таблицу (если она еще не существует)
cursor.execute('''CREATE TABLE IF NOT EXISTS records (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER,
                    email TEXT)''')
conn.commit()

def add_data():
    name = entry_name.get()
    age = entry_age.get()
    email = entry_email.get()
    if name and age and email:
        cursor.execute("INSERT INTO records (name, age, email) VALUES (?, ?, ?)", (name, age, email))
        conn.commit()
        messagebox.showinfo("Success", "Data added successfully!")
        clear_entries()
    else:
        messagebox.showerror("Error", "All fields are required!")

def delete_data():
    record_id = entry_id.get()
    if record_id:
        cursor.execute("DELETE FROM records WHERE id = ?", (record_id,))
        conn.commit()
        messagebox.showinfo("Success", "Data deleted successfully!")
        clear_entries()
    else:
        messagebox.showerror("Error", "ID is required!")

def update_data():
    record_id = entry_id.get()
    name = entry_name.get()
    age = entry_age.get()
    email = entry_email.get()
    if record_id and name and age and email:
        cursor.execute("UPDATE records SET name = ?, age = ?, email = ? WHERE id = ?", (name, age, email, record_id))
        conn.commit()
        messagebox.showinfo("Success", "Data updated successfully!")
        clear_entries()
    else:
        messagebox.showerror("Error", "All fields are required!")

def fetch_data():
    cursor.execute("SELECT * FROM records")
    records = cursor.fetchall()
    text_output.delete(1.0, tk.END)
    for record in records:
        text_output.insert(tk.END, f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}, Email: {record[3]}\n")

def search_by_name():
    search_term = entry_name.get()
    if search_term:
        cursor.execute("SELECT * FROM records WHERE name LIKE ?", ('%' + search_term + '%',))
        records = cursor.fetchall()
        text_output.delete(1.0, tk.END)
        for record in records:
            text_output.insert(tk.END, f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}, Email: {record[3]}\n")
    else:
        messagebox.showerror("Error", "Please enter a name to search.")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_id.delete(0, tk.END)

# Создаем окно Tkinter
window = tk.Tk()
window.title("Database Manager")

# Создаем поля для ввода данных
label_name = tk.Label(window, text="Name:")
label_name.grid(row=0, column=0)
entry_name = tk.Entry(window)
entry_name.grid(row=0, column=1)

label_age = tk.Label(window, text="Age:")
label_age.grid(row=1, column=0)
entry_age = tk.Entry(window)
entry_age.grid(row=1, column=1)

label_email = tk.Label(window, text="Email:")
label_email.grid(row=2, column=0)
entry_email = tk.Entry(window)
entry_email.grid(row=2, column=1)

label_id = tk.Label(window, text="ID (for delete/update):")
label_id.grid(row=3, column=0)
entry_id = tk.Entry(window)
entry_id.grid(row=3, column=1)

# Создаем кнопки
button_add = tk.Button(window, text="Add Data", command=add_data)
button_add.grid(row=4, column=0)

button_delete = tk.Button(window, text="Delete Data", command=delete_data)
button_delete.grid(row=4, column=1)

button_update = tk.Button(window, text="Update Data", command=update_data)
button_update.grid(row=5, column=0)

button_fetch = tk.Button(window, text="Fetch All Data", command=fetch_data)
button_fetch.grid(row=5, column=1)

button_search = tk.Button(window, text="Search by Name", command=search_by_name)
button_search.grid(row=6, column=0)

# Поле для отображения данных
text_output = tk.Text(window, height=10, width=50)
text_output.grid(row=7, column=0, columnspan=2)

# Запуск окна
window.mainloop()

# Закрытие соединения при выходе
conn.close()

