#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tkinter as tk
window=tk.Tk()
window.geometry("900x650")
window.title("APP Week 4 SET 5")
#Title
tk.Label(window, text='CAR RENTAL RECEIPT', font=('bold')).grid(row=0,column=2)
tk.Label(window, text=' ').grid(row=1,column=0)

#Receipt
tk.Label(window, text='Date:').grid(row=2,column=0)
tk.Entry(window).grid(row=2,column=1)
tk.Label(window, text='Receipt #:').grid(row=3,column=0)
tk.Entry(window).grid(row=3,column=1)

#Rental Company Info
tk.Label(window, text='Rental Company Info:', font=('bold')).grid(row=4,column=0)
tk.Label(window, text='Company:').grid(row=5,column=0)
tk.Entry(window).grid(row=5,column=1)
tk.Label(window, text='Representative:').grid(row=6,column=0)
tk.Entry(window).grid(row=6,column=1)
tk.Label(window, text='Location:').grid(row=7,column=0)
tk.Entry(window).grid(row=7,column=1)
tk.Label(window, text='City/State/ZIP:').grid(row=8,column=0)
tk.Entry(window).grid(row=8,column=1)
tk.Label(window, text='Phone:').grid(row=9,column=0)
tk.Entry(window).grid(row=9,column=1)

#Lessee Info
tk.Label(window, text='Lessee Info', font=('bold')).grid(row=4,column=2)
tk.Label(window, text='Name:').grid(row=5,column=2)
tk.Entry(window).grid(row=5,column=3)
tk.Label(window, text='License #:').grid(row=6,column=2)
tk.Entry(window).grid(row=6,column=3)
tk.Label(window, text='Address:').grid(row=7,column=2)
tk.Entry(window).grid(row=7,column=3)
tk.Label(window, text='City/State/ZIP:').grid(row=8,column=2)
tk.Entry(window).grid(row=8,column=3)
tk.Label(window, text='Phone:').grid(row=9,column=2)
tk.Entry(window).grid(row=9,column=3)
tk.Label(window, text=' ').grid(row=10,column=0)

#Vehicle Info
tk.Label(window, text='Vehicle Information', font=('bold')).grid(row=11,column=2)
tk.Label(window, text='VIN:').grid(row=12,column=0)
tk.Entry(window).grid(row=12,column=1)
tk.Label(window, text='Make:').grid(row=13,column=0)
tk.Entry(window).grid(row=13,column=1)
tk.Label(window, text='Year:').grid(row=14,column=0)
tk.Entry(window).grid(row=14,column=1)
tk.Label(window, text='Color:').grid(row=15,column=0)
tk.Entry(window).grid(row=15,column=1)
tk.Label(window, text='Registration #:').grid(row=12,column=2)
tk.Entry(window).grid(row=12,column=3)
tk.Label(window, text='Model:').grid(row=13,column=2)
tk.Entry(window).grid(row=13,column=3)
tk.Label(window, text='Mileage:').grid(row=14,column=2)
tk.Entry(window).grid(row=14,column=3)
tk.Label(window, text=' ').grid(row=16,column=0)

#Table
tk.Label(window, text='VIN', bd=1, relief='solid').grid(row=17,column=0,sticky='nsew')
tk.Label(window, text='Cost/Day', bd=1, relief='solid').grid(row=17,column=1,sticky='nsew')
tk.Label(window, text='# of Days', bd=1, relief='solid').grid(row=17,column=2,sticky='nsew')
tk.Label(window, text='Additional Costs', bd=1, relief='solid').grid(row=17,column=3,sticky='nsew')
tk.Label(window, text='Line Total', bd=1, relief='solid').grid(row=17,column=4,sticky='nsew')

for i in range(18,21):
    for j in range(0,5):
        tk.Entry(window, bd=1, relief='solid').grid(row=i,column=j,sticky='nesw')
tk.Label(window, text='Payment Method:').grid(row=21,column=0)
tk.Checkbutton(window,text='Cash    :').grid(row=22,column=0)
tk.Checkbutton(window,text='Check#  :').grid(row=22,column=1)
tk.Entry(window).grid(row=22,column=2)
tk.Checkbutton(window,text='Credit# :').grid(row=23,column=0)
tk.Entry(window).grid(row=23,column=1)
tk.Checkbutton(window,text='Other   :').grid(row=24,column=0)
tk.Entry(window).grid(row=24,column=1)

for i in range(21,25):
    tk.Entry(window, bd=1, relief='solid').grid(row=i,column=4,sticky='nesw')
text1=tk.StringVar()
text2=tk.StringVar()
text3=tk.StringVar()
text4=tk.StringVar()
text1.set('Subtotal:')
text2.set('Tax(  %):')
text3.set('Total:')
text4.set('Amount Paid:')

tk.Entry(window, bd=1, relief='solid', textvariable=text1).grid(row=21,column=3,sticky='nesw')
tk.Entry(window, bd=1, relief='solid', textvariable=text2).grid(row=22,column=3,sticky='nesw')
tk.Entry(window, bd=1, relief='solid', textvariable=text3).grid(row=23,column=3,sticky='nesw')
tk.Entry(window, bd=1, relief='solid', textvariable=text4).grid(row=24,column=3,sticky='nesw')
tk.Label(window, text=' ').grid(row=25,column=0)

#Signature
tk.Label(window, text='Authorized Signature:', font=('bold',10)).grid(row=26,column=3)
tk.Entry(window).grid(row=26,column=4)
tk.Label(window, text=' ').grid(row=27,column=0)
tk.Label(window, text='Representative Name:', font=('bold',10)).grid(row=28,column=3)
tk.Entry(window).grid(row=28,column=4)





# In[ ]:


window.mainloop()


# In[ ]:




