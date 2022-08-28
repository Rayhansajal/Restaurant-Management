from tkinter import *

# Initialize TKinter

application = Tk()

# Windows Size
application.geometry('1120x550+0+0')

# Application title
application.title('Restaurant Management')

# Windows backgorund color
application.config(bg='burlywood2')

# Prevent from maximizing
application.resizable(False,False)

# Top Panel
top_panel = Frame(application, bd=1 , relief= FLAT)
top_panel.pack(side = TOP)

# Title Tag
title_tag = Label(top_panel, text='Invoicing System' , fg='azure4' ,
                  font=('Dosis' , 58), bg='burlywood1',width=27 )
title_tag.grid(row=0, column=0)

# Left Panel
left_panel = Frame(application, bd=1 , relief=FLAT)
left_panel.pack(side= LEFT)

# Cost Panel
cost_panel = Frame(left_panel , bd=1 , relief=FLAT,bg='azure4',padx=50)
cost_panel.pack(side= BOTTOM)

# Food Panel
food_panel = LabelFrame(left_panel,text='Food' , font=('Dosis',19,'bold'),
                        bd=1,relief=FLAT,fg='azure4')
food_panel.pack(side=LEFT)

# Drink Panel
drink_panel = LabelFrame(left_panel,text='Drink' , font=('Dosis',19,'bold'),
                        bd=1,relief=FLAT,fg='azure4')
drink_panel.pack(side=LEFT)

# Dessert Panel
dessert_panel = LabelFrame(left_panel,text='Dessert' , font=('Dosis',19,'bold'),
                        bd=1,relief=FLAT,fg='azure4')
dessert_panel.pack(side=LEFT)

# Right Panel
right_panel = Frame(application,bd=1 ,relief=FLAT)
right_panel.pack(side=RIGHT)

# Calculator Panel
calculator_panel = Frame(application,bd =1 , relief=FLAT,bg='burlywood1')
calculator_panel.pack()

# Invoice Panel
invoice_panel = Frame(application,bd =1 , relief=FLAT,bg='burlywood1')
invoice_panel.pack()

# buttons Panel
buttons_panel = Frame(application,bd =1 , relief=FLAT,bg='burlywood1')
buttons_panel.pack()

# Product List
food_list = ['Pizza' , 'Burger','Kabab','Salad' ,'Sandwich','Hot-dogs','Roll','Noodles']
drink_list = ['7up','Pepsi','Cocacola','Fanta','Sprite','Juice','Lemon','Soda']
dessert_list = ['Ice-cream','Cake','Fruit','Pudding','Cake2','Cake3','Cake4','Cake5']

# Create Food items
food_variables = []
food_box = []
food_text = []
counter = 0

# Create Chekcbuttons
for food in food_list:
    food_variables.append('')
    food_variables[counter] = IntVar()
    food = Checkbutton(food_panel,
                       text=food.title(),
                       font=('Dosis',19,'bold'),
                       onvalue=1,
                       offvalue=0,
                       variable= food_variables[counter])
    food.grid(row=counter ,
              column=0 ,
              sticky=W)

    # Create Input boxes
    food_box.append('')
    food_text.append('')
    food_text[counter] = StringVar()
    food_text[counter].set('0')
    food_box[counter] = Entry(food_panel,
                             font=('Dosis',18,'bold'),
                              bd=1,
                              width=6,
                              state=DISABLED,
                              textvariable=food_text[counter])
    food_box[counter].grid(row=counter,
                           column=1)

    counter +=1


# Create drink items
drink_variables = []
drink_box = []
drink_text = []
counter = 0
for drink in drink_list:
    drink_variables.append('')
    drink_variables[counter] = IntVar()
    drink = Checkbutton(drink_panel,
                        text=drink.title(),
                        font=('Dosis',19,'bold'),
                       onvalue=1,
                        offvalue=0,
                        variable= drink_variables[counter])
    drink.grid(row=counter ,
               column=0 ,
               sticky=W)
    # Create Input boxes
    drink_box.append('')
    drink_text.append('')
    drink_text[counter] = StringVar()
    drink_text[counter].set('0')
    drink_box[counter] = Entry(drink_panel,
                              font=('Dosis', 18, 'bold'),
                              bd=1,
                              width=6,
                              state=DISABLED,
                              textvariable=drink_text[counter])
    drink_box[counter].grid(row=counter,
                           column=1)

    counter +=1

