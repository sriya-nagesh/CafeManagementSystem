#Sriya Nagesh
from tkinter import *
from tkinter import filedialog,messagebox
import random
import time

def reset():
    textReceipt.delete(1.0,END)
    numvanillamuffin.set('0')
    numchocolatecupcake.set('0')
    numredvelvetcake.set('0')
    numbananabread.set('0')
    numcheesecake.set('0')
    numcherrypie.set('0')
    numvolcanocake.set('0')
    numchocolatecookies.set('0')
    numpeanutbuttercookies.set('0')

    numearlgreytea.set('0')
    nummacchiato.set('0')
    numgreentea.set('0')
    numamericano.set('0')
    nummilkshake.set('0')
    numlatte.set('0')
    numwhitecoffee.set('0')
    numchamomiletea.set('0')
    numpepperminttea.set('0')

    costofdrinksvar.set('')
    costofdessertvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')

def save():
    if textReceipt.get(1.0,END)=='\n':
        pass
    else:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        if url==None:
            pass
        else:
            addReceipt=textReceipt.get(1.0,END)
            url.write(addReceipt)
            url.close()
            messagebox.showinfo('Status','Your receipt has been saved!')

def receipt():
    global Receiptnum,date
    if costofdessertvar.get() != '' or costofdrinksvar.get() != '':
        textReceipt.delete(1.0,END)
        x=random.randint(10,1000)
        Receiptnum='RECEIPT'+str(x)
        date=time.strftime('%d/%m/%Y')
        textReceipt.insert(END,'Order Reference:\t\t'+Receiptnum+'\t\t'+date+'\n')
        textReceipt.insert(END,'---------------------------------------------------------------\n')
        textReceipt.insert(END,'Order:\t\tPrice of order(RM)\t\tQuantity\n')
        textReceipt.insert(END,'---------------------------------------------------------------\n')
        if numchocolatecupcake.get()!='0':
            textReceipt.insert(END,f'Chocolate Cupcake\t\t\t{int(numchocolatecupcake.get())* 8}\t\t{int(numchocolatecupcake.get())}\n\n')

        if numvanillamuffin.get()!='0':
            textReceipt.insert(END,f'Vanilla Muffin\t\t\t{int(numvanillamuffin.get())* 4}\t\t{int(numvanillamuffin.get())}\n\n')

        if numbananabread.get()!='0':
            textReceipt.insert(END,f'Banana Bread\t\t\t{int(numbananabread.get())* 4}\t\t{int(numbananabread.get())}\n\n')

        if numcherrypie.get() != '0':
            textReceipt.insert(END, f'Cherry Pie:\t\t\t{int(numcherrypie.get()) * 12}\t\t{int(numcherrypie.get())}\n\n')

        if numredvelvetcake.get() != '0':
            textReceipt.insert(END, f'Red Velvet Cake:\t\t\t{int(numredvelvetcake.get()) * 12}\t\t{int(numredvelvetcake.get())}\n\n')

        if numchocolatecookies.get() != '0':
            textReceipt.insert(END, f'Chocolate Cookies:\t\t\t{int(numchocolatecookies.get()) * 15}\t\t{int(numchocolatecookies.get())}\n\n')

        if numcheesecake.get() != '0':
            textReceipt.insert(END, f'Cheesecake:\t\t\t{int(numcheesecake.get()) * 10}\t\t{int(numcheesecake.get())}\n\n')

        if numpeanutbuttercookies.get() != '0':
            textReceipt.insert(END, f'Peanut Butter Cookies:\t\t\t{int(numpeanutbuttercookies.get()) * 15}\t\t{int(numpeanutbuttercookies.get())}\n\n')

        if numvolcanocake.get() != '0':
            textReceipt.insert(END, f'Volcano Cake:\t\t\t{int(numvolcanocake.get()) * 15}\t\t{int(numvolcanocake.get())}\n\n')

        if numearlgreytea.get() != '0':
            textReceipt.insert(END, f'Earl Grey Tea:\t\t\t{int(numearlgreytea.get()) * 5}\t\t{int(numearlgreytea.get())}\n\n')

        if nummacchiato.get() != '0':
            textReceipt.insert(END, f'Macchiato:\t\t\t{int(nummacchiato.get()) * 9}\t\t{int(nummacchiato.get())}\n\n')

        if numgreentea.get() != '0':
            textReceipt.insert(END, f'Green Tea:\t\t\t{int(numgreentea.get()) * 5}\t\t{int(numgreentea.get())}\n\n')

        if nummilkshake.get() != '0':
            textReceipt.insert(END, f'Milkshake:\t\t\t{int(nummilkshake.get()) * 15}\t\t{int(nummilkshake.get())}\n\n')

        if numlatte.get() != '0':
            textReceipt.insert(END, f'Latte:\t\t\t{int(numlatte.get()) * 15}\t\t{int(numlatte.get())}\n\n')

        if numamericano.get() != '0':
            textReceipt.insert(END, f'Americano:\t\t\t{int(numamericano.get()) * 8}\t\t{int(numamericano.get())}\n\n')

        if numwhitecoffee.get() != '0':
            textReceipt.insert(END, f'White Coffee:\t\t\t{int(numwhitecoffee.get()) * 10}\t\t{int(numwhitecoffee.get())}\n\n')

        if numchamomiletea.get() != '0':
            textReceipt.insert(END, f'Chamomile Tea:\t\t\t{int(numchamomiletea.get()) * 5}\t\t{int(numchamomiletea.get())}\n\n')

        if numpepperminttea.get() != '0':
            textReceipt.insert(END, f'Peppermint Tea:\t\t\t{int(numpepperminttea.get()) * 5}\t\t{int(numpepperminttea.get())}\n\n')

        textReceipt.insert(END,'---------------------------------------------------------------\n')
        if costofdessertvar.get()!='RM 0':
            textReceipt.insert(END,f'Cost Of dessert\t\t\tRM{priceofdessert}\n\n')
        if costofdrinksvar.get() != 'RM 0':
            textReceipt.insert(END,f'Cost Of Drinks\t\t\tRM{priceofDrinks}\n\n')

        textReceipt.insert(END, f'Sub Total\t\t\tRM{subtotalofItems}\n\n')
        textReceipt.insert(END, f'SST\t\t\tRM{3}\n\n')
        textReceipt.insert(END, f'Total Cost\t\t\tRM{subtotalofItems+3}\n\n')
        textReceipt.insert(END,'---------------------------------------------------------------\n')

    else:
        messagebox.showerror('Error','Pick an item')

