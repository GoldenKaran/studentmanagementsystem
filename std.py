
from importlib.resources import contents
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql


class student():
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")

        title = Label(self.root, text="Library Management System", bd=10, relief=GROOVE, font=(
            "times new roman", 40, "bold"), bg="yellow", fg="red")
        title.pack(side=TOP, fill=X)
# ===========All Variables==========
        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()


# ======Manage Frame=============

        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Manage_Frame.place(x=20, y=100, width=450, height=600)

        m_title = Label(Manage_Frame, text="Manage students", bg="crimson",fg="white", font=("times new roman", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_roll = Label(Manage_Frame, text="Roll No.", bg="crimson",fg="white", font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_Roll = Entry(Manage_Frame, textvariable=self.Roll_No_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name = Label(Manage_Frame, text="Name", bg="crimson",fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_name = Entry(Manage_Frame, textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_email = Label(Manage_Frame, text="Email", bg="crimson",fg="white", font=("times new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_email = Entry(Manage_Frame, textvariable=self.email_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(Manage_Frame, text="Gender", bg="crimson",fg="white", font=("times new roman", 20, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender = ttk.Combobox(Manage_Frame, textvariable=self.gender_var, font=("times new roman", 13, "bold"), state='readonly')
        combo_gender['values'] = ("Male", "Female", "Other")
        combo_gender.grid(row=4, column=1, padx=20, pady=10)

        lbl_contact = Label(Manage_Frame, text="Contact", bg="crimson",fg="white", font=("times new roman", 20, "bold"))
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_contact = Entry(Manage_Frame, textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_Dob = Label(Manage_Frame, text="D.O.B", bg="crimson",fg="white", font=("times new roman", 20, "bold"))
        lbl_Dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_Dob = Entry(Manage_Frame, textvariable=self.dob_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_Address = Label(Manage_Frame, text="Address", bg="crimson",fg="white", font=("times new roman", 20, "bold"))
        lbl_Address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.txt_Address = Text(Manage_Frame, width=30,height=4, font=("", 10))
        self.txt_Address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        # =========Button Frame===========================
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="crimson")
        btn_Frame.place(x=15, y=530, width=420)

        Addbtn = Button(btn_Frame, text="Add", width=10).grid(row=0, column=0, padx=10, pady=10)
        Updatebtn = Button(btn_Frame, text="Update", width=10).grid(row=0, column=1, padx=10, pady=10)
        Deletebtn = Button(btn_Frame, text="Delete", width=10).grid(row=0, column=2, padx=10, pady=10)
        Clearbtn = Button(btn_Frame, text="Clear", width=10).grid(row=0, column=3, padx=10, pady=10)

# ========================Detail Frame =====================================

        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=500, y=100, width=850, height=580)

        lbl_Search = Label(Detail_Frame, text="Search By", bg="crimson",fg="white", font=("times new roman", 20, "bold"))
        lbl_Search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_Search = ttk.Combobox(Detail_Frame, textvariable=self.search_by, width=10, font=("times new roman", 13, "bold"), state='readonly')
        combo_Search['values'] = ("Roll_No", "Name", "Contact")
        combo_Search.grid(row=0, column=1, padx=20, pady=10, sticky="w")

        txt_Search = Entry(Detail_Frame, textvariable=self.search_txt, width=20, font=("times new roman", 10, "bold"), bd=5, relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(Detail_Frame, text="Search", width=10, pady=5).grid(row=0, column=3, padx=10, pady=10)
        showallbtn = Button(Detail_Frame, text="Report Gen.", width=10, pady=5).grid(row=0, column=4, padx=10, pady=10)

# ===========Table Frame==========================
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=820, height=500)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.students_table = ttk.Treeview(Table_Frame, columns=("roll", "name", "email", "gender", "contact", "dob", "Address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.students_table.xview)
        scroll_y.config(command=self.students_table.yview)
        self.students_table.heading("roll", text="Roll No.")
        self.students_table.heading("name", text="Name")
        self.students_table.heading("email", text="Email")
        self.students_table.heading("gender", text="Gender")
        self.students_table.heading("contact", text="Contact")
        self.students_table.heading("dob", text="D.O.B")
        self.students_table.heading("Address", text="Address")

        self.students_table['show'] = 'headings'
        self.students_table.column("roll", width=100)
        self.students_table.column("name", width=100)
        self.students_table.column("email", width=100)
        self.students_table.column("gender", width=100)
        self.students_table.column("contact", width=100)
        self.students_table.column("dob", width=100)
        self.students_table.column("Address", width=100)
        self.students_table.pack(fill=BOTH, expand=1)
        #self.students_table.bind("<ButtonRelease-1>",self.get_cursor)
        #self.fetch_data()
        
    def add_students(self):
        if self.Roll_No_var.get() == "" or self.name_var.get() == "":
            messagebox.showerror("Error", "all fields are required to fill")
        else:
            con = pymysql.connector.connect(host="localhost", user="root", password="", database="karan")
            cur = con.cursor()
            cur.execute("insert into stud values (%s,%s,%s,%s,%s,%s,%s)", (self.Roll_No_var.get(),
                                                                           self.name_var.get(),
                                                                           self.email_var.get(),
                                                                           self.gender_var.get(),
                                                                           self.contact_var.get(),
                                                                           self.dob_var.get(),
                                                                           self.txt_Address.get(
                                                                               '1.0', END)
                                                                           ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been inserted")
        def fetch_data(self):
            con = pymysql.connector.connect(host="localhost", user="root", password="", database="karan")
            cur=con.cursor()
            cur.execute("select * from stud")
            rows=cur.fetchall()
            if len(rows)!=0:
                self.students_table.delete(*self.students_table.get_children())
                for row in rows:
                    self.students_table.insert('',END,values=row)
                con.commit()
            con.close()
            
        def get_cursor(self,ev):
                curosor_row=self.students_table.focus()
                contents=self.students_table.item(curosor_row)
                row=contents['values']
                
                self.Roll_No_var.set(row[0])
                self.name_var.set(row[1])
                self.email_var.set(row[2])
                self.gender_var.set(row[3])
                self.contact_var.set(row[4])
                self.dob_var.set(row[5])
                self.txt_Address.delete("1.0",END)
                self.txt_Address.insert(END,row[6])
                
            
        def clear(self):
            self.Roll_No_var.set("")
            self.name_var.set("")
            self.email_var.set("")
            self.gender_var.set("")
            self.contact_var.set("")
            self.dob_var.set("")
            self.txt_Address.delete("1.0",END)

class Student():

    root = Tk()
    root.geometry("1350x750")
    ob = student(root)
    root.mainloop()
