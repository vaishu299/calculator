from tkinter import *
import tkinter.font as font

expression = "" 

def add(a,b):
    return int(a + b)

def sub(a,b):
    return int(a - b)

def mul(a,b):
    return int(a * b)

def div(a,b):
    return a / b

def mod(a,b):
    return int(a % b)

def lcm(a,b):
    L = a if a>b else b
    while L <= a*b:
        if L%a == 0 and L%b == 0:
            return int(L)
        L+=1

def hcf(a,b):
    H = a if a<b else b
    while H >= 1:
        if a%H == 0 and b%H == 0:
            return int(H)
        H-=1

def extract_from_text(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l



def calculate():
    text = textin.get()

    for word in text.split(' '):
            
        if word in operations.keys():
            try:
                l = extract_from_text(text)
                r = operations[word](l[0] , l[1])
                e2.delete(0,END)
                e2.insert(END,r)
            except:
                e2.delete(0,END)
                e2.insert(END,'something went wrong please enter again')
            finally:
                break
        elif word not in operations.keys():
            e2.delete(0,END)
            e2.insert(END,'something went wrong please enter again')

       

operations = {'ADD':add , 'ADDITION':add , 'SUM':add , 'PLUS':add ,'add':add , 'addition':add , 'sum':add , 'plus':add , 
                'SUB':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,'sub':sub , 'difference':sub , 'minus':sub , 'subtract':sub, 
                'LCM':lcm , 'HCF':hcf ,'lcm':lcm , 'hcf':hcf ,'LOWEST COMMON MULTIPLE':lcm , 'HIGHEST COMMON FACTOR':hcf ,'lowest common multiple':lcm , 'highest common factor':hcf ,
                'PRODUCT':mul , 'MULTIPLICATION':mul,'MULTIPLY':mul ,'product':mul , 'multiplication':mul,'multiply':mul ,
                'DIVISION':div , 'DIV':div ,'DIVIDE':div,'division':div , 'div':div ,'divide':div,
                'MOD':mod ,'REMAINDER':mod , 'MODULUS':mod, 'mod':mod ,'remainder':mod , 'modulus':mod, 'absolute':mod ,'ABSOLUTE':mod ,
              '+':add , '-':sub , '*':mul ,'x':mul ,'X':mul , '/':div}



def open():
  
    def press(num): 
     
        global expression 
  
 
        expression = expression + str(num) 
  
     
        textin.set(expression) 
  
  
 
    def equalpress(): 
        try: 
  
            global expression 
  
            total = str(eval(expression)) 
  
            value.set(total) 
  
            expression = "" 
  
        except: 
  
            value.set(" something went wrong please enter again ") 
            expression = "" 

    def delete():
        textin.set(textin.get()[0:-1])
    
  
    def clear(): 
        global expression 
        expression = "" 
        textin.set("") 
        value.set("") 
          
    Fontz = font.Font(family='cooper black',size=12)
     
    button1 = Button(win, text=' 1\n one ', fg='white', bg='black',relief=RAISED,bd=8,activebackground='skyblue',activeforeground='black', 
                     command=lambda: press(1), height=2, width=8) 
    button1.place(x=10,y=365 ) 
    button1['font'] = Fontz
    
    button2 = Button(win, text=' 2\n two ', fg='white', bg='black',relief=RAISED,bd=8,activebackground='skyblue',activeforeground='black',
                     command=lambda: press(2), height=2, width=8) 
    button2.place(x=120,y=365 ) 
    button2['font'] = Fontz
    
    button3 = Button(win, text=' 3\n three ', fg='white', bg='black', relief=RAISED,bd=8,activebackground='skyblue',activeforeground='black',
                     command=lambda: press(3), height=2, width=8) 
    button3.place(x=230,y=365 )
    button3['font'] = Fontz
    
    add = Button(win, text=' +\n plus ', fg='white', bg='black', relief=RAISED,bd=8,activebackground='skyblue',activeforeground='black',
                     command=lambda: press('+'), height=2, width=8) 
    add.place(x=340,y=365)
    add['font'] = Fontz    

    button4 = Button(win, text=' 4\n four ', fg='white', bg='black', relief=RAISED,bd=8,activebackground='skyblue',activeforeground='black',
                     command=lambda: press(4), height=2, width=8) 
    button4.place(x=10,y=430 )
    button4['font'] = Fontz

    button5 = Button(win, text=' 5\n five ', fg='white', bg='black', relief=RAISED,bd=8,activebackground='skyblue',activeforeground='black',
                     command=lambda: press(5), height=2, width=8) 
    button5.place(x=120,y=430 )
    button5['font'] = Fontz

    button6 = Button(win, text=' 6\n six ', fg='white', bg='black', relief=RAISED,bd=8,activebackground='skyblue',activeforeground='black',
                     command=lambda: press(6), height=2, width=8) 
    button6.place(x=230,y=430 )
    button6['font'] = Fontz

    subtract = Button(win, text=' -\n minus ', fg='white', bg='black',relief=RAISED,bd=8,activebackground='skyblue',activeforeground='black', 
                     command=lambda: press('-'), height=2, width=8) 
    subtract.place(x=340,y=430 )
    subtract['font'] = Fontz

    
    button7 = Button(win, text=' 7\n seven ', fg='white', bg='black', relief=RAISED,bd=8,activebackground='skyblue',activeforeground='black',
                     command=lambda: press(7), height=2, width=8) 
    button7.place(x=10,y=495 )
    button7['font'] = Fontz

    button8 = Button(win, text=' 8\n eight ', fg='white', bg='black', relief=RAISED,bd=8,activebackground='skyblue',activeforeground='black',
                     command=lambda: press(8), height=2, width=8) 
    button8.place(x=120,y=495 )
    button8['font'] = Fontz

    button9 = Button(win, text=' 9\n nine ', fg='white', bg='black', relief=RAISED,bd=8,activebackground='skyblue',activeforeground='black',
                     command=lambda: press(9), height=2, width=8) 
    button9.place(x=230,y=495 )
    button9['font'] = Fontz

    multiply = Button(win, text=' *\n multiply', fg='white', bg='black', relief=RAISED,bd=8,activebackground='skyblue',activeforeground='black',
                     command=lambda: press('*'), height=2, width=8) 
    multiply.place(x=340,y=495 )
    multiply['font'] = Fontz


    button0 = Button(win, text=' 0\n zero', fg='white', bg='black', relief=RAISED,bd=8,activebackground='skyblue',activeforeground='black',
                     command=lambda: press(0), height=2, width=8) 
    button0.place(x=10,y=560 ) 
    button0['font'] = Fontz
    
    bracketopen = Button(win, text=' ( ', fg='white', bg='black', relief=RAISED,bd=8,activebackground='skyblue',activeforeground='black',
                     command=lambda: press('('), height=2, width=8) 
    bracketopen.place(x=120,y=560 ) 
    bracketopen['font'] = Fontz
    
    bracketclose = Button(win, text=' ) ', fg='white', bg='black', relief=RAISED,bd=8,activebackground='skyblue',activeforeground='black',
                     command=lambda: press(')'), height=2, width=8) 
    bracketclose.place(x=230,y=560 )
    bracketclose['font'] = Fontz

    divide = Button(win, text=' /\n divide ', fg='white', bg='black', relief=RAISED,bd=8,activebackground='skyblue',activeforeground='black',
                     command=lambda: press('/'), height=2, width=8) 
    divide.place(x=340,y=560 )
    divide['font'] = Fontz


    decimal = Button(win, text=' .\n decimal ', fg='white', bg='black', relief=RAISED,bd=8,activebackground='skyblue',activeforeground='black',
                     command=lambda: press('.'), height=2, width=8) 
    decimal.place(x=10,y=625 )
    decimal['font'] = Fontz

    delete = Button(win, text=' del ', fg='white', bg='black', relief=RAISED,bd=8,activebackground='skyblue',activeforeground='black',
                     command=delete, height=2, width=8) 
    delete.place(x=120,y=625)
    delete['font'] = Fontz

    equal = Button(win, text=' =\n equal ', fg='white', bg='black', relief=RAISED,bd=8,activebackground='skyblue',activeforeground='black',
                     command=equalpress, height=2, width=8) 
    equal.place(x=230,y=625 )
    equal['font'] = Fontz

    clear = Button(win, text=' clear ', fg='white', bg='black', relief=RAISED,bd=8,activebackground='skyblue',activeforeground='black',
                     command=clear, height=2, width=8) 
    clear.place(x=340,y=625 )
    clear['font'] = Fontz

def clear(): 
        global expression 
        expression = "" 
        textin.set("") 
        value.set("") 


win = Tk()
win.geometry('500x750')
win.resizable(0,0)
win.title('Smart Calci')
win.configure(bg='black')

Fontvalue = font.Font(family='ravie',size=13)

l1 = Label(win , text='I am a smart calculator',height=2,width=20 , padx=3,fg='white', bg='black')
l1.place(x=70,y=10)
l1['font'] = Fontvalue

style = font.Font(family='showcard gothic',size=13)

l2 = Label(win , text='My  name  is  Vaishnavi' ,height=2,width=20 ,padx=3,fg='white', bg='black')
l2.place(x=80,y=45)
l2['font'] = style

mystyle = font.Font(family='broadway',size=15)

l3 = Label(win , text='How  may  I  help  you ??' ,height=2,width=20, padx=3,fg='white', bg='black')
l3.place(x=65,y=83)
l3['font'] = mystyle

mine = font.Font(family='bahnschrift',size=13,weight='bold')

l4 = Label(win , text='for simple operations type "add 5 and 3" or  "multiply 6 and 7" \n in the below box  or for complex operations use the KEYPAD' ,fg='white', bg='black',height=4,width=54,justify= LEFT, padx=3)
l4.place(x=5,y=120)
l4['font'] = mine

styles = font.Font(family='bahnschrift',size=15,weight='bold')

textin = StringVar()
e1 = Entry(win , width=39 , textvariable = textin,fg='black', bg='white',bd=2,justify=CENTER,relief=RAISED)
e1.place(x=10,y=205)
e1['font'] = styles

value = StringVar()
e2 = Entry(win ,width=39,textvariable=value,fg='white', bg='black',bd=4,justify=CENTER,relief=RAISED )
e2.place(x=10,y=250)
e2['font'] = styles

myFont = font.Font(family='lucida calligraphy',size=12,weight='bold')

b1 = Button(win , text='GO !!' ,command=calculate,height=1, width=6,fg='white', bg='black',relief=RAISED,bd=5,activebackground='white',activeforeground='black',)
b1.place(x=10,y=300)
b1['font'] = myFont


clearall = Button(win, text=' Clear All ', fg='white', bg='black', relief=RAISED,bd=5,activebackground='white',activeforeground='black',
                     command=clear, height=1, width=8) 
clearall.place(x=140,y=300 )
clearall['font'] = myFont    


Fontstyle = font.Font(family='cooper black',size=12)
    
viewkeypad = Button(win, text=' VIEW  KEYPAD ', fg='white', bg='black', relief=RAISED,bd=5,activebackground='white',activeforeground='black',
                     command=open, height=1, width=14) 
viewkeypad.place(x=300,y=300 )
viewkeypad['font'] = Fontstyle

    
win.mainloop()
