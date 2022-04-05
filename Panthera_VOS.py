from tkinter import *
from tkinter import messagebox
import webbrowser
import tkinter.font
import platform
import time
from tkinter import *
from tkinter import ttk, colorchooser
import psutil
from time import strftime
import pyttsx3
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from tkinter import colorchooser
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
def Pantheraos():
    root = Tk()
    root.title("Panthera VOS")
    root.wm_attributes('-fullscreen', 'True')
    root.config(bg = "White")
    battery = psutil.sensors_battery()
    percent = str(battery.percent)
    lu = Label(root, text = percent+"%",font = ("Verdana"), bg = "White", fg = "Black").place(x = 1315, y = 735)
    lulu = Label(root, text = "Hello, "+ user_name + "!", font = ("Verdana", 22), bg = "White", fg = "Black").place(x = 100, y = 15)
    mainlab = Label(root, text = "Panthera.", font = ("Verdana", 72), bg = "White", fg = "Black").place(x = 450, y = 300)
    sec = Label(root, text = "Virtual Operating System", font = ("Verdana", 18), bg = "White", fg = "Black").place(x = 700, y = 405)
    def ext():
        root.destroy()
    #Browser
    def NavigatorB():
        class Window(QMainWindow):
            def __init__(self):
                super(Window,self).__init__()
                self.browser = QWebEngineView()
                self.browser.setUrl(QUrl('http://google.com'))
                self.setCentralWidget(self.browser)
                self.showMaximized()
                navbar = QToolBar()
                self.addToolBar(navbar)
                prevBtn = QAction('<',self)
                prevBtn.triggered.connect(self.browser.back)
                navbar.addAction(prevBtn)
                nextBtn = QAction('>',self)
                nextBtn.triggered.connect(self.browser.forward)
                navbar.addAction(nextBtn)
                refreshBtn = QAction('Refresh',self)
                refreshBtn.triggered.connect(self.browser.reload)
                navbar.addAction(refreshBtn)
                homeBtn = QAction('Home',self)
                homeBtn.triggered.connect(self.home)
                navbar.addAction(homeBtn)
                self.searchBar = QLineEdit()
                self.searchBar.returnPressed.connect(self.loadUrl)
                navbar.addWidget(self.searchBar)
                self.browser.urlChanged.connect(self.updateUrl)
            def home(self):
                self.browser.setUrl(QUrl('http://google.com'))
            def loadUrl(self):
                url = self.searchBar.text()
                self.browser.setUrl(QUrl(url))
            def updateUrl(self, url):
                self.searchBar.setText(url.toString())
        MyApp = QApplication(sys.argv)
        QApplication.setApplicationName('Navigator Browser')
        window = Window()
        MyApp.Panthera_()
        #/Browser
    def setto():
        top = Toplevel()
        top.title("Preferences")
        top.config(bg = "White")
        top.resizable(0,0)
        top.geometry("350x500+150+100")
        offlab = Label(top, text = "Preferences", bg = "White", fg = "Black").pack()
        def themeseto():
            root.config(bg = "Black")
            top.config(bg = "Black")
        poc = PhotoImage(file = r"F:\\Programming\\Python\\Panthera VOS\\moon.png")
        ptimage = poc.subsample(2,2)
        Button(top, image = ptimage,command = themeseto, border = "0").place(x = 10, y = 50)
        top.mainloop()
    def applico():
        tpp = Toplevel()        
        tpp.geometry("350x500")
        tpp.title("Panthera Utilities")
        tpp.resizable(0,0)
        def dfbo():
            webbrowser.open("https://www.google.com/")
        betuo = Button(tpp, text = "Default Webbrowser",border = "0", command = dfbo).place(x = 7, y = 60)
        Prefo = Button(tpp, text = "Preferences", border = "0", command = setto).place(x = 7, y = 90)
        arto = Button(tpp, text = "Panthera Artist", border = "0", command = artist).place(x = 7, y = 120)
        luo = Label(tpp, text = "Panthera Utilities", font = ("Verdana")).pack()
        tpp.mainloop()
    def sysinfo():
        titu = Toplevel()
        titu.resizable(0,0)
        def ok():
            titu.destroy()
        titu.title("System Info")
        titu.geometry("350x150")
        info = f"System: {platform.system()}\n \
        User name: {platform.node()}\n \
        Version: {platform.version()}\n \
        Machine: {platform.machine()}\n \
        "
        my_labu = Label(titu, text = info, font = ("Verdana", 14)).pack()
        betu = Button(titu, text = "Ok",border = "0",command = ok,font = ("Verdana", 10)).place(x = 300, y = 110)
        titu.mainloop()
    def artist():
        class main:
            def __init__(self,master):
                self.master = master
                self.color_fg = 'black'
                self.color_bg = 'white'
                self.old_x = None
                self.old_y = None
                self.penwidth = 5
                self.drawWidgets()
                self.c.bind('<B1-Motion>',self.paint)#drwaing the line 
                self.c.bind('<ButtonRelease-1>',self.reset)

            def paint(self,e):
                if self.old_x and self.old_y:
                    self.c.create_line(self.old_x,self.old_y,e.x,e.y,width=self.penwidth,fill=self.color_fg,capstyle=ROUND,smooth=True)

                self.old_x = e.x
                self.old_y = e.y

            def reset(self,e):    #reseting or cleaning the canvas 
                self.old_x = None
                self.old_y = None      

            def changeW(self,e): #change Width of pen through slider
                self.penwidth = e
                

            def clear(self):
                self.c.delete(ALL)

            def change_fg(self):  #changing the pen color
                self.color_fg=colorchooser.askcolor(color=self.color_fg)[1]

            def change_bg(self):  #changing the background color canvas
                self.color_bg=colorchooser.askcolor(color=self.color_bg)[1]
                self.c['bg'] = self.color_bg

            def drawWidgets(self):
                self.controls = Frame(self.master,padx = 5,pady = 5)
                Label(self.controls, text='Pen Width:',font=('arial 18')).grid(row=0,column=0)
                self.slider = ttk.Scale(self.controls,from_= 5, to = 100,command=self.changeW,orient=VERTICAL)
                self.slider.set(self.penwidth)
                self.slider.grid(row=0,column=1,ipadx=30)
                self.controls.pack(side=LEFT)
                
                self.c = Canvas(self.master,width=500,height=400,bg=self.color_bg,)
                self.c.pack(fill=BOTH,expand=True)

                menu = Menu(self.master)
                self.master.config(menu=menu)
                filemenu = Menu(menu)
                colormenu = Menu(menu)
                menu.add_cascade(label='Colors',menu=colormenu)
                colormenu.add_command(label='Brush Color',command=self.change_fg)
                colormenu.add_command(label='Background Color',command=self.change_bg)
                optionmenu = Menu(menu)
                menu.add_cascade(label='Options',menu=optionmenu)
                optionmenu.add_command(label='Clear Canvas',command=self.clear)
                optionmenu.add_command(label='Exit',command=self.master.destroy) 
        if __name__ == '__main__':
            root = Tk()
            main(root)
            root.resizable(0,0)
            root.title('Panthera Artist')
            root.mainloop()
            #
    pcc = PhotoImage(file = r"F:\\Programming\\Python\\Panthera VOS\\panther.png")
    pytimage = pcc.subsample(1,1)
    Button(root, image = pytimage,command = applico, border = "0").place(x = 10, y = 10)
    puc = PhotoImage(file = r"F:\\Programming\\Python\\Panthera VOS\\power.png")
    pitimage = puc.subsample(2,2)
    Button(root, image = pitimage, command = ext , border = "0").place(x = 1320, y = 10)
    pic = PhotoImage(file = r"F:\\Programming\\Python\\Panthera VOS\\navigatr.png")
    pimage = pic.subsample(2,2)
    Button(root, image = pimage,command = NavigatorB, border = "0").place(x = 15, y = 300)
    photo = PhotoImage(file = r"F:\\Programming\\Python\\Panthera VOS\\settings-3110.png")
    photoimage = photo.subsample(2, 2)
    Button(root, image = photoimage,command = setto, border = "0").place(x = 15, y = 200)
    poto = PhotoImage(file = r"F:\\Programming\\Python\\Panthera VOS\\Panthera-artist.png")
    photoimge = poto.subsample(2, 2)
    Button(root, image = photoimge,command = artist, border = "0").place(x = 15, y = 400)  
    peto = PhotoImage(file = r"F:\\Programming\\Python\\Panthera VOS\\yours.png")
    photoim = peto.subsample(2, 2)
    Button(root, image = photoim,command = sysinfo, border = "0").place(x = 15, y = 500)
    #
    def time():
           string = strftime('%H:%M:%S')
           lbl.config(text = string)
           lbl.after(1000, time)
    lbl = Label(root, font = ('Verdana', 22), bg = "White", fg = "Black")
    lbl.pack()
    time()
    root.mainloop()
