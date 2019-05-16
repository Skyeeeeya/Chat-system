##import pymysql
from tkinter import *

init_window=Tk()        #实例化出一个父窗口
 ##设置窗口属性
init_window.title("Skye and Jennie Chat system Login")
init_window.geometry('700x400+10+10')  

# welcome image
canvas = Canvas(init_window, height=150, width=430)#创建画布
canvas.pack(side=TOP)#放置画布（为上端）
image_file = PhotoImage(file='/Users/wanyiyang/Desktop/pygame/welcome.gif')#加载图片文件
image = canvas.create_image(0,0, anchor='nw', image=image_file)#将图片置于画布上

#建立输入框
#mysql 地址
##labe_iddr = Label(init_window, text="mysql地址")
##labe_iddr.pack()  
##text_iddr_default = StringVar()
##text_iddr = Entry(init_window, textvariable = text_iddr_default)
##text_iddr_default.set("localhost")
##text_iddr.pack()
#账户
labe_user = Label(init_window, text="账户")
labe_user.pack()  
text_user_default = StringVar()
text_user = Entry(init_window, textvariable = text_user_default)
text_user_default.set("")
text_user.pack()
#密码
labe_pwd = Label(init_window, text="密码")
labe_pwd.pack()  
text_pwd_default = StringVar()
text_pwd = Entry(init_window, textvariable = text_pwd_default)
text_pwd_default.set("")
text_pwd.pack()

#建立按钮
##通过command属性来指定Button的回调函数
button_sure = Button(init_window,text="确定",width=15,height=2,command=inset_get)
button_sure.pack()
init_window.mainloop()
##6.按钮回调函数，拷贝输入框的字符串，然后将字符串用于连接数据库
 
def inset_get():
    mysql_host = text_iddr.get()
    mysql_user = text_user.get()
    mysql_pwd  = text_pwd.get()
print(mysql_host,mysql_user,mysql_pwd)
try :
#连接数据库
    global db_login
    db_login=pymysql.connect(host="%s"%mysql_host,user="%s"%mysql_user,passwd="%s"%mysql_pwd,db="jailsystem",charset="utf8")
    init_window.destroy()
    main()
except:
    print("ERROR:mysql not connect")
    messagebox.showinfo(title='login faild', message='登录失败，请重新登录 ')

