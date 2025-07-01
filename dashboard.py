from tkinter import *
from employees import employee_form
from supplier import supplier_form
from category import category_form

from sales import sales_form
# Window Setup
window = Tk()
window.title('Dashboard')
window.geometry('1270x668+0+0')
window.resizable(False, False)
window.config(bg='white')

# Title
bg_Image = PhotoImage(file='inventory1.png')
titleLabel = Label(window, image=bg_Image, compound=LEFT, text='Inventory Management System',
                   font=('times new roman', 40, 'bold'), bg='#010c48', fg='white')
titleLabel.place(x=0, y=0, relwidth=1)

# Logout Button
logoutButton = Button(window, text='Logout', font=('times new roman', 20, 'bold'), fg='#010c48')
logoutButton.place(x=1100, y=10)

# Subtitle
subtitleLabel = Label(window, text='Welcome Admin \t\t Date:08-07-2025\t\t Time: 12:00:16 pm',
                      font=('times new roman', 15), bg='#4d636d', fg='white')
subtitleLabel.place(x=0, y=70, relwidth=1)

# Left Menu Frame
leftFrame = Frame(window, bg='white')
leftFrame.place(x=0, y=102, width=200, height=555)

# Left Menu Content
logoImage = PhotoImage(file='logo.png')
imageLabel = Label(leftFrame, image=logoImage, bg='white')
imageLabel.pack()

menuLabel = Label(leftFrame, text='Menu', font=('times new roman', 20), bg='#009688', fg='white')
menuLabel.pack(fill=X)

# Menu Buttons
employee_icon = PhotoImage(file='employee.png')
employee_button = Button(leftFrame, image=employee_icon, compound=LEFT, text=' Employees',
                         font=('times new roman', 20, 'bold'), anchor='w', padx=10,
                         command=lambda: employee_form(window))
employee_button.pack(fill=X)

supplier_icon = PhotoImage(file='supplier.png')
supplier_button = Button(leftFrame, image=supplier_icon, compound=LEFT, text=' Suppliers',
                         font=('times new roman', 20, 'bold'), anchor='w', padx=10,
                         command=lambda: supplier_form(window))
supplier_button.pack(fill=X)

category_icon = PhotoImage(file='category.png')
category_button = Button(leftFrame, image=category_icon, compound=LEFT, text=' Category',
                         font=('times new roman', 20, 'bold'), anchor='w', padx=10,
                         command=lambda: category_form(window))
category_button.pack(fill=X)
'''
product_icon = PhotoImage(file='product.png')
product_button = Button(leftFrame, image=product_icon, compound=LEFT, text=' Product',
                        font=('times new roman', 20, 'bold'), anchor='w', padx=10,command=lambda:product_form(window))
product_button.pack(fill=X)
'''
sales_icon = PhotoImage(file='sales.png')
sales_button = Button(leftFrame, image=sales_icon, compound=LEFT, text='  Sales',
                      font=('times new roman', 20, 'bold'), anchor='w', padx=10, command=lambda: sales_form(window))
sales_button.pack(fill=X)

exit_icon = PhotoImage(file='exit.png')
exit_button = Button(leftFrame, image=exit_icon, compound=LEFT, text='  Exit',
                     font=('times new roman', 20, 'bold'), anchor='w', padx=10,
                     command=window.destroy)
exit_button.pack(fill=X)

# Main Dashboard Widgets

# Total Employees Frame
emp_frame = Frame(window, bg='#2C3E50', bd=3, relief=RIDGE)
emp_frame.place(x=400, y=125, height=170, width=280)

total_emp_icon = PhotoImage(file='total_emp.png')
Label(emp_frame, image=total_emp_icon, bg='#2C3E50').pack(pady=10)
Label(emp_frame, text='Total Employees', bg='#2C3E50', fg='white', font=('times new roman', 15, 'bold')).pack()
Label(emp_frame, text='6', bg='#2C3E50', fg='white', font=('times new roman', 15, 'bold')).pack()

# Total Suppliers Frame
sup_frame = Frame(window, bg='#8E44AD', bd=3, relief=RIDGE)
sup_frame.place(x=800, y=125, height=170, width=280)

total_sup_icon = PhotoImage(file='total_sup.png')
Label(sup_frame, image=total_sup_icon, bg='#8E44AD').pack(pady=10)
Label(sup_frame, text='Total Suppliers', bg='#8E44AD', fg='white', font=('times new roman', 15, 'bold')).pack()
Label(sup_frame, text='5', bg='#8E44AD', fg='white', font=('times new roman', 15, 'bold')).pack()

# Total Categories Frame
cat_frame = Frame(window, bg='#27AE60', bd=3, relief=RIDGE)
cat_frame.place(x=400, y=310, height=170, width=280)

total_cat_icon = PhotoImage(file='total_cat.png')
Label(cat_frame, image=total_cat_icon, bg='#27AE60').pack(pady=10)
Label(cat_frame, text='Total Categories', bg='#27AE60', fg='white', font=('times new roman', 15, 'bold')).pack()
Label(cat_frame, text='7', bg='#27AE60', fg='white', font=('times new roman', 15, 'bold')).pack()

# Total Products Frame
'''
prod_frame = Frame(window, bg='#2980B9', bd=3, relief=RIDGE)
prod_frame.place(x=800, y=310, height=170, width=280)

total_prod_icon = PhotoImage(file='total_prod.png')
Label(prod_frame, image=total_prod_icon, bg='#2980B9').pack(pady=10)
Label(prod_frame, text='Total Products', bg='#2980B9', fg='white', font=('times new roman', 15, 'bold')).pack()
Label(prod_frame, text='0', bg='#2980B9', fg='white', font=('times new roman', 15, 'bold')).pack()
'''
# Total Sales Frame
sales_frame = Frame(window, bg='#E74C3C', bd=3, relief=RIDGE)
sales_frame.place(x=800, y=310, height=170, width=280)

total_sales_icon = PhotoImage(file='total_sales.png')
Label(sales_frame, image=total_sales_icon, bg='#E74C3C').pack(pady=10)
Label(sales_frame, text='Total Sales', bg='#E74C3C', fg='white', font=('times new roman', 15, 'bold')).pack()
Label(sales_frame, text='3', bg='#E74C3C', fg='white', font=('times new roman', 15, 'bold')).pack()

# Start Window
window.mainloop()
