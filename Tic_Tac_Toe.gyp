from tkinter import *
from tkinter import font as tkFont
from tkmacosx import Button



root = Tk()
root.title("Tic Tac Toe")

def initia():
    global xo
    xo="X"
    ox="O's Turn."

    root.config(bg="LightSteelBlue1")
    myLabel.config(bg="LightSteelBlue1",fg="Black")
    demoLb.config(bg="LightSteelBlue1")

    btn_1.config(state = NORMAL)
    btn_2.config(state = NORMAL)
    btn_3.config(state = NORMAL)
    btn_4.config(state = NORMAL)
    btn_5.config(state = NORMAL)
    btn_6.config(state = NORMAL)
    btn_7.config(state = NORMAL)
    btn_8.config(state = NORMAL)
    btn_9.config(state = NORMAL)

    btn_1.config(text=" ")
    btn_2.config(text=" ")
    btn_3.config(text=" ")
    btn_4.config(text=" ")
    btn_5.config(text=" ")
    btn_6.config(text=" ")
    btn_7.config(text=" ")
    btn_8.config(text=" ")
    btn_9.config(text=" ")

    btn_1.config(bg="White")
    btn_2.config(bg="White")
    btn_3.config(bg="White")
    btn_4.config(bg="White")
    btn_5.config(bg="White")
    btn_6.config(bg="White")
    btn_7.config(bg="White")
    btn_8.config(bg="White")
    btn_9.config(bg="White")
    

    
    myLabel.config(text=ox)

def diableAllBtns():
    btn_1.config(state = DISABLED)
    btn_2.config(state = DISABLED)
    btn_3.config(state = DISABLED)
    btn_4.config(state = DISABLED)
    btn_5.config(state = DISABLED)
    btn_6.config(state = DISABLED)
    btn_7.config(state = DISABLED)
    btn_8.config(state = DISABLED)
    btn_9.config(state = DISABLED)

    btn_10.config(text="Reset")

def pressActivity(btnName):
    global xo
    
    
    if(xo=="O"):
        xo="X"
        ox="O's Turn."
    
    elif(xo=="X"):
        xo="O"
        ox="X's Turn."
    
    myLabel.config(text=ox)
    #yellow="yellow"
    if(btnName=="1"):
        if(xo=="X"):
            btn_1.config(bg="Yellow",fg="Black")
        elif(xo=="O"):
            btn_1.config(bg="Black",fg="Yellow")
        btn_1.config(text=xo,state = DISABLED)


    elif(btnName=="2"):
        if(xo=="X"):
            btn_2.config(bg="Yellow",fg="Black")
        elif(xo=="O"):
            btn_2.config(bg="Black",fg="Yellow")
        
        btn_2.config(text=xo,state = DISABLED)
    elif(btnName=="3"):
        if(xo=="X"):
            btn_3.config(bg="Yellow",fg="Black")
        elif(xo=="O"):
            btn_3.config(bg="Black",fg="Yellow")
        btn_3.config(text=xo,state = DISABLED)
    elif(btnName=="4"):
        if(xo=="X"):
            btn_4.config(bg="Yellow",fg="Black")
        elif(xo=="O"):
            btn_4.config(bg="Black",fg="Yellow")
        btn_4.config(text=xo,state = DISABLED)
    elif(btnName=="5"):
        if(xo=="X"):
            btn_5.config(bg="Yellow",fg="Black")
        elif(xo=="O"):
            btn_5.config(bg="Black",fg="Yellow")
        btn_5.config(text=xo,state = DISABLED)
    elif(btnName=="6"):
        if(xo=="X"):
            btn_6.config(bg="Yellow",fg="Black")
        elif(xo=="O"):
            btn_6.config(bg="Black",fg="Yellow")
        btn_6.config(text=xo,state = DISABLED)
    elif(btnName=="7"):
        if(xo=="X"):
            btn_7.config(bg="Yellow",fg="Black")
        elif(xo=="O"):
            btn_7.config(bg="Black",fg="Yellow")
        btn_7.config(text=xo,state = DISABLED)
    elif(btnName=="8"):
        if(xo=="X"):
            btn_8.config(bg="Yellow",fg="Black")
        elif(xo=="O"):
            btn_8.config(bg="Black",fg="Yellow")
        btn_8.config(text=xo,state = DISABLED)
    elif(btnName=="9"):
        if(xo=="X"):
            btn_9.config(bg="Yellow",fg="Black")
        elif(xo=="O"):
            btn_9.config(bg="Black",fg="Yellow")
        btn_9.config(text=xo,state = DISABLED)

    check4Win()



