#import libraries
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3

#function to define database
def Database():
    global conn, cursor
    #creating contact database
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    #creating REGISTRATION table
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS REGISTRATION (RID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, ID TEXT NOT NULL, LName TEXT NOT NULL, FName TEXT NOT NULL, Gender TEXT NULL, Year_Level TEXT NOT NULL, Course_Code TEXT NOT NULL,Course TEXT NOT NULL)")

#defining function for creating GUI Layout
def DisplayForm():
    #creating window
    display_screen = Tk()
    #setting width and height for window
    display_screen.geometry("1200x450")
    #setting title for window
    display_screen.title("Simple Student Information System")
    global tree
    global SEARCH
    global id,fname,lname,gender,yearlevel,coursecode,course
    SEARCH = StringVar()
    id = StringVar()
    fname = StringVar()
    lname = StringVar()
    gender = StringVar()
    yearlevel = StringVar()
    coursecode = StringVar()
    course = StringVar()

    #creating frames for layout
    #topview frame for heading
    TopViewForm = Frame(display_screen, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)

    #first left frame for registration from
    LFrom = Frame(display_screen, width="350",bg="yellow")
    LFrom.pack(side=LEFT, fill=Y)

    #seconf left frame for search form
    LeftViewForm = Frame(display_screen, width=500,bg="light green")
    LeftViewForm.pack(side=LEFT, fill=Y)

    #mid frame for displaying lnames record
    MidViewForm = Frame(display_screen, width=600)
    MidViewForm.pack(side=RIGHT)

    #label for heading
    lbl_text = Label(TopViewForm, text="STUDENT INFORMATION SYSTEM", font=('palatino', 30), fg="yellow", width=600,bg="red")
    lbl_text.pack(fill=X)

    #creating registration form in first left frame
    Label(LFrom, text="ID ", font=("Arial", 12),bg="yellow",fg="black").pack(side=TOP)
    Entry(LFrom,font=("Arial",10,"bold"),textvariable=id).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="LAST NAME ", font=("Arial", 12),bg="yellow",fg="black").pack(side=TOP)
    Entry(LFrom,font=("Arial",10,"bold"),textvariable=fname).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="FIRST NAME ", font=("Arial", 12),bg="yellow",fg="black").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=lname).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="GENDER ", font=("Arial", 12),bg="yellow",fg="black").pack(side=TOP)

    #Entry(LFrom, font=("Arial", 10, "bold"),textvariable=gender).pack(side=TOP, padx=10, fill=X)
    gender.set("SELECT GENDER")
    content={'MALE','FEMALE'}
    OptionMenu(LFrom,gender,*content).pack(side=TOP, padx=10, fill=X)

    Label(LFrom, text="YEAR LEVEL", font=("Arial", 12),bg="yellow",fg="black").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=yearlevel).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="COURSE CODE ", font=("Arial", 12),bg="yellow",fg="black").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=coursecode).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="COURSE", font=("Arial", 12),bg="yellow",fg="black").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=course).pack(side=TOP, padx=10, fill=X)
    Button(LFrom,text="ADD",font=("Arial", 10, "bold"),command=register,bg="pink",fg="black").pack(side=TOP, padx=10,pady=5, fill=X)

    #creating search label and entry in second frame
    lbl_txtsearch = Label(LeftViewForm, text="Enter ID to Search:", font=('Arial', 10), fg="white", bg="green")
    lbl_txtsearch.pack()
    #creating search entry
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('Arial', 10), width=12)
    search.pack(side=TOP, padx=10, fill=X)
    #creating search button
    btn_search = Button(LeftViewForm, text="SEARCH", font=("Arial",10), command=SearchRecord,bg="pink")
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating view button
    btn_view = Button(LeftViewForm, text="VIEW ALL", font=("Arial",10), command=DisplayData,bg="pink")
    btn_view.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating reset button
    btn_reset = Button(LeftViewForm, text="RESET", font=("Arial",10), command=Reset,bg="pink")
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating delete button
    btn_delete = Button(LeftViewForm, text="DELETE", font=("Arial",10), command=Delete,bg="pink")
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    #create update button
    btn_delete = Button(LeftViewForm, text="UPDATE", font=("Arial",10), command=Update,bg="pink")
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_exit = Button(LeftViewForm, text="EXIT", font=("Arial",10), command=Exit,bg="yellow")
    btn_exit.pack(side=TOP, padx=10, pady=10, fill=X)
    #setting scrollbar
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm,columns=("No","ID", "LName", "FName", "Gender","Year_Level","Course_Code","Course"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    #setting headings for the columns
    tree.heading('No', text="No.", anchor=W)
    tree.heading('ID', text="ID", anchor=W)
    tree.heading('FName', text="First Name", anchor=W)
    tree.heading('LName', text="Last Name", anchor=W)
    tree.heading('Gender', text="Gender", anchor=W)
    tree.heading('Year_Level', text="Year Level", anchor=W)
    tree.heading('Course_Code', text="Course Code", anchor=W)
    tree.heading('Course', text="Course", anchor=W)

    #setting width of the columns
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=100)
    tree.column('#3', stretch=NO, minwidth=0, width=100)
    tree.column('#4', stretch=NO, minwidth=0, width=100)
    tree.column('#5', stretch=NO, minwidth=0, width=100)
    tree.column('#6', stretch=NO, minwidth=0, width=100)
    tree.column('#7', stretch=NO, minwidth=0, width=100)
    tree.pack()
    DisplayData()
    
