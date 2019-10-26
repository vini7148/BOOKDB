from tkinter import Tk, Button, Label, Scrollbar, Listbox, StringVar, Entry, W, E, N, S, END
from tkinter import ttk # wiggitd lib
from tkinter import messagebox
from sqlserver_config import dbConfig
import pypyodbc as pyo

con = pyo.connect(**dbConfig)
# print(con)

cursor = con.cursor()


class bookdb:
	def __init__(self): # constructor
		self.con = pyo.connect(**dbConfig)
		self.cursor = con.cursor()
		print("You have connected to DATABASE")
		print(con)

	def __del__(self): # destructor
		self.con.close()

	def view(self):
		self.cursor.execute("SELECT * from books")
		row = self.cursor.fetchall()
		return row

	def insert(self, title, author, isbn):
		sql = ("INSERT INTO books(title, author, isbn)VALUES (?, ?, ?)")
		values = [title, author, isbn]
		self.cursor.execute(sql, values)
		self.con.commit()
		messagebox.showinfo(title = "Book database", message = "New book added")

	def update(self, id, title, author, isbn):
		tsql = 'UPDATE books SET title = ?, author = ?, isbn = ? WHERE id = ?'
		self.cursor.execute(tsql, [title, author, isbn, id])
		self.con.commit()
		messagebox.showinfo(title = "Book database", message = "Book updated")

	def delete(self, id):
		delq = 'Delete from books where id = ?'
		self.cursor.execute(delq, [id])
		self.con.commit()
		messagebox.showinfo(title = "Book database", message = "Book deleted")

db = bookdb()

def get_selected_row(event):
	global selected_tuple
	index = li_b.curselection()[0]
	selected_tuple = li_b.get(index)
	t_e.delete(0, 'end')
	t_e.insert('end', selected_tuple[1])
	a_e.delete(0, 'end')
	a_e.insert('end', selected_tuple[2])
	i_e.delete(0, 'end')
	i_e.insert('end', selected_tuple[3])

def view_records():
	li_b.delete(0, 'end')
	for row in db.view():
		li_b.insert('end', row)

def add_book():
	db.insert(t_txt.get(), a_txt.get(), i_txt.get())
	li_b.delete(0, 'end')
	li_b.insert('end', (t_txt.get(), a_txt.get(), i_txt.get()))
	t_e.delete(0, 'end')
	a_e.delete(0, 'end')
	i_e.delete(0, 'end')
	con.commit()

def delete_records():
	db.delete(selected_tuple[0])
	con.commit()

def clear_screen():
	li_b.delete(0, 'end')
	t_e.delete(0, 'end')
	a_e.delete(0, 'end')
	i_e.delete(0, 'end')

def update_records():
	db.update(selected_tuple[0], t_txt.get(), a_txt.get(), i_txt.get())
	t_e.delete(0, 'end')
	a_e.delete(0, 'end')
	i_e.delete(0, 'end')
	con.commit()

def on_closing():
	dd = db
	if messagebox.askokcancel("Quit", "Do you want to quit?"):
		root.destroy()
		del dd


root = Tk() # to make a window

root.title("MYBOOKS DATABASE APPLICATION")
root.configure(background = "light green")
root.geometry("850x540") # 50% for 1080p
root.resizable(width = False, height = False)


t_l = ttk.Label(root, text = "Title", background = "light green", font = ("TkDefaultFont", 16))
t_l.grid(row = 0, column = 0, sticky = W)
t_txt = StringVar()
t_e = ttk.Entry(root, width = 24, textvariable = t_txt)
t_e.grid(row = 0, column = 1, sticky = W)

a_l = ttk.Label(root, text = "Author", background = "light green", font = ("TkDefaultFont", 16))
a_l.grid(row = 0, column = 2, sticky = W)
a_txt = StringVar()
a_e = ttk.Entry(root, width = 24, textvariable = a_txt)
a_e.grid(row = 0, column = 3, sticky = W)

i_l = ttk.Label(root, text = "ISBN", background = "light green", font = ("TkDefaultFont", 16))
i_l.grid(row = 0, column = 4, sticky = W)
i_txt = StringVar()
i_e = ttk.Entry(root, width = 24, textvariable = i_txt)
i_e.grid(row = 0, column = 5, sticky = W)

ad_bt = Button(root, text = "Add Book", bg = "blue", fg = "white", font = "helvetica 10 bold", command = add_book)
ad_bt.grid(row = 0, column = 6, sticky = W)


li_b = Listbox(root, height = 16, width = 40, font = "helvetica 13", bg = "light blue")
li_b.grid(row = 3, column = 1, columnspan = 14, sticky = W + E, pady = 40, padx = 15)
li_b.bind('<<ListboxSelect>>', get_selected_row)

sc_b = Scrollbar(root)
sc_b.grid(row = 1, column = 8, rowspan = 14, sticky = W)

li_b.configure(yscrollcommand = sc_b.set)
sc_b.configure(command = li_b.yview)


m_bt = Button(root, text = "Modify Record", bg = "purple", fg = "white", font = "helvetica 10 bold", command = update_records)
m_bt.grid(row = 15, column = 4)

d_bt = Button(root, text = "Delete Record", bg = "purple", fg = "white", font = "helvetica 10 bold", command = delete_records)
d_bt.grid(row = 15, column = 5)

v_bt = Button(root, text = "View all records", bg = "purple", fg = "white", font = "helvetica 10 bold", command = view_records)
v_bt.grid(row = 15, column = 1)

c_bt = Button(root, text = "Clear Screen", bg = "purple", fg = "white", font = "helvetica 10 bold", command = clear_screen)
c_bt.grid(row = 15, column = 2)

e_bt = Button(root, text = "Exit Application", bg = "purple", fg = "white", font = "helvetica 10 bold", command = root.destroy)
e_bt.grid(row = 15, column = 3)


# last line of file to keep the file running until exit
root.mainloop()