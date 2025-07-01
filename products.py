# product.py
from tkinter import *

def product_form(window):
    global back_image
    product_frame = Frame(window, width=1070, height=567, bg='white')
    product_frame.place(x=200, y=100)

    # Make sure 'back.png' exists in the correct directory
    back_image = PhotoImage(file='back.png')  # Path to the back image
    back_button = Button(product_frame, image=back_image, bd=0, cursor='hand2', bg='white',
                         command=lambda: product_frame.place_forget())
    back_button.place(x=10, y=30)

    left_frame = Frame(product_frame, bg='white')
    left_frame.place(x=20, y=60)

    heading_label = Label(product_frame, text='Manage Category Details', font=('times new roman', 16, 'bold'),
                          bg='#0f4d7d', fg='white')
    heading_label.grid(row=0, column=0)