def calculate():
    global priceofdessert,priceofDrinks,subtotalofItems
    try:
        int(numchocolatecupcake.get())
        int(numvanillamuffin.get())
        int(numbananabread.get())
        int(numredvelvetcake.get())
        int(numcheesecake.get())
        int(numcherrypie.get())
        int(numvolcanocake.get())
        int(numchocolatecookies.get())
        int(numpeanutbuttercookies.get())

        int(numearlgreytea.get())
        int(nummacchiato.get())
        int(numgreentea.get())
        int(nummilkshake.get())
        int(numlatte.get())
        int(numamericano.get())
        int(numwhitecoffee.get())
        int(numchamomiletea.get())
        int(numpepperminttea.get())

        if int(numchocolatecupcake.get()) != 0 or int(numvanillamuffin.get()) != 0 or int(numbananabread.get()) != 0 or int(numredvelvetcake.get())!= 0 or int(numcheesecake.get()) != 0 or \
        int(numcherrypie.get()) != 0 or int(numvolcanocake.get()) != 0 or int(numchocolatecookies.get()) != 0 or int(numpeanutbuttercookies.get())!= 0 or int(numearlgreytea.get()) != 0 or\
        int(nummacchiato.get()) != 0 or int(numgreentea.get()) != 0 or int(nummilkshake.get()) != 0 or int(numlatte.get()) != 0 or int(numamericano.get()) != 0 or \
        int(numwhitecoffee.get()) != 0 or int(numchamomiletea.get()) != 0 or int(numpepperminttea.get()) != 0:

            item1=int(numchocolatecupcake.get())
            item2=int(numvanillamuffin.get())
            item3=int(numbananabread.get())
            item4=int(numredvelvetcake.get())
            item5=int(numcheesecake.get())
            item6=int(numcherrypie.get())
            item7=int(numvolcanocake.get())
            item8=int(numchocolatecookies.get())
            item9=int(numpeanutbuttercookies.get())

            item10=int(numearlgreytea.get())
            item11=int(nummacchiato.get())
            item12=int(numgreentea.get())
            item13=int(nummilkshake.get())
            item14=int(numlatte.get())
            item15=int(numamericano.get())
            item16=int(numwhitecoffee.get())
            item17=int(numchamomiletea.get())
            item18=int(numpepperminttea.get())

            priceofdessert=(item1*8)+(item2*4)+(item3*4)+(item4*12)+ (item5*10) + (item6 * 12) + (item7 * 15) + (item8 * 15) + (item9 * 15)
            priceofDrinks=(item10*5)+(item11*9)+ (item12 * 5) + (item13 * 15) + (item14 * 15) + (item15 * 8) + (item16 * 10) + (item17 * 5) + (item18 * 5)

            costofdessertvar.set('RM '+str(priceofdessert))
            costofdrinksvar.set('RM '+str(priceofDrinks))

            subtotalofItems=priceofdessert+priceofDrinks
            subtotalvar.set('RM '+str(subtotalofItems))

            servicetaxvar.set('RM 3 ')
            tottalcost=subtotalofItems+3
            totalcostvar.set('RM '+str(tottalcost))

        else:
            messagebox.showerror('No item selected','Please select an item')

    except:
        messagebox.showerror('Error','Please enter only numbers')
        reset()


