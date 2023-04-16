from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
import mysql.connector
from tkinter import messagebox
from datetime import date
today = date.today().strftime('%d.%m.%y')

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="q1wer234",
database="hi"
)
mycursor = mydb.cursor()

class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x750+50+0")
        self.root.state("zoomed")
        self.root.title("Repair Services Management System")
        
        # Variables
        self.var_job_id=StringVar()
        self.var_date=StringVar()
        self.var_date.set(today)
        self.var_party_name=StringVar()
        self.var_mobile_name=StringVar()
        self.var_address=StringVar()
        self.var_item_name=StringVar()
        self.var_item_desc=StringVar()
        self.var_estimate=StringVar()
        self.var_est_deldate=StringVar()
        self.var_del_taken_date=StringVar()
        self.var_delivery_status=StringVar()



        lbl_title=Label(self.root,text='Repair Services Management System',font=('times new roman',40,'bold'),fg='darkblue',bg='white')
        lbl_title.place(x=0,y=0,width=1530,height=60)
        
        img_logo=Image.open('pnp.jpg')
        img_logo=img_logo.resize((80,60))
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=270,y=0,width=50)

        # Frame 1
        frame1=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        frame1.place(x=10,y=70,width=450,height=720)

        #Labels and Entry 
        r=0
        
        label_name=Label(frame1,text='Job ID',font=('times new roman',15,),fg='darkblue',bg='white')
        label_name.grid(row=r,column=0,padx=2,sticky=W)

        self.var_job_id.set(self.ser_no())
        job_id_entry=ttk.Entry(frame1,textvariable=self.var_job_id,width=28,font=('times new roman',15),state=DISABLED)
        job_id_entry.grid(row=r,column=1,padx=2,pady=7)


        r+=1

        
        label_name=Label(frame1,text='Date',font=('times new roman',15,),fg='darkblue',bg='white')
        label_name.grid(row=r,column=0,padx=2,sticky=W)

        date_entry=ttk.Entry(frame1,textvariable=self.var_date,width=28,font=('times new roman',15))
        date_entry.grid(row=r,column=1,padx=2,pady=7)

        r+=1

        
        label_name=Label(frame1,text='Party Name',font=('times new roman',15,),fg='darkblue',bg='white')
        label_name.grid(row=r,column=0,padx=2,sticky=W)

        name_entry=ttk.Entry(frame1,textvariable=self.var_party_name,width=28,font=('times new roman',15))
        name_entry.grid(row=r,column=1,padx=2,pady=7)

        r+=1

        
        label_name=Label(frame1,text='Mobile No. ',font=('times new roman',15,),fg='darkblue',bg='white')
        label_name.grid(row=r,column=0,padx=2,sticky=W)

        mobile_entry=ttk.Entry(frame1,textvariable=self.var_mobile_name,width=28,font=('times new roman',15))
        mobile_entry.grid(row=r,column=1,padx=2,pady=7)

        r+=1

        
        label_name=Label(frame1,text='Address',font=('times new roman',15,),fg='darkblue',bg='white')
        label_name.grid(row=r,column=0,padx=2,sticky=W)

        address_entry=ttk.Entry(frame1,textvariable=self.var_address,width=28,font=('times new roman',15))
        address_entry.grid(row=r,column=1,padx=2,pady=7)

        r+=1

        
        label_name=Label(frame1,text='Item Name',font=('times new roman',15,),fg='darkblue',bg='white')
        label_name.grid(row=r,column=0,padx=2,sticky=W)

        item_entry=ttk.Entry(frame1,textvariable=self.var_item_name,width=28,font=('times new roman',15))
        item_entry.grid(row=r,column=1,padx=2,pady=7)

        r+=1

        
        label_name=Label(frame1,text='Item Description',font=('times new roman',15,),fg='darkblue',bg='white')
        label_name.grid(row=r,column=0,padx=2,sticky=W)

        item_desc_entry=ttk.Entry(frame1,textvariable=self.var_item_desc,width=28,font=('times new roman',15))
        item_desc_entry.grid(row=r,column=1,padx=2,pady=7)

        r+=1

        
        label_name=Label(frame1,text='Estimate',font=('times new roman',15,),fg='darkblue',bg='white')
        label_name.grid(row=r,column=0,padx=2,sticky=W)

        estimate_entry=ttk.Entry(frame1,textvariable=self.var_estimate,width=28,font=('times new roman',15))
        estimate_entry.grid(row=r,column=1,padx=2,pady=7)

        r+=1

        
        label_name=Label(frame1,text='Est. Del. Date',font=('times new roman',15,),fg='darkblue',bg='white')
        label_name.grid(row=r,column=0,padx=2,sticky=W)

        est_deldate_entry=ttk.Entry(frame1,textvariable=self.var_est_deldate,width=28,font=('times new roman',15))
        est_deldate_entry.grid(row=r,column=1,padx=2,pady=7)

        r+=1


        label_name=Label(frame1,text='Del. Taken Date',font=('times new roman',15,),fg='darkblue',bg='white')
        label_name.grid(row=r,column=0,padx=2,sticky=W)

        deltakendate_entry=ttk.Entry(frame1,textvariable=self.var_del_taken_date,width=28,font=('times new roman',15))
        deltakendate_entry.grid(row=r,column=1,padx=2,pady=7)

        r+=1

        label_dep=Label(frame1,text='Delivery Status',font=('times new roman',15),fg='darkblue',bg='white')
        label_dep.grid(row=r,column=0,padx=2,sticky=W)
        
        delstatus_entry=ttk.Combobox(frame1,textvariable=self.var_delivery_status,font=('times new roman',13),width=29,state='readonly')
        delstatus_entry['value']=('Pending','Delivery Taken')
        delstatus_entry.current(0)
        delstatus_entry.grid(row=r, column=1,padx=2,sticky=W)
        r+=1
       

        # Button frame n then buttons
        frame_3=Frame(frame1,bd=2,relief=RIDGE,bg='white')
        frame_3.place(x=5,y=600,width=430,height=72)


        Btn_add=Button(frame_3,text='Save',font=('times new roman',15),fg='darkblue',bg='white',padx=20,command=self.add_data)
        Btn_add.grid(row=r,column=0,padx=20,pady=15)

        Btn_add=Button(frame_3,text='Update',font=('times new roman',15),fg='darkblue',bg='white',padx=20,command=self.update_data)
        Btn_add.grid(row=r,column=1,padx=20,pady=15)

        Btn_add=Button(frame_3,text='Delete',font=('times new roman',15),fg='darkblue',bg='white',padx=20,command=self.delete_data)
        Btn_add.grid(row=r,column=2,padx=20,pady=15)

        # Frame 2 is right side frame
        r=0
        frame2=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        frame2.place(x=465,y=70,width=1060,height=720)
        
        # Search Frame
        self.var_search_phone=StringVar()
        self.var_search=StringVar()

        search_frame=Frame(frame2,bd=2,relief=RIDGE,bg='white')
        search_frame.place(x=5,y=5,width=1045,height=50)

        search_label=Label(search_frame,text='Search By :- ',font=('times new roman',15),fg='darkblue',bg='white',padx=20)
        search_label.grid(row=r,column=0)

        searchoption_entry=ttk.Combobox(search_frame,textvariable=self.var_search,font=('times new roman',13),width=29,state='readonly')
        searchoption_entry['value']=('Mobile','Pending Delivery','Done Delivery')
        searchoption_entry.current(0)
        searchoption_entry.grid(row=r, column=1,padx=2,sticky=W)
        # print(combo_dep.current())
        search_cell=ttk.Entry(search_frame,textvariable=self.var_search_phone,width=28,font=('times new roman',15))
        search_cell.grid(row=r,column=2,padx=2,pady=7)
        search_cell.insert(0,'Enter Mobile Number')

        search_btn=Button(search_frame,text='Search ',font=('times new roman',15),fg='darkblue',bg='white',padx=20,command=self.search)
        search_btn.grid(row=r,column=3,padx=10)

        show_all_btn=Button(search_frame,text='Show All ',font=('times new roman',15),fg='darkblue',bg='white',padx=20,command=self.fetch_data)
        show_all_btn.grid(row=r,column=4,padx=10)
    
        # Table Frame
        table_frame=Frame(frame2,bd=2,relief=RIDGE,bg='white')
        table_frame.place(x=5,y=60,width=1045,height=650)

        # scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        
        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL,width=10)
        scroll_x.pack(side=BOTTOM,fill=X)

        scroll_y=Scrollbar(table_frame,orient=VERTICAL,width=10)
        scroll_y.pack(side=RIGHT,fill=Y)

        r=0
        self.entry_table=ttk.Treeview(table_frame,columns=('job_id','date_title','name_title','mobile_title','address_title','item_title','item_desc_title','estimate_title','estimate_deldate_title','del_date_title','del_status_title'),xscrollcommand = scroll_x.set,yscrollcommand=scroll_y.set)
 
        scroll_x.config(command=self.entry_table.xview)
        scroll_y.config(command=self.entry_table.yview) 
        
        self.entry_table.heading('job_id',text='Job ID')
        self.entry_table.heading('date_title',text='Date')
        self.entry_table.heading('name_title',text='Name')
        self.entry_table.heading('mobile_title',text='Mobile Number')
        self.entry_table.heading('address_title',text='Address')
        self.entry_table.heading('item_title',text='Items ')
        self.entry_table.heading('item_desc_title',text='Item Description')
        self.entry_table.heading('estimate_title',text='Estimate')
        self.entry_table.heading('estimate_deldate_title',text='Est. Del. Date')
        self.entry_table.heading('del_date_title',text='Del. Date')
        self.entry_table.heading('del_status_title',text='Del. Status')
       
        self.entry_table['show']='headings'
        self.entry_table.column('job_id',width=50)
        self.entry_table.column('date_title',width=70)
        self.entry_table.column('name_title',width=150)
        self.entry_table.column('mobile_title',width=100)
        self.entry_table.column('address_title',width=100)
        self.entry_table.column('item_title',width=150)
        self.entry_table.column('item_desc_title',width=100)
        self.entry_table.column('estimate_title',width=70)
        self.entry_table.column('estimate_deldate_title',width=80)
        self.entry_table.column('del_date_title',width=70)
        self.entry_table.column('del_status_title',width=100)
        self.fetch_data()

        self.entry_table.pack(fill=BOTH,expand=1)
        self.entry_table.bind('<ButtonRelease>',self.get_cursor)

         
    # Function For Job ID
    def ser_no(self):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT Job_ID FROM rsms ORDER BY Job_ID DESC LIMIT 1")
        ans=mycursor.fetchall()
        if not ans:
            x=1
        else:
            x=ans[0][0]+1
        return x
    
    def add_data(self):
        mycursor.execute('insert into rsms values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
            self.var_job_id.get(),
            self.var_date.get(),
            self.var_party_name.get(),
            self.var_mobile_name.get(),
            self.var_address.get(),
            self.var_item_name.get(),
            self.var_item_desc.get(),
            self.var_estimate.get(),
            self.var_est_deldate.get(),
            self.var_del_taken_date.get(),
            self.var_delivery_status.get()
        ))

        mydb.commit()
        self.fetch_data()
        # mydb.close()
        messagebox.showinfo('Success ','Entry Added Successfully! ',parent=self.root )
        self.reset()

    # Fetch Data
    def fetch_data(self):
        mycursor.execute('SELECT *from rsms ORDER BY Job_ID DESC')
        data=mycursor.fetchall()
        if len(data)!=0:
            self.entry_table.delete(*self.entry_table.get_children())
            for i in data:
                self.entry_table.insert("",END,values=i)
                mydb.commit()
                                

    # fetch data from list to entry 
    def get_cursor(self,event=""):
        cursor_row=self.entry_table.focus()
        content=self.entry_table.item(cursor_row)
        data=content['values']

        self.var_job_id.set(data[0])
        self.var_date.set(data[1])
        self.var_party_name.set(data[2])
        self.var_mobile_name.set(data[3])
        self.var_address.set(data[4])
        self.var_item_name.set(data[5])
        self.var_item_desc.set(data[6])
        self.var_estimate.set(data[7])
        self.var_est_deldate.set(data[8])
        self.var_del_taken_date.set(data[9])
        self.var_delivery_status.set(data[10])

    # Update Data:
    def update_data(self):
        update=messagebox.askyesno('Update','Are you sure to Update')
        if update>0:
            mycursor.execute(
            'update rsms set Date=%s,Party_Name=%s,Mobile=%s,Address=%s,Item=%s,Item_Desc=%s,Estimate=%s,Est_Del_Date=%s,Del_Taken_Date=%s,Del_Status=%s WHERE Job_ID=%s',(
                self.var_date.get(),
                self.var_party_name.get(),
                self.var_mobile_name.get(),
                self.var_address.get(),
                self.var_item_name.get(),
                self.var_item_desc.get(),
                self.var_estimate.get(),
                self.var_est_deldate.get(),
                self.var_del_taken_date.get(),
                self.var_delivery_status.get(),
                self.var_job_id.get(),
            ))

        else :
            if not update:
                return

        mydb.commit()        
        self.fetch_data()
        messagebox.showinfo('Success','Data Updated Successfully',parent=self.root)
        self.reset()

    
    # Delete Function 
    def delete_data(self):
        Delete=messagebox.askyesno('Delete','Are You Sure Delete This Employee')
        if Delete>0:
            mycursor.execute(
                'delete from rsms where Job_ID=%s',
                (self.var_job_id.get(),)
            )
        else:
            if not Delete:
                return   
        mydb.commit()   
        self.fetch_data()
        messagebox.showinfo('Delete','Entry Deleted.')  
        self.reset()


    def reset(self):
    
        self.var_job_id.set(""),
        self.var_date.set(""),
        self.var_party_name.set(""),
        self.var_mobile_name.set(""),
        self.var_address.set(""),
        self.var_item_name.set(""),
        self.var_item_desc.set(""),
        self.var_estimate.set(""),
        self.var_est_deldate.set(""),
        self.var_del_taken_date.set(""),
        self.var_delivery_status.set("")
        self.var_job_id.set(self.ser_no())
        self.var_date.set(today)
        self.var_delivery_status.set("Pending")
        



    def search(self):
        if (self.var_search.get()=='' or self.var_search_phone==''):
            messagebox.showerror('Error','Pls. select search moethod.')
        else :
            # try:
                print(self.var_search.get())
                x=self.var_search_phone.get()
                if (self.var_search.get()=='Mobile' and len(x)>0 ):
                    query="SELECT *FROM rsms WHERE Mobile LIKE '"+str(self.var_search_phone.get())+"_%' ORDER BY Job_ID DESC"
                    print(query)
                    mycursor.execute(query)
                    data=mycursor.fetchall()
                    if len(data)!=0:
                        self.entry_table.delete(*self.entry_table.get_children())
                        for i in data:
                            self.entry_table.insert("",END,values=i)
                            mydb.commit()
                
                elif (self.var_search.get()=='Pending Delivery'):
                    query="SELECT *FROM rsms WHERE Del_Status LIKE 'Pending' ORDER BY Job_ID DESC"
                    mycursor.execute(query)
                    data=mycursor.fetchall()
                    if len(data)!=0:
                        self.entry_table.delete(*self.entry_table.get_children())
                        for i in data:
                            self.entry_table.insert("",END,values=i)
                            mydb.commit()
                elif (self.var_search.get()=='Done Delivery'):
                    query="SELECT *FROM rsms WHERE Del_Status LIKE 'Delivery Taken' ORDER BY Job_ID DESC"
                    mycursor.execute(query)
                    data=mycursor.fetchall()
                    if len(data)!=0:
                        self.entry_table.delete(*self.entry_table.get_children())
                        for i in data:
                            self.entry_table.insert("",END,values=i)
                            mydb.commit()    


    def date_check(x):
        i=0
        digit=0
        flag=False
        sym=0
        while (i<len(x)):
                
            if (x[i]=='/' or x[i]=='.'):
                x[i]='.'
            elif (not (x[i]<='9' and x[i]>='0')):
                flag=True
                break 
                
        #now check for dd,mm,yy
        i=0
        #Check for DD
        if (not flag):    
            while(x[i]!='.'):
                i+=1
                if (i>2):
                    flag=True
                    break
            c=i
            i+=1    
        # Now Check For MM
        if (not flag):    
            while(x[i]!='.'):
                i+=1
                if ((c-i)>2):
                    flag=True
                    break
            c=i    
            i+=1

        # Now Check For YYYY
        if (not flag):    
            while(x[i]!='.'):
                i+=1
                if ((c-i)>4):
                    flag=True
                    break








 

if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()


