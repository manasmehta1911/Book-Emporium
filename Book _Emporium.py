from tkinter import * 
import backend
from tkinter import messagebox

def get_selected_row(event):
    global selected_tuple
    index=listb.curselection()[0]
    selected_tuple=listb.get(index)

    entry1.delete(0,END)
    entry1.insert(END, selected_tuple[1])

    entry2.delete(0,END)
    entry2.insert(END, selected_tuple[2])

    entry3.delete(0,END) 
    entry3.insert(END, selected_tuple[3])

    entry4.delete(0,END)
    entry4.insert(END, selected_tuple[4])

    entry5.delete(0,END)
    entry5.insert(END, selected_tuple[5])

    entry6.delete(0,END)
    entry6.insert(END, selected_tuple[6])

def add_command():
        try:
            (title_text.get(), author_text.get() ,int(year_text.get()) ,int(isbn_text.get()),genre_text.get(),int(price_text.get()))
        except ValueError:
            messagebox.showinfo("Alert!!","Year/ISBN/Price cannot be Alphabet")
        if(str(title_text.get())=="" or str(author_text.get())=="" or str(genre_text.get())==""):
            messagebox.showinfo("Alert!!","Title , Author or Genre cannot be empty")
        else:
            backend.insert(title_text.get(), author_text.get() ,int(year_text.get()) ,int(isbn_text.get()),genre_text.get(),int(price_text.get()))
            listb.insert(END, title_text.get(), author_text.get() ,year_text.get() ,isbn_text.get(), genre_text.get(),price_text.get())

def display_command():
    listb.delete(0,END)
    for row in backend.display():
        listb.insert(END, row)

def search_command():
    listb.delete(0,END)
    for row in backend.search(title_text.get(), author_text.get() ,year_text.get() ,isbn_text.get(), genre_text.get(),price_text.get()):
        listb.insert(END, row)

def upd_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get() ,year_text.get() ,isbn_text.get(), genre_text.get(),price_text.get())

def del_command():
    backend.delete(selected_tuple[0])
    display_command()

window= Tk()
window.wm_title("Book Emporium")

l1= Label(window,text="Title")
l1.grid(row=0,column=0)

l2= Label(window,text="Author")
l2.grid(row=0,column=2)

l3= Label(window,text="Year")
l3.grid(row=1,column=0)

l4= Label(window,text="ISBN")
l4.grid(row=1,column=2)

l5= Label(window,text="Genre")
l5.grid(row=2,column=0)

l6= Label(window,text="Price")
l6.grid(row=2,column=2)

title_text=StringVar()
entry1=Entry(window,textvariable=title_text)
entry1.grid(row=0,column=1)

author_text=StringVar()
entry2=Entry(window,textvariable=author_text)
entry2.grid(row=0,column=3)

year_text=StringVar()
entry3=Entry(window,textvariable=year_text)
entry3.grid(row=1,column=1)

isbn_text=StringVar()
entry4=Entry(window,textvariable=isbn_text)
entry4.grid(row=1,column=3)

genre_text=StringVar()
entry5=Entry(window,textvariable=genre_text)
entry5.grid(row=2,column=1)

price_text=StringVar()
entry6=Entry(window,textvariable=price_text)
entry6.grid(row=2,column=3)

listb=Listbox(window,height=6,width=45)
listb.grid(row=3,column=0,rowspan=6,columnspan=2)

sb=Scrollbar(window)
sb.grid(row=3,column=2,rowspan=6)

listb.configure(yscrollcommand=sb.set)
sb.configure(command=listb.yview)

listb.bind("<<ListboxSelect>>",get_selected_row)

b1=Button(window,text="Display All",width=10 ,command=display_command)
b1.grid(row=3,column=3)

b2=Button(window,text="Search Book",width=10 ,command=search_command)
b2.grid(row=4,column=3)

b3=Button(window,text="Add Book",width=10, command=add_command)
b3.grid(row=5,column=3)

b4=Button(window,text="Update Book",width=10,command=upd_command)
b4.grid(row=6,column=3)

b5=Button(window,text="Delete Book",width=10,command=del_command)
b5.grid(row=7,column=3)

b6=Button(window,text="Close",width=10,command=window.destroy)
b6.grid(row=8,column=3)

window.mainloop()