root=Tk()

root.geometry('1290x690+30+0')

root.resizable(0,0)

root.title('Cafe Management System')

root.config(bg='#16191e',padx=30)

topFrame=Frame(root,relief=RIDGE,bg='#16191e',pady=15)
topFrame.pack(side=TOP)

labelTitle=Label(topFrame,text='Cafe Management System',font=('arial',30,'bold'),fg='lightgray',bg='#4f4e4f',width=45)
labelTitle.grid(row=0,column=0)

rightFrame=Frame(root,relief=FLAT,bg='#16191e')
rightFrame.pack(side=RIGHT)

totalsFrame=Frame(rightFrame,bd=4,relief=RIDGE,padx=30,pady=10,bg="#040401")
totalsFrame.pack(side=BOTTOM)

dessertFrame=LabelFrame(rightFrame,text='Dessert',font=('arial',20,'bold'),bd=5,relief=RIDGE,fg='#b98d74',padx=50,pady=30,bg="#040401")
dessertFrame.pack(side=RIGHT,fill="both", expand="yes")

drinksFrame=LabelFrame(rightFrame,text='Drinks',font=('arial',20,'bold'),bd=5,relief=RIDGE,fg='#b98d74',padx=50,pady=30,bg="#040401")
drinksFrame.pack(side=LEFT,fill="both", expand="yes")

leftFrame=Frame(root,relief=RIDGE,bg='#16191e',padx=20,pady=30)
leftFrame.pack(side=LEFT)

recieptFrame=Frame(leftFrame,bd=4,relief=RIDGE,bg='#4f4e4f')
recieptFrame.pack()

buttonFrame=Frame(leftFrame,bd=3,relief=RIDGE,bg='#4f4e4f')
buttonFrame.pack()

textReceipt=Text(recieptFrame,font=('arial',10,'bold'),bd=3,width=42,height=25, bg="darkgray",fg='#040401')
textReceipt.grid(row=0,column=0)

scrollbar=Scrollbar(recieptFrame,command=textReceipt.yview)
textReceipt['yscroll']=scrollbar.set
scrollbar.grid(row=0,column=2,sticky='ns')

#Variables
numchocolatecupcake=StringVar()
numvanillamuffin=StringVar()
numredvelvetcake = StringVar()
numcherrypie = StringVar()
numbananabread = StringVar()
numvolcanocake = StringVar()
numcheesecake = StringVar()
numpeanutbuttercookies = StringVar()
numchocolatecookies = StringVar()
numearlgreytea=StringVar()
nummacchiato = StringVar()
numgreentea = StringVar()
nummilkshake = StringVar()
numamericano = StringVar()
numlatte = StringVar()
numwhitecoffee = StringVar()
numchamomiletea = StringVar()
numpepperminttea = StringVar()

costofdessertvar=StringVar()
costofdrinksvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()

numchocolatecupcake.set('0')
numvanillamuffin.set('0')
numredvelvetcake.set('0')
numbananabread.set('0')
numcheesecake.set('0')
numcherrypie.set('0')
numvolcanocake.set('0')
numpeanutbuttercookies.set('0')
numchocolatecookies.set('0')
numearlgreytea.set('0')
nummacchiato.set('0')
numgreentea.set('0')
numamericano.set('0')
nummilkshake.set('0')
numlatte.set('0')
numwhitecoffee.set('0')
numchamomiletea.set('0')
numpepperminttea.set('0')

#checkbuttons for all fields
def Labels(name,frame,text,r):
    name=Label(frame,text=text,font=('arial',14,'bold'),fg='#b98d74',bg="#040401")
    name.grid(row=r,column=0)

