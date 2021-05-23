from tkinter import *
import chat_both_project as cbp
import pyttsx3

#print('Hello')

#=================================functions-start========================================
engine = pyttsx3.init()

def Btn_submit():
    asks=ask_txt.get()
    result=cbp.check_chat(asks)
    prt="ME: "+asks+"\nBoth: "+result+"\n"
    text.insert(END,prt+"\n")

    engine.say(result)
    engine.runAndWait()

    #text.insert(END,"hello world\n")
    

def btn_clear():
    text.delete("1.0",END)
    #ask_txt.insert(END,"")
    

#=================================functions-End========================================


#==================================design-START===========================================
screen= Tk()
screen.geometry("300x400")
screen.title("Python form")
#screen.attributes("-fullscreen", True)

#head
heading=Label(text="AI Chat Both",bg="grey",fg="white",width="300",height="2",font="10")
heading.pack()

#text
text=Text(width="300",height=10)
text.pack()
#text.insert(END,"hello world")

#Textbox
ask_txt=StringVar()
ask=Entry(width="300",font="10",textvariable=ask_txt)
#ask.pack(padx=0, pady=15)
ask.place(y=250)

#button Clear
btn_cls=Button(screen,text="Clear",bg="red",width="8",height="2",command=btn_clear)
btn_cls.pack(side=LEFT,padx=10, pady=0)

#button submit
btn=Button(screen,text="submit",width="8",height="2",command=Btn_submit)
#btn.place(x=280,y=200)
btn.pack(side=RIGHT,padx=10, pady=0)


#==========================main loop==========================
screen.mainloop()
#==================================design-END===========================================