print()
print()
print("             Panthera Virtual Operating System | System - 0.6")
print()
print()
print()
print("		[1] Continue Startup.")
print("		[2] Terminal.")
print("                [3] Quit.")
print()
bootak = input("	 	>.  ")
if bootak == "1":
	user_name = input("		Enter the user-name you want to continue the whole session with: ")
	activation = input("	        Enter Panthera OS authentication key: ")
	if activation == "betatest":
		print("                Authentication successful!")
		Pantheraos()
	else:
		print("                Authentication Failed!")
elif bootak == "3":
	exit()
elif bootak == "2":
    un = input("            Enter the user-name you want to continue the Terminal-session with : ")
    print("         The Panthera OS Terminal")
    print()
    def termio():
        termo = input("         [>>>].   ")
        if termo == "exit":
            exit()
        elif termo == "fetch-authKey":
            print("         Panthera OS Authentication Key : " + "betatest")
        elif "user info" in termo:
            print("         User : " + un)
        elif "cnt dir" in termo:
            cwd = os.getcwd()
            print("         " + cwd)
        elif termo == "sys info":
            print("         Panthera Virtual Operating System - BETA System V - 0.6")
        elif "help" in termo:
            print("         Help:")
            print("         This Virtual Operating System is built by Abeer Joshi and is not distributed yet...")
            print("         be the first one to test it!")
        elif "echo" in termo:
            print("         ### Welcome to Panthera Echo! - A fun way to hear to yourself! ###")
            heor = input("          What do you want to hear? :  ")
            engine = pyttsx3.init()
            engine.setProperty("rate", 130)
            engine.say(heor)
            engine.runAndWait()
        elif "list dir" in termo:
            path = input("Parent Directory [C: / F: / E: ...]  :  ")
            dir_list = os.listdir(path)
            print("Files and directories in '", path, "' :")
            print(dir_list)
        elif termo == "boot panthera":
            Pantheraos()
        else:
            print("         '"+ termo + "' is not recognized as an external command.")
    for x in range(1000):
        termio()
else:
    print("Unable to get desired response from the user, Quiting the program...")
    exit()
