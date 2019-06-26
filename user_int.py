from tkinter import *
from code import Database

database=Database("books.db")

#Initializing the GUI Window
class Window(object):

    def __init__(self, window):

        self.window=window
        self.window.wm_title("BOOK LIBRARY")

        #Labels for the Book details in GUI
        l1 =Label(window, text= "Title")
        l1.grid(row=0, column=0)

        l2 =Label(window, text= "Author")
        l2.grid(row=0, column=2)

        l3 =Label(window, text= "ISBN")
        l3.grid(row=1, column=0)

        l4 =Label(window, text= "Year")
        l4.grid(row=1, column=2)

        #Text box to take entry from user in GUI
        self.title_text= StringVar()
        self.e1= Entry(window, textvariable= self.title_text)
        self.e1.grid(row=0, column=1)

        self.author_text= StringVar()
        self.e2= Entry(window, textvariable= self.author_text)
        self.e2.grid(row=0, column=3)

        self.year_text= StringVar()
        self.e3= Entry(window, textvariable=self. year_text)
        self.e3.grid(row=1, column=1)

        self.isbn_text= StringVar()
        self.e4= Entry(window, textvariable= self.isbn_text)
        self.e4.grid(row=1, column=3)

        #List box that will show the details of books with the scroll bar to access books
        self.list1= Listbox(window, height=6, width= 35)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

        sb1= Scrollbar(window)
        sb1.grid(row=2, column=2, rowspan=6)

        self.list1.configure(yscrollcommand= sb1.set)
        sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        #Buttons for the GUI controlling the functions
        b1=Button(window, width=12, text="View All", command=self.view_command) #View
        b1.grid(row=2, column=3)
        b2=Button(window, width=12, text="Search Entry",command=self.search_command) #Search
        b2.grid(row=3, column=3)
        b3=Button(window, width=12, text="Add Entry",command=self.add_command) #Insert
        b3.grid(row=4, column=3)
        b4=Button(window, width=12, text="Update Entry",command=self.update_command) #Update
        b4.grid(row=5, column=3)
        b5=Button(window, width=12, text="Delete Entry", command=self.delete_command) #Delete
        b5.grid(row=6, column=3)
        b6=Button(window, width=12, text="Close",command=window.destroy) #Close the application
        b6.grid(row=7, column=3)

    #Defining functions
    def view_command(self): 
        self.list1.delete(0,END)
        for rows in database.view():
            self.list1.insert(END, rows)

    def search_command(self):
        self.list1.delete(0, END)
        for rows in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
            self.list1.insert(END, rows)

    def add_command(self):
        database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.list1.delete(0,END)
        self.list1.insert(END,(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))

    def get_selected_row(self,event):
        index=self.list1.curselection()[0]
        self.selected_tuple=self.list1.get(index)
        self.e1.delete(0,END)
        self.e1.insert(END,self.selected_tuple[1])
        self.e2.delete(0,END)
        self.e2.insert(END,self.selected_tuple[2])
        self.e3.delete(0,END)
        self.e3.insert(END,self.selected_tuple[3])
        self.e4.delete(0,END)
        self.e4.insert(END,self.selected_tuple[4])

    def delete_command(self):
        database.delete(self.selected_tuple[0])

    def update_command(self):
        database.update(self.selected_tuple[0], self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())

window=Tk()    #defining window with tkinter
Window(window)
window.mainloop()
