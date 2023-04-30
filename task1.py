b1_price = 499.00
b2_price = 855.00
b3_price = 645.00
n1=int(input("Enter number of books1 you want: "))
n2=int(input("Enter number of books2 you want: "))
n3=int(input("Enter number of books3 you want: "))
s_total=b1_price*n1+b2_price*n2+b3_price*n3
gst=0.12
taxes=s_total*gst
delivery_charges=250.0
total_invoice=s_total+taxes+delivery_charges
print(s_total)
print(taxes)
print(total_invoice)
