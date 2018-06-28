import tkinter
from tkinter import *
import time
import random

tk = tkinter.Tk()
tk.geometry("1600x800+0+0")
tk.title("Restaurant Management")

frame1 = Frame(tk, width = 1600, height = 50,relief = SUNKEN)
frame1.pack(side = TOP)

frame2 = Frame(tk, width = 800, height = 700,relief = SUNKEN)
frame2.pack(side = RIGHT)
frame3 = Frame(tk, width = 800, height = 700,relief = SUNKEN)
frame3.pack(side = LEFT)

time1 = time.asctime()
lbl1 = Label(frame1, font = ("Arial",65,"bold"), text = "Restaurant Management System", bd = 10, anchor = "e")
lbl1.grid(row = 0, column = 0)
lbl2 = Label(frame1, font = ("Arial",35,"bold"), text = time1, bd = 10, anchor = "e")
lbl2.grid(row=1, column = 0)
                                                        #CALCULATOR
#click the numbers and operators in the calculator
def click(numbers):
    global operator
    operator = operator + str(numbers)
    input.set(operator)

#clears the screen
def clear():
    global operator
    operator= ""
    input.set("")

#shows the result
def equal():
    global operator
    result = str(eval(operator))
    input.set(result)
    operator = ""

tk.title("Calculator")
operator = ""
input = StringVar()

display = Entry(frame2,textvariable =input,font = ("arial", 20, "bold"), bd = 30, insertwidth = 5, justify = "right").grid(columnspan = 45)

bt15 = Button(frame2, bd= 10, padx = 26, pady = 5, font = ("arial", 15, "bold"), text = "(", width = 1, height = 2, bg = "grey" , command = lambda:click("(")).grid(column = 0, row = 1)
bt16 = Button(frame2, bd= 10, padx = 26, pady = 5, font = ("arial", 15, "bold"),text = ")", width = 1, height = 2, bg = "grey", command = lambda:click(")")).grid(column = 1, row = 1)
bt17 = Button(frame2, bd= 10, padx = 26, pady = 5, font = ("arial", 15, "bold"), text = "%", width = 1, height = 2, bg = "grey",command = lambda: click("%")).grid(column = 2, row = 1)
bt18 = Button(frame2, bd= 10, padx = 26, pady = 5, font = ("arial", 15, "bold"), text = "C", width = 1, height = 2, bg = "grey",command = lambda:clear()).grid(column = 3, row = 1)

bt1 = Button(frame2, bd= 10, padx = 26, pady = 5, font = ("arial", 15, "bold"), text = "7", width = 1, height = 2,bg = "grey", command = lambda:click(7)).grid(column = 0, row = 2)
bt2 = Button(frame2, bd= 10, padx = 26, pady = 5, font = ("arial", 15, "bold"), text = "8", width = 1, height = 2,bg = "grey",command = lambda:click(8)).grid(column = 1, row = 2)
bt3 = Button(frame2, bd= 10, padx = 26, pady = 5, font = ("arial", 15, "bold"), text = "9", width = 1, height = 2,bg = "grey", command = lambda:click(9)).grid(column = 2, row = 2)
bt1 = Button(frame2, bd= 10, padx = 26, pady = 5, font = ("arial", 15, "bold"), text = "/", width = 1, height = 2,bg = "grey", command = lambda:click("/")).grid(column = 3, row = 2)

bt4 = Button(frame2, bd= 10, padx = 26, pady = 5, font = ("arial", 15, "bold"), text = "6", width = 1, height = 2, bg = "grey",command = lambda:click(6)).grid(column = 0, row = 3)
bt5 = Button(frame2, bd= 10, padx = 26, pady = 5, font = ("arial", 15, "bold"), text = "5", width = 1, height = 2, bg = "grey",command = lambda:click(5)).grid(column = 1, row = 3)
bt6 = Button(frame2, bd= 10, padx = 26, pady = 5, font = ("arial", 15, "bold"), text = "4", width = 1, height = 2, bg = "grey",command = lambda:click(4)).grid(column = 2, row = 3)
bt1 = Button(frame2, bd= 10, padx = 26, pady = 5, font = ("arial", 15, "bold"), text = "*", width = 1, height = 2, bg = "grey",command = lambda:click("*")).grid(column = 3, row = 3)