#function to update data into database
def Update():
    Database()
    #getting form data
    id1=id.get()
    fname1=fname.get()
    lname1=lname.get()
    gender1=gender.get()
    yearlevel1=yearlevel.get()
    coursecode1=coursecode.get()
    course1=course.get()

    #applying empty validation
    if id1=='' or fname1=='' or lname1==''or gender1=='' or yearlevel1=='' or coursecode1=='' or course1=='':
        tkMessageBox.showinfo("Warning","fill the empty field!!!")
    else:
        #getting selected data
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['values']
        #update query
        conn.execute('UPDATE REGISTRATION SET ID=?,FName=?,LName=?,Gender=?,Year_Level=?,Course_Code=?,Course=? WHERE RID =?',(id1,fname1,lname1,gender1,yearlevel1,coursecode1,course1, selecteditem[0]))
        conn.commit()
        tkMessageBox.showinfo("Message","Updated successfully")
        #reset form
        Reset()
        #refresh table data
        DisplayData()
        conn.close()

def register():
    Database()
    #getting form data
    id1=id.get()
    fname1=fname.get()
    lname1=lname.get()
    gender1=gender.get()
    yearlevel1=yearlevel.get()
    coursecode1=coursecode.get()
    course1=course.get()
    #applying empty validation
    if id1=='' or fname1=='' or lname1==''or gender1=='' or yearlevel1=='' or coursecode1=='' or course=='':
        tkMessageBox.showinfo("Warning","fill the empty field!!!")
    else:
        #execute query
        conn.execute('INSERT INTO REGISTRATION (ID,FName,LName,Gender,Year_Level,Course_Code,Course) \
              VALUES (?,?,?,?,?,?,?)',(id1,fname1,lname1,gender1,yearlevel1,coursecode1,course1));
        conn.commit()
        tkMessageBox.showinfo("Message","Stored successfully")
        #refresh table data
        DisplayData()
        conn.close()
        Reset()
        
def Reset():
    #clear current data from table
    tree.delete(*tree.get_children())
    #refresh table data
    DisplayData()
    #clear search text
    SEARCH.set("")
    id.set("")
    fname.set("")
    lname.set("")
    gender.set("")
    yearlevel.set("")
    coursecode.set("")
    course.set("")

def Delete():
    #open database
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Warning","Select data to delete")
    else:
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            cursor=conn.execute("DELETE FROM REGISTRATION WHERE RID = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

#function to search data
def SearchRecord():
    #open database
    Database()
    #checking search text is empty or not
    if SEARCH.get() != "":
        #clearing current display data
        tree.delete(*tree.get_children())
        #select query with where clause
        cursor=conn.execute("SELECT * FROM REGISTRATION WHERE ID LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        #fetch all matching records
        fetch = cursor.fetchall()
        #loop for displaying all records into GUI
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

#defining function to access data from SQLite database
def DisplayData():
    #open database
    Database()
    #clear current data
    tree.delete(*tree.get_children())
    #select query
    cursor=conn.execute("SELECT * FROM REGISTRATION")
    #fetch all data from database
    fetch = cursor.fetchall()
    #loop for displaying all data in GUI
    for data in fetch:
        tree.insert('', 'end', values=(data))
        tree.bind("<Double-1>",OnDoubleClick)
    cursor.close()
    conn.close()

def OnDoubleClick(self):
    #getting focused item from treeview
    curItem = tree.focus()
    contents = (tree.item(curItem))
    selecteditem = contents['values']
    #set values in the fields
    id.set(selecteditem[1])
    fname.set(selecteditem[2])
    lname.set(selecteditem[3])
    gender.set(selecteditem[4])
    yearlevel.set(selecteditem[5])
    coursecode.set(selecteditem[6])
    course.set(selecteditem[7])

def Exit():
    result = tkMessageBox.askquestion('Student Information System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        exit()

#calling function
DisplayForm()
if __name__=='__main__':
    #Running Application
    mainloop()