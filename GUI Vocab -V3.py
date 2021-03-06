# GUIBasic2-vocab.py
from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import *
import csv
import datetime

# ttk is theme of Tk

GUI = Tk()
GUI.title('โปรแกรมบันทึกคำศัพท์ by Yale')
GUI.geometry('800x600+250+20')

############MENU###############
menubar = Menu(GUI)
GUI.config(menu=menubar)

# File menu
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Import CSV')
filemenu.add_command(label='Export to Googlesheet')

# Help
def About():
    messagebox.showinfo('About','Vocabulary learning focused on SAT and GRE\n Any recommendation pls contact lm_jelly@hotmail.com')
helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About', command=About)



Tab = ttk.Notebook(GUI)

T1 = Frame(Tab)
T2 = Frame(Tab)
Tab.pack(fill=BOTH, expand=1)

vocabicon = PhotoImage(file='vocab.png')
listicon = PhotoImage(file='list.png')


### web load icon http://www.iconarchive.com/
Tab.add(T1, text=f'{"Add vocab": ^50s}', image=vocabicon,compound='top')
Tab.add(T2, text=f'{"vocab List": ^50s}', image=listicon,compound='top')

F1 = Frame(T1)
#F1.place(x=140,y=10)
F1.pack()

today = datetime.date.today()

def Save(event=None):
    
    vocab = v_vocab.get()
    part_of_speech = v_part_of_speech.get()
    meaning = v_meaning.get()
    example = v_example.get()

    if vocab == '': #or part_of_speech == '' or meaning =='':
      messagebox.showwarning('Error','Pls input a vocab')
      #print('Not completed Info')
      #messagebox.showwarning('Error','Pls fill up all information.')
      return
    elif part_of_speech == '':
      messagebox.showwarning('Error','Part of Speech missing')
      return
    elif meaning == '':
      messagebox.showwarning('Error','Definition missing') 
      return
    elif example == '':
      messagebox.showwarning('Error','Example of sentece missing') 
      return

    try:
              # .get() คือดึงค่ามาจาก v_vocab = StringVar()
                
        text = 'word: {} ,Part of Speech: {} , Definition: {}\n Example: {}'.format(vocab,part_of_speech,meaning,example)        #\n เป็นการขึ้นบรรทัดใหม่
        v_result.set(text)

        # clear 
        v_vocab.set('')
        v_part_of_speech.set('')
        v_meaning.set('')
        v_example.set('') 
        # writ to csv อย่าลืม import csv ด้วย
        from datetime import datetime

        today = datetime.now().strftime('%a') 
        dt = datetime.now().strftime('%d/%m/%Y %H:%M')
        with open('savedata6.1.csv','a',encoding='utf-8',newline='') as f:
            # with คือสั่งเปิดไฟล์แล้วปิดอัตโนมัติ
            # 'a' การบันทึกเรื่อยๆ เพิ่มข้อมูลต่อจากข้อมูลเก่า
            # newline='' ทำให้ข้อมูลไม่มีบรรทัดว่าง
            fw = csv.writer(f) #สร้างฟังชั่นสำหรับเขียนข้อมูล
            data = [vocab,part_of_speech,meaning,example,dt]
            fw.writerow(data)

        # ทำให้เคอเซอร์กลับไปตำแหน่งช่องกรอก E1
        E1.focus()
        update_table()
        
    except Exception as e: #(เป็น technique การดูว่า error ตรงไหน)
        #print(e)
        print("ERROR",e)
        messagebox.showwarning ('Error','กรุณาระบุข้อมูลให้ถูกต้อง')
        #messagebox.showerror('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
        #messagebox.showinfo ('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
        v_vocab.set('')
        v_part_of_speech.set('')
        v_meaning.set('') 
        v_example.set('') 
        
        
# ทำให้สามารถกด enter ได้
GUI.bind('<Return>',Save) #ต้องเพิ่มใน def Save(event=None) ด้วย

FONT1 = ("TH SarabunPSK",14) # None เปลี่ยนเป็น 'Angsana New'
FONT2 = ("TH SarabunPSK",22)
FONT3 = ("TH SarabunPSK",18,'bold','underline')

centerimg = PhotoImage(file='wallet.png')
logo = ttk.Label(F1,image=centerimg)
logo.pack()


#------text1--------
L = ttk.Label(F1,text='Word',font=FONT1).pack()
v_vocab = StringVar()
# StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E1 = ttk.Entry(F1,textvariable=v_vocab,font=FONT1)
E1.pack()
#-------------------

#------text2--------
L = ttk.Label(F1,text='Part of Speech',font=FONT1).pack()
v_part_of_speech = StringVar()
# StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E2 = ttk.Entry(F1,textvariable=v_part_of_speech,font=FONT1)
E2.pack()
#-------------------

