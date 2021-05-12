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
    messagebox.showinfo('About','โปรแกรมบันทึกข้อมูลค่าใช้จ่ายจัดทำขึ้นเพื่อจัดระเบียบการเงิน\nติดต่อเจ้าของโปรแกรมได้ที่เมลล์ lm_jelly@hotmail.com')
helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About', command=About)
###########################

'''
style = ttk.Style()
style.theme_create( "MyStyle", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {"configure": {"padding": [50, 20] },}})

style.theme_use("MyStyle")
'''

Tab = ttk.Notebook(GUI)

T1 = Frame(Tab)
T2 = Frame(Tab)
Tab.pack(fill=BOTH, expand=1)

vocabicon = PhotoImage(file='vocab.png')
listicon = PhotoImage(file='list.png')


'''
# f'{"tab short": ^50s}
# f'{"tab longgggggggggg": ^50s}'

https://stackoverflow.com/questions/8450472/how-to-print-a-string-at-a-fixed-width
https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep498
>>> f'{"HELLO": <{20}}'
'HELLO               '
>>> f'{"HELLO": >{20}}'
'               HELLO'
>>> f'{"HELLO": ^{20}}'
'       HELLO        '
'''
### web load icon http://www.iconarchive.com/
Tab.add(T1, text=f'{"Add vocab": ^50s}', image=vocabicon,compound='top')
Tab.add(T2, text=f'{"vocab List": ^50s}', image=listicon,compound='top')
#Tab.add(T2, text='vocab List', image=listicon,compound='top')

# B1 = Button(GUI,text='Hello')
# B1.pack(ipadx=50,ipady=20) #.pack() ติดปุ่มเข้ากับ GUI หลัก
 
F1 = Frame(T1)
#F1.place(x=140,y=10)
F1.pack()

today = datetime.date.today()

days = {'Mon':'จันทร์',
        'Tue':'อังคาร',
        'Wed':'พุธ',
        'Thu':'พฤหัสบดี',
        'Fri':'ศุกร์',
        'Sat':'เสาร์',
        'Sun':'อาทิตย์'}


def Save(event=None):
    
    vocab = v_vocab.get()
    part_of_speech = v_part_of_speech.get()
    meaning = v_meaning.get()
    example = v_example.get()

    if vocab == '': #or part_of_speech == '' or meaning =='':
      messagebox.showwarning('Error','กรุณากรอกรายการคำศัพท์')
      #print('Not completed Info')
      #messagebox.showwarning('Error','กรุณากรอกข้อมูลให้ครบ')
      return
    elif part_of_speech == '':
      messagebox.showwarning('Error','กรุณากรอกหน้าที่ของคำ')
      return
    elif meaning == '':
      messagebox.showwarning('Error','กรุณากรอกความหมาย') 
    elif example == '':
      messagebox.showwarning('Error','กรุณากรอกตัวอย่าง') 

    try:
              # .get() คือดึงค่ามาจาก v_vocab = StringVar()
        #print('รายการ: {} หน้าที่ของคำ: {} ความหมาย: {} ตัวอย่าง: {}' .format(vocab,part_of_speech,meaning,example))
        
        text = 'รายการ: {} หน้าที่ของคำ: {} ความหมาย: {}\n ตัวอย่าง: {}'.format(vocab,part_of_speech,meaning,example)        #\n เป็นการขึ้นบรรทัดใหม่
        v_result.set(text)

        # clear ข้อมูลเก่า
        v_vocab.set('')
        v_part_of_speech.set('')
        v_meaning.set('')
        v_example.set('') 
        # บันทึกข้อมูลลง csv อย่าลืม import csv ด้วย
        from datetime import datetime

        today = datetime.now().strftime('%a') # days['Mon'] = 'จันทร์'
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



#F2 = Frame(T2)
#F1.place(x=140,y=10)
#F2.pack()
v_result = StringVar()
#v_result.set('     ผลลัพธ์      ')
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

# def update_record():
#     getdata = read_csv()
#     v_allrecord.set('')
#     text = ''
#     for d in getdata:
#         txt = '{}--{}--{}--{}--{}--{}\n'.format(d[0],d[1],d[2],d[3],d[4],d[5])
#         text = text+txt
#     v_allrecord.set(text)



# v_allrecord = StringVar()
# v_allrecord.set('----All Record----')
# Allrecord = ttk.Label(T2,textvariable=v_allrecord,font=FONT1,foreground='teal')
# Allrecord.pack()






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
    #my_entry.delete(0, 'end')

def Clear():
    result_table.delete(*result_table.get_children())   # ล้างค่าทุกครั้งก่อน อ่านค่าใหม่ *เทียบเท่า run for loop แบบไม่เอา ''
    # for c in result_table.get_children() :            # หรือใช้วิธี for loop ก็ได้
    #     result_table.delete(c)

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


#result_table.bind("<<ListboxSelect>>", fillout)

ClearButton = ttk.Button(T2,text='Clear',command=Clear)
ClearButton.place(x=15,y=20,width=100)


 

            
# # Create a binding on the listbox onclick
# result_table.bind("<<ListboxSelect>>", fillout)

# # Create a binding on the entry box
# my_entry.bind("<KeyRelease>", check)


GUI.bind('<Tab>',lambda x: E2.focus())   
GUI.mainloop()