# Create dessert items
dessert_variables = []
dessert_box = []
dessert_text = []
counter = 0
for dessert in dessert_list:
    dessert_variables.append('')
    dessert_variables[counter] = IntVar()
    dessert = Checkbutton(dessert_panel,
                          text=dessert.title(),
                          font=('Dosis',19,'bold'),
                       onvalue=1,
                          offvalue=0,
                          variable= dessert_variables[counter])
    dessert.grid(row=counter ,
                 column=0 ,
                 sticky=W)
    # Create Input boxes
    dessert_box.append('')
    dessert_text.append('')
    dessert_text[counter] = StringVar()
    dessert_text[counter].set('0')
    dessert_box[counter] = Entry(dessert_panel,
                              font=('Dosis', 18, 'bold'),
                              bd=1,
                              width=6,
                              state=DISABLED,
                              textvariable=dessert_text[counter])
    dessert_box[counter].grid(row=counter,
                           column=1)

    counter +=1


# Variables
food_cost_var = StringVar()
drink_cost_var = StringVar()
dessert_cost_var = StringVar()
subtotal_cost_var = StringVar()
taxes_cost_var = StringVar()
total_cost_var = StringVar()




# Cost Labels and input Fields
food_cost_label = Label(cost_panel,
                        text='Food Cost',
                        font=('Dosis',12,'bold'),
                        bg='azure4',
                        fg='white')
food_cost_label.grid(row=0,column=0)
food_cost_text = Entry(cost_panel,
                       font=('Dosis',12,'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=food_cost_var)
food_cost_text.grid(row=0,column=1,padx=41)

drink_cost_label = Label(cost_panel,
                        text='Drink Cost',
                        font=('Dosis',12,'bold'),
                        bg='azure4',
                        fg='white')
drink_cost_label.grid(row=1,column=0)
drink_cost_text = Entry(cost_panel,
                       font=('Dosis',12,'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=drink_cost_var)
drink_cost_text.grid(row=1,column=1,padx=41)

dessert_cost_label = Label(cost_panel,
                        text='Dessert Cost',
                        font=('Dosis',12,'bold'),
                        bg='azure4',
                        fg='white')
dessert_cost_label.grid(row=2,column=0)
dessert_cost_text = Entry(cost_panel,
                       font=('Dosis',12,'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=dessert_cost_var)
dessert_cost_text.grid(row=2,column=1,padx=41)

subtotal_cost_label = Label(cost_panel,
                        text='Subtotal',
                        font=('Dosis',12,'bold'),
                        bg='azure4',
                        fg='white')
subtotal_cost_label.grid(row=0,column=2,padx=41)
subtotal_cost_text = Entry(cost_panel,
                       font=('Dosis',12,'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=subtotal_cost_var)
subtotal_cost_text.grid(row=0,column=3)

taxes_cost_label = Label(cost_panel,
                        text='Taxes',
                        font=('Dosis',12,'bold'),
                        bg='azure4',
                        fg='white')
taxes_cost_label.grid(row=1,column=2)
taxes_cost_text = Entry(cost_panel,
                       font=('Dosis',12,'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=taxes_cost_var)
taxes_cost_text.grid(row=1,column=3,padx=41)

total_cost_label = Label(cost_panel,
                        text='Total Cost',
                        font=('Dosis',12,'bold'),
                        bg='azure4',
                        fg='white')
total_cost_label.grid(row=2,column=2)
total_cost_text = Entry(cost_panel,
                       font=('Dosis',12,'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=total_cost_var)
total_cost_text.grid(row=2,column=3,padx=41)

# Buttons
buttons = ['total','invoice','save','reset']
column = 0
for button in buttons:
    button = Button(buttons_panel,
                    text=button.title(),
                    font=('Dosis',14,'bold'),
                    fg='white',
                    bg='azure4',
                    bd=1,
                    width=8)
    button.grid(row=0 ,column=column)
    column +=1

# Invoice
invoice_text = Text(invoice_panel,
                    font=('Dosis',12,'bold'),
                    bd=1,
                    height=12.49,
                    width=45)
invoice_text.grid(row=0,column=0)

# Calculator
calculator_display = Entry(calculator_panel,
                           font=('Dosis',16,'bold'),
                           width=30,
                           bd=1)
calculator_display.grid(row=0,column=0,columnspan=4)

calculator_buttons = ['7','8','9','+',
                      '4','5','6','-',
                      '1','2','3','x',
                      'CE','Delete','0','/']
my_row = 1
my_column = 0

for button in calculator_buttons:
    button= Button(calculator_panel,
                   text=button.title(),
                   font=('Dosis',14,'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=8)
    button.grid(row=my_row, column=my_column)
    if my_column == 3:
        my_row += 1
    my_column +=1

    if my_column == 4:
        my_column = 0

# Prevent windows from closing
application.mainloop()