Labels("chocolatecupcake",dessertFrame,"Chocolate Cupcake",0)
Labels("vanillamuffin",dessertFrame,"Vanilla Muffin",1)
Labels("bananabread",dessertFrame,"Banana Bread",2)
Labels("redvelvetcake",dessertFrame,"Red Velvet Cake",3)
Labels("cheesecake",dessertFrame,"Cheesecake",4)
Labels("cherrypie",dessertFrame,"Cherry Pie",5)
Labels("volcanocake",dessertFrame,"Volcano Cake",6)
Labels("chocolatecookies",dessertFrame,"Chocolate Cookies",7)
Labels("peanutbuttercookies",dessertFrame,"Peanut Butter Cookies",8)

Labels("earlgreytea",drinksFrame,"Earl Grey Tea",0)
Labels("macchiato",drinksFrame,"Macchiato",1)
Labels("greentea",drinksFrame,"Green Tea",2)
Labels("milkshake",drinksFrame,"Milkshake",3)
Labels("latte",drinksFrame,"Latte",4)
Labels("americano",drinksFrame,"Americano",5)
Labels("whitecoffee",drinksFrame,"White Coffee",6)
Labels("chamomiletea",drinksFrame,"Chamomile Tea",7)
Labels("pepperminttea",drinksFrame,"Peppermint Tea",8)

#Entries for all fields
def textboxes(name,frame,var,r):
    name=Entry(frame,font=('arial',18,'bold'),bd=1,width=6,textvariable=var)
    name.grid(row=r,column=1)

textboxes("textchocolatecupcake",dessertFrame,numchocolatecupcake,0)
textboxes("textvanillamuffin",dessertFrame,numvanillamuffin,1)
textboxes("textbananabread",dessertFrame,numbananabread,2)
textboxes("textredvelvetcake",dessertFrame,numredvelvetcake,3)
textboxes("textcheesecake",dessertFrame,numcheesecake,4)
textboxes("textcherrypie",dessertFrame,numcherrypie,5)
textboxes("textvolcanocake",dessertFrame,numvolcanocake,6)
textboxes("textchocolatecookies",dessertFrame,numchocolatecookies,7)
textboxes("textpeanutbuttercookies",dessertFrame,numpeanutbuttercookies,8)

textboxes("textearlgreytea",drinksFrame,numearlgreytea,0)
textboxes("textmacchiato",drinksFrame,nummacchiato,1)
textboxes("textgreentea",drinksFrame,numgreentea,2)
textboxes("textmilkshake",drinksFrame,nummilkshake,3)
textboxes("textlatte",drinksFrame,numlatte,4)
textboxes("textamericano",drinksFrame,numamericano,5)
textboxes("textwhitecoffee",drinksFrame,numwhitecoffee,6)
textboxes("textchamomiletea",drinksFrame,numchamomiletea,7)
textboxes("textpepperminttea",drinksFrame,numpepperminttea,8)

#labels for bottom row
def labels(name,text,r,c):
    name=Label(totalsFrame,text=text,font=('arial',14,'bold'),fg='#b98d74',bg="#040401")
    name.grid(row=r,column=c)

labels("labelCostofdessert","Dessert Total",0,0)
labels("labelCostofDrinks","Drinks Total",1,0)
labels("labelSubTotal","Total",0,2)
labels("labelServiceTax","Tax",1,2)
labels("labelTotalCost","Total after Tax",2,2)

#textboxes for bottom row
def text(name,variable,r,c):
    name=Entry(totalsFrame,font=('arial',16,'bold'),bd=2,width=14,state='readonly',textvariable=variable)
    name.grid(row=r,column=c,padx=41)

text("textCostofdessert",costofdessertvar,0,1)
text("textCostofDrinks",costofdrinksvar,1,1)
text("textubTotal",subtotalvar,0,3)
text("texterviceTax",servicetaxvar,1,3)
text("textTotalCost",totalcostvar,2,3)

#buttons below receipt
def btn(name,text,command,c):
    name=Button(buttonFrame,text=text,font=('arial',14,'bold'),fg='lightgray',bg='#4f4e4f',relief=FLAT,padx=5,command=command)
    name.grid(row=0,column=c)

btn("btn_total","Total",calculate,0)
btn("btn_receipt","Receipt",receipt,1)
btn("btn_save","Save",save,2)
btn("btn_reset","Reset",reset,3)

root.mainloop()