bt7 = Button(frame2, bd= 10, padx = 26, pady = 5, font = ("arial", 15, "bold"), text = "3", width = 1, height = 2,bg = "grey", command = lambda:click(3)).grid(column = 0, row = 4)
bt8 = Button(frame2, bd= 10, padx = 26, pady = 5, font = ("arial", 15, "bold"), text = "2", width = 1, height = 2,bg = "grey", command = lambda:click(2)).grid(column = 1, row = 4)
bt9 = Button(frame2, bd= 10, padx = 26, pady = 5, font = ("arial", 15, "bold"), text = "1", width = 1, height = 2,bg = "grey", command = lambda:click(1)).grid(column = 2, row = 4)
bt10 = Button(frame2, bd= 10, padx = 26, pady = 5, font = ("arial", 15, "bold"), text = "-", width = 1, height = 2,bg = "grey", command = lambda:click("-")).grid(column = 3, row = 4)

bt11 = Button(frame2, bd= 10, padx = 26, pady = 5, font = ("arial", 15, "bold"), text = "0", width = 1, height = 2, bg = "grey",command = lambda:click(0)).grid(column = 0, row = 5)
bt12 = Button(frame2, bd= 10, padx = 26, pady = 5, font = ("arial", 15, "bold"), text = ".", width = 1, height = 2, bg = "grey",command = lambda:click(".")).grid(column = 1, row = 5)
bt13 = Button(frame2, bd= 10, padx = 26, pady = 5, font = ("arial", 15, "bold"), text = "=", width = 1, height = 2, bg = "grey",command = lambda:equal()).grid(column = 2, row = 5)
bt14 = Button(frame2, bd= 10, padx = 26, pady = 5, font = ("arial", 15, "bold"), text = "+", width = 1, height = 2, bg = "grey",command = lambda:click("+")).grid(column = 3, row = 5)

                                        # ADDING ITEMS IN FIRST COLUMN
empty = StringVar()
lbl1 = Label(frame3, font=('arial', 16, 'bold'), text="Reference", bd=16, anchor='w')
lbl1.grid(row=0, column=0)
display1 = Entry(frame3, font=('arial', 16, 'bold'), textvariable=empty, bd=10, insertwidth=4, justify='right')
display1.grid(row=0, column=1)

empty1 = StringVar()
lbl2 = Label(frame3, font=('arial', 16, 'bold'), text="Burger", bd=16, anchor='w')
lbl2.grid(row=1, column=0)
display2 = Entry(frame3, font=('arial', 16, 'bold'), textvariable=empty1, bd=10, insertwidth=4, justify='right')
display2.grid(row=1, column=1)

empty2 = StringVar()
lbl3 = Label(frame3, font=('arial', 16, 'bold'), text="Pastry", bd=16, anchor='w')
lbl3.grid(row=2, column=0)
display3 = Entry(frame3, font=('arial', 16, 'bold'), textvariable=empty2, bd=10, insertwidth=4, justify='right')
display3.grid(row=2, column=1)

empty3 = StringVar()
lbl4 = Label(frame3, font=('arial', 16, 'bold'), text="Maggi", bd=16, anchor='w')
lbl4.grid(row=3, column=0)
display4 = Entry(frame3, font=('arial', 16, 'bold'), textvariable=empty3, bd=10, insertwidth=4, justify='right')
display4.grid(row=3, column=1)

empty4 = StringVar()
lbl5 = Label(frame3, font=('arial', 16, 'bold'), text="Appy/Frooti", bd=16, anchor='w')
lbl5.grid(row=4, column=0)
display5 = Entry(frame3, font=('arial', 16, 'bold'), textvariable=empty4, bd=10, insertwidth=4, justify='right')
display5.grid(row=4, column=1)

empty5 = StringVar()
lbl6 = Label(frame3, font=('arial', 16, 'bold'), text="Idli", bd=16, anchor='w')
lbl6.grid(row=5, column=0)
display6 = Entry(frame3, font=('arial', 16, 'bold'), textvariable=empty5, bd=10, insertwidth=4, justify='right')
display6.grid(row=5, column=1)

                                            # ADDING ITEMS IN SECOND COLUMN