#------text3--------
L = ttk.Label(F1,text='Definition',font=FONT1).pack()
v_meaning = StringVar()
# StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E3 = ttk.Entry(F1,textvariable=v_meaning,font=FONT1,width=60)
E3.pack()
#-------------------
#------text4--------
L = ttk.Label(F1,text='Example Sentence',font=FONT1).pack()
v_example = StringVar()
# StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E3 = ttk.Entry(F1,textvariable=v_example,font=FONT1,width=100)
E3.pack()


saveicon = PhotoImage(file='save.png')


B2 = ttk.Button(F1,text=f'{"Save": >{6}}',command=Save,image=saveicon,compound='left')
B2.pack(ipadx=30,ipady=5,pady=15)


v_result = StringVar()
result = ttk.Label(F1, textvariable=v_result, font=FONT1,foreground='darkslategrey')
# result = Label(F1, textvariable=v_result, font=FONT1,fg='teal')
result.pack(pady=5)


###########TAB2###########

def read_csv():
    with open('savedata6.1.csv',newline='',encoding='utf-8') as f:    
    # with open ช่วยให้เปิดและปิดได้เลย (ป้องกันการลืม close ถ้าลืมโปรแกรมจะ error) ไม่ต้องไปใส่ function open และ close ซึ่งต้องทำอีก 2 บรรทัด
        fr = csv.reader(f)      # fr stands for file reader
        data = list(fr)         # ถ้าไม่ใส่ list จะอ่านค่าไม่ออก
    return data                 # ต้องการค่าไปใช้งานต่อ ต้อง return
        # print(data)           # วิธี select แล้ว comment ลัดคือ กด ctrl+/
        # print('----')
        # print(data[0][0])
        # for d in data:
        #   print(d)
        # for a,b,c,d,e,f in data:
        #     print(b)


# table
L = ttk.Label(T2,text='ตารางแสดงผลลัพธ์',font=FONT3, foreground='teal').pack(pady=20)
header = ['Word','Part of Speech','Definition','Example Sentece','Record Date']
result_table = ttk.Treeview(T2, columns=header,show='headings',height=20)   # height เพิ่มความสูงของ table
result_table.pack()

# สร้าง ชื่อใน header ทำได้ 2 วิธี
# for i in range(len(header)):
#     result_table.heading(header[i],text=header[i])

for h in header:  
    result_table.heading(h,text=h)

headerwidth = [150,90,350,440,150]    #ตั้งค่าขนาดคอลัมภ์
for h,w in zip(header,headerwidth):
    result_table.column(h,width = w)

# result_table.insert('','end',value=['จันทร์','น้ำดื่ม',33,4,132]
def update_table():
    result_table.delete(*result_table.get_children())   # ล้างค่าทุกครั้งก่อน อ่านค่าใหม่ *เทียบเท่า run for loop แบบไม่เอา ''
    # for c in result_table.get_children() :            # หรือใช้วิธี for loop ก็ได้
    #     result_table.delete(c)

    data = read_csv()
    for d in data:
        result_table.insert('',0,value=d)   # 0 หมายถึง ข้อมูลล่าสุดอยู่บนสุด 'end' หมายถึง ข้อมูลไล่ตามลำดับ

update_table()


def search(self):
    data = read_csv()
    for d in data:
        result_table.insert('',0,value=d) 
   
    result_table.delete(*result_table.get_children())
    word=v_search.get()
    
    if v_search.get():
        for a,b,c,d,e in data:
            if word in a:
                result_table.insert('', 0, values=(a,b,c,d,e))
    else:
        for a,b,c,d,e in data:
            result_table.insert('', 0, values=(a,b,c,d,e))
    
def Clear():
    result_table.delete(*result_table.get_children())   # ล้างค่าทุกครั้งก่อน อ่านค่าใหม่ *เทียบเท่า run for loop แบบไม่เอา ''
    data = read_csv()
    for d in data:
        result_table.insert('',0,value=d)   # 0 หมายถึง ข้อมูลล่าสุดอยู่บนสุด 'end' หมายถึง ข้อมูลไล่ตามลำดับ
    v_search.set('') 

# searching
# StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
v_search = StringVar()
my_entry = ttk.Entry(T2,textvariable=v_search,font=FONT1,width=50)
my_entry.place(x=130,y=15,width=160)
#my_entry.bind("<Return>", Clear)
my_entry.bind("<KeyRelease>", search)


ClearButton = ttk.Button(T2,text='Clear',command=Clear)
ClearButton.place(x=15,y=20,width=100)


GUI.bind('<Tab>',lambda x: E2.focus())   
GUI.mainloop()
