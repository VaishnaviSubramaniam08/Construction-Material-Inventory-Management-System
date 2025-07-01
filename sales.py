from tkinter import *
from tkinter import ttk, messagebox, filedialog
import qrcode
import csv
import os
from PIL import Image, ImageTk

from datetime import datetime
sales_data = []

def sales_form(parent):
    # Create a frame for sales form
    sales_frame = Frame(parent, width=1070, height=567, bg='white')
    sales_frame.place(x=200, y=100)

    # Load the back image
    back_image = PhotoImage(file='back.png')  # Path to the back image

    # Create the back button with the image
    back_button = Button(sales_frame, image=back_image, bd=0, cursor='hand2', bg='white',
                         command=lambda: sales_frame.place_forget())  # Close the sales form
    back_button.place(x=10, y=30)
    back_button.image = back_image  # Keep reference to avoid garbage collection

    # Clear previous widgets
    for widget in parent.winfo_children():
        widget.destroy()

    # --- Variables ---
    product_name = StringVar()
    quantity_sold = StringVar()
    product_price = StringVar()

    # --- Functions ---
    def add_sale():
        product = product_name.get()
        quantity = quantity_sold.get()
        price = product_price.get()

        if product == '' or quantity == '' or price == '':
            messagebox.showerror('Error', 'All fields are required!', parent=parent)
            return

        try:
            quantity = int(quantity)
            price = float(price)
            total = quantity * price

            sales_data.append([product, quantity, f"{price:.2f}", f"{total:.2f}"])
            update_table()
            clear_fields()
            generate_qr(product, quantity, total)
        except ValueError:
            messagebox.showerror('Error', 'Invalid quantity or price!', parent=parent)

    def update_table():
        sales_table.delete(*sales_table.get_children())
        for row in sales_data:
            sales_table.insert('', END, values=row)

    def clear_fields():
        product_name.set('')
        quantity_sold.set('')
        product_price.set('')
        qr_label.config(image='')

    def export_data():
        if not sales_data:
            messagebox.showerror('Error', 'No data to export!', parent=parent)
            return
        file_path = filedialog.asksaveasfilename(defaultextension='.csv',
                                                 filetypes=[('CSV Files', '*.csv')],
                                                 title='Save Report')
        if file_path:
            with open(file_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Product Name', 'Quantity Sold', 'Unit Price (₹)', 'Total Amount (₹)'])
                writer.writerows(sales_data)
            messagebox.showinfo('Success', 'Data exported successfully!', parent=parent)

    def generate_qr(product, quantity, total):
        data = f"Product: {product}\nQuantity: {quantity}\nTotal: ₹{total:.2f}"
        qr = qrcode.make(data)

        if not os.path.exists('QR'):
            os.makedirs('QR')

        qr_path = f'QR/{product}_qr.png'
        qr.save(qr_path)

        qr_img = Image.open(qr_path)
        qr_img = qr_img.resize((150, 150))
        qr_photo = ImageTk.PhotoImage(qr_img)
        qr_label.config(image=qr_photo)
        qr_label.image = qr_photo

    def generate_invoice():
        if not sales_data:
            messagebox.showerror('Error', 'No data to generate invoice!', parent=parent)
            return

        # Get current date and time
        now = datetime.now()
        timestamp = now.strftime("%d-%m-%Y %H:%M:%S")

        invoice_text = f"==== Invoice ====\nDate & Time: {timestamp}\n\n"
        grand_total = 0
        for item in sales_data:
            invoice_text += f"Product: {item[0]}, Quantity: {item[1]}, Unit Price: ₹{item[2]}, Total: ₹{item[3]}\n"
            grand_total += float(item[3])

        invoice_text += f"\nGrand Total: ₹{grand_total:.2f}\n"

        invoice_window = Toplevel(parent)
        invoice_window.title("Invoice")
        invoice_window.geometry("400x400")

        invoice_box = Text(invoice_window, font=('times new roman', 15))
        invoice_box.pack(expand=True, fill=BOTH)
        invoice_box.insert(END, invoice_text)

        Button(invoice_window, text="Save Invoice", font=('times new roman', 14, 'bold'),
               command=lambda: save_invoice(invoice_text)).pack(pady=10)

    def save_invoice(content):
        file_path = filedialog.asksaveasfilename(defaultextension='.txt',
                                                 filetypes=[('Text Files', '*.txt')],
                                                 title='Save Invoice')
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            messagebox.showinfo('Success', 'Invoice saved successfully!', parent=parent)

    # --- GUI Elements ---

    title = Label(parent, text='Sales Page', font=('times new roman', 30, 'bold'), bg='#262626', fg='white')
    title.pack(side=TOP, fill=X)

    entry_frame = Frame(parent, bg='white', bd=2, relief=RIDGE)
    entry_frame.place(x=20, y=80, width=400, height=200)

    Label(entry_frame, text='Product Name', font=('times new roman', 20, 'bold'), bg='white').grid(row=0, column=0, padx=10, pady=10, sticky='w')
    Entry(entry_frame, textvariable=product_name, font=('times new roman', 15), bg='lightyellow').grid(row=0, column=1, padx=10, pady=10)

    Label(entry_frame, text='Quantity Sold', font=('times new roman', 20, 'bold'), bg='white').grid(row=1, column=0, padx=10, pady=10, sticky='w')
    Entry(entry_frame, textvariable=quantity_sold, font=('times new roman', 15), bg='lightyellow').grid(row=1, column=1, padx=10, pady=10)

    Label(entry_frame, text='Product Price (₹)', font=('times new roman', 20, 'bold'), bg='white').grid(row=2, column=0, padx=10, pady=10, sticky='w')
    Entry(entry_frame, textvariable=product_price, font=('times new roman', 15), bg='lightyellow').grid(row=2, column=1, padx=10, pady=10)

    btn_frame = Frame(parent, bg='white')
    btn_frame.place(x=20, y=300, width=400, height=120)

    Button(btn_frame, text='Add Sale', font=('times new roman', 18, 'bold'), bg='#4caf50', fg='white', command=add_sale).grid(row=0, column=0, padx=10, pady=10, sticky="ew")
    Button(btn_frame, text='Export CSV', font=('times new roman', 18, 'bold'), bg='#2196f3', fg='white', command=export_data).grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    Button(btn_frame, text='Generate Invoice', font=('times new roman', 18, 'bold'), bg='#ff5722', fg='white', command=generate_invoice).grid(row=1, column=0, columnspan=2, pady=10, sticky="ew")

    global qr_label
    qr_label = Label(parent, bg='white')
    qr_label.place(x=450, y=80, width=200, height=200)

    sales_frame = Frame(parent, bd=2, relief=RIDGE)
    sales_frame.place(x=700, y=80, width=580, height=370)

    scroll_x = Scrollbar(sales_frame, orient=HORIZONTAL)
    scroll_y = Scrollbar(sales_frame, orient=VERTICAL)

    global sales_table
    sales_table = ttk.Treeview(sales_frame, columns=('product', 'quantity', 'unit_price', 'total'),
                               xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_x.config(command=sales_table.xview)
    scroll_y.config(command=sales_table.yview)

    sales_table.heading('product', text='Product')
    sales_table.heading('quantity', text='Quantity')
    sales_table.heading('unit_price', text='Unit Price (₹)')
    sales_table.heading('total', text='Total (₹)')
    sales_table['show'] = 'headings'

    sales_table.column('product', width=150)
    sales_table.column('quantity', width=80)
    sales_table.column('unit_price', width=100)
    sales_table.column('total', width=100)

    sales_table.pack(fill=BOTH, expand=1)