empty6 = StringVar()
lbl7 = Label(frame3, font=('arial', 16, 'bold'), text="Carbonated Drinks", bd=16, anchor='w')
lbl7.grid(row=0, column=2)
display7 = Entry(frame3, font=('arial', 16, 'bold'), textvariable=empty6, bd=10, insertwidth=4, justify='right')
display7.grid(row=0, column=3)

empty7 = StringVar()
lbl8 = Label(frame3, font=('arial', 16, 'bold'), text="Pav Bhaji", bd=16, anchor='w')
lbl8.grid(row=1, column=2)
display8 = Entry(frame3, font=('arial', 16, 'bold'), textvariable=empty7, bd=10, insertwidth=4, justify='right')
display8.grid(row=1, column=3)

empty8 = StringVar()
lbl9 = Label(frame3, font=('arial', 16, 'bold'), text="Sweets", bd=16, anchor='w')
lbl9.grid(row=2, column=2)
display9 = Entry(frame3, font=('arial', 16, 'bold'), textvariable=empty8, bd=10, insertwidth=4, justify='right')
display9.grid(row=2, column=3)

empty9 = StringVar()
lbl10 = Label(frame3, font=('arial', 16, 'bold'), text="Tax", bd=16, anchor='w')
lbl10.grid(row=3, column=2)
display10 = Entry(frame3, font=('arial', 16, 'bold'), textvariable=empty9, bd=10, insertwidth=4, justify='right')
display10.grid(row=3, column=3)

empty10 = StringVar()
lbl11 = Label(frame3, font=('arial', 16, 'bold'), text="Sub Total", bd=16, anchor='w')
lbl11.grid(row=4, column=2)
display11 = Entry(frame3, font=('arial', 16, 'bold'), textvariable=empty10, bd=10, insertwidth=4, justify='right')
display11.grid(row=4, column=3)

empty11 = StringVar()
lbl12 = Label(frame3, font=('arial', 16, 'bold'), text="Total Cost", bd=16, anchor='w')
lbl12.grid(row=5, column=2)
display12 = Entry(frame3, font=('arial', 16, 'bold'), textvariable=empty11, bd=10, insertwidth=4, justify='right')
display12.grid(row=5, column=3)

def clear_it():
    empty.set("")
    empty1.set("")
    empty2.set("")
    empty3.set("")
    empty4.set("")
    empty5.set("")
    empty6.set("")
    empty7.set("")
    empty8.set("")
    empty9.set("")
    empty10.set("")
    empty11.set("")

def total_it():
    x = random.randint(2500,7000)
    random_reference = str(x)
    empty.set(random_reference)

    cost1 = float(empty1.get())
    cost2 = float(empty2.get())
    cost3 = float(empty3.get())
    cost4 = float(empty4.get())
    cost5 = float(empty5.get())
    cost6 = float(empty6.get())
    cost7 = float(empty7.get())
    cost8 = float(empty8.get())

    cost1 = cost1 * 30
    cost2 = cost2 * 35
    cost3 = cost3 * 20
    cost4 = cost4 * 10
    cost5 = cost5 * 30
    cost6 = cost6 * 40
    cost7 = cost7 * 50
    cost8 = cost8 * 30

    totalcost = (cost1 + cost2 + cost3 + cost4 + cost5 + cost6 + cost7 + cost8)
    totaltax = ((cost1 + cost2 + cost3 + cost4 + cost5 + cost6 + cost7 + cost8) * 0.05)
    total = (totaltax + totalcost)
    empty9.set(totaltax)
    empty10.set(totalcost)
    empty11.set(total)

                                                 #BUTTONS
button1 = Button(frame3, font = ("arial", 16, "bold"), text = "Clear", bd = 12, padx = 45, pady = 16, command = clear_it)
button1.grid(row = 7, column = 1)

button2 = Button(frame3, font = ("arial", 16, "bold"), text = "Total", bd = 12, padx = 45, pady = 16, command = total_it)
button2.grid(row = 7, column = 2)

button3 = Button(frame3, font = ("arial", 16, "bold"), text = "Exit", bd = 12, padx = 45, pady = 16, command = tk.destroy)
button3.grid(row = 7, column = 3)

tk.mainloop()