def check4Win():
    ##Horizontal
    if((btn_1.cget('text') == btn_2.cget('text') == btn_3.cget('text')=="X") or (btn_4.cget('text') == btn_5.cget('text') == btn_6.cget('text')=="X") or (btn_7.cget('text') == btn_8.cget('text') == btn_9.cget('text')=="X")):
        myLabel.config(text="X Won")
        diableAllBtns()
        root.config(bg="Yellow")
        demoLb.config(bg="Yellow")
        myLabel.config(bg="Yellow")

    elif((btn_1.cget('text') == btn_2.cget('text') == btn_3.cget('text')=="O") or (btn_4.cget('text') == btn_5.cget('text') == btn_6.cget('text')=="O") or (btn_7.cget('text') == btn_8.cget('text') == btn_9.cget('text')=="O")):
        myLabel.config(text="O Won")
        diableAllBtns()
        root.config(bg="Black")
        demoLb.config(bg="Black")
        myLabel.config(bg="Black",fg="Yellow")
    ##Vertical
    elif((btn_1.cget('text') == btn_4.cget('text') == btn_7.cget('text')=="X") or (btn_2.cget('text') == btn_5.cget('text') == btn_8.cget('text')=="X") or (btn_3.cget('text') == btn_6.cget('text') == btn_9.cget('text')=="X")):
        myLabel.config(text="X Won")
        diableAllBtns()
        root.config(bg="Yellow")
        demoLb.config(bg="Yellow")
        myLabel.config(bg="Yellow",fg="Black")

    elif((btn_1.cget('text') == btn_4.cget('text') == btn_7.cget('text')=="O") or (btn_2.cget('text') == btn_5.cget('text') == btn_8.cget('text')=="O") or (btn_3.cget('text') == btn_6.cget('text') == btn_9.cget('text')=="O")):
        myLabel.config(text="O Won")
        diableAllBtns()
        root.config(bg="Black")
        demoLb.config(bg="Black")
        myLabel.config(bg="Black",fg="Yellow")
    ##Diagonal
    elif((btn_1.cget('text') == btn_5.cget('text') == btn_9.cget('text')=="X") or (btn_3.cget('text') == btn_5.cget('text') == btn_7.cget('text')=="X")):
        myLabel.config(text="X Won")
        diableAllBtns()
        root.config(bg="Yellow")
        demoLb.config(bg="Yellow")
        myLabel.config(bg="Yellow",fg="Black")

    elif((btn_1.cget('text') == btn_5.cget('text') == btn_9.cget('text')=="O") or (btn_3.cget('text') == btn_5.cget('text') == btn_7.cget('text')=="O")):
        myLabel.config(text="O Won")
        diableAllBtns()
        root.config(bg="Black")
        demoLb.config(bg="Black")
        myLabel.config(bg="Black",fg="Yellow")
        
    
    ##CheckDraq
    elif(btn_1.cget('text') == " " or btn_2.cget('text') == " " or btn_3.cget('text') == " " or btn_4.cget('text') == " " or btn_5.cget('text') == " " or btn_6.cget('text') == " " or btn_7.cget('text') == " " or btn_8.cget('text') == " " or btn_9.cget('text') == " "):
        pass
    else:
        myLabel.config(text="Match Draw")
        diableAllBtns()
        root.config(bg="NavajoWhite2")
        demoLb.config(bg="NavajoWhite2")
        myLabel.config(bg="NavajoWhite2",fg="Black")
        


root.geometry("650x650")
myFont = tkFont.Font(family='Helvetica', size=20, weight=tkFont.BOLD)
myFont1 = tkFont.Font(family='Helvetica', size=40, weight=tkFont.BOLD)

myLabel = Label(root,text = "",font=myFont1)
myLabel.grid(row=0,column=1,columnspan=3)

btn_1 = Button(root, text=" ",padx=50,pady=50,font=myFont,state=DISABLED,command=lambda: pressActivity("1"))
btn_1.grid(row=1,column=1)

btn_2 = Button(root, text=" ",padx=50,pady=50,font=myFont,state=DISABLED,command=lambda: pressActivity("2"))
btn_2.grid(row=1,column=2)

btn_3 = Button(root, text=" ",padx=50,pady=50,font=myFont,state=DISABLED,command=lambda: pressActivity("3"))
btn_3.grid(row=1,column=3)


btn_4 = Button(root, text=" ",padx=50,pady=50,font=myFont,state=DISABLED,command=lambda: pressActivity("4"))
btn_4.grid(row=2,column=1)

btn_5 = Button(root, text=" ",padx=50,pady=50,font=myFont,state=DISABLED,command=lambda: pressActivity("5"))
btn_5.grid(row=2,column=2)

btn_6 = Button(root, text=" ",padx=50,pady=50,font=myFont,state=DISABLED,command=lambda: pressActivity("6"))
btn_6.grid(row=2,column=3)


btn_7 = Button(root, text=" ",padx=50,pady=50,font=myFont,state=DISABLED,command=lambda: pressActivity("7"))
btn_7.grid(row=3,column=1)

btn_8 = Button(root, text=" ",padx=50,pady=50,font=myFont,state=DISABLED,command=lambda: pressActivity("8"))
btn_8.grid(row=3,column=2)

btn_9 = Button(root, text=" ",padx=50,pady=50,font=myFont,state=DISABLED,command=lambda: pressActivity("9"))
btn_9.grid(row=3,column=3)

demoLb = Label(root,text = "",font=myFont1)
demoLb.grid(row=4,column=1,columnspan=3)
btn_10 = Button(root, text="Start",padx=50,pady=50,bg="Tomato",command=initia)
btn_10.grid(row=6,column=2)



root.mainloop()

