#!/usr/bin/env python
# coding: utf-8

# In[ ]:


==================================PASSWORD GENERATOR FOR USER=============================================


# In[2]:


pip install pyperclip


# In[ ]:





# In[ ]:


from tkinter import *
import string
import random 
import pyperclip

"""Generates a random password that meets specific requirements"""

    # Define the allowed character sets for the password
#define (def) generator for generate fun

def generator():
    small_alphabets=string.ascii_lowercase   #a-z small alphabates
    capital_alphabets=string.ascii_uppercase #A-z capital alphabates
    numbers=string.digits  #all digits 0-infi 
    special_charecters=string.punctuation   # special characters

    #by combinig all data by adding + 
    #using variable password_length and length_box will return all the element
    
    all=small_alphabets+capital_alphabets+numbers+special_charecters
    password_length=int(length_Box.get())

    # Initialize password with one character from each character set  
    #for displaying password we use passwordfield.insert method 
    #choice condition
    
    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))

    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))

    if choice.get()==3:
        passwordField.insert(0,random.sample(all,password_length))


def copy():
    random_password=passwordField.get()
    pyperclip.copy(random_password)

    
    #object of tk class(tkinter module)
root=Tk()

    #for background color(config is used) you can use many different colors
root.config(bg='cyan')

   #int variable and font varable

choice=IntVar()
Font=('arial',13,'bold')

#label class for creating lable by passing root and txt and from font keywrd argument we can cng font an bg for background
#fg for forground color we used white
# grid method helps us to add a lable on the screen or display padding or space we use pady

passwordLabel=Label(root,text='Password Generator',font=('times new roman',20,'bold'),bg='gray20',fg='white')
passwordLabel.grid(pady=10)


#for button we've used weak radiobuttonclass we'll pass root object for displaying
#for displaying radiobutton on screen and verticle padding for spacing used pady

weakradioButton=Radiobutton(root,text='Weak',value=1,variable=choice,font=Font)
weakradioButton.grid(pady=5)

#for medium radio button its all same just object variable name is diff 

mediumradioButton=Radiobutton(root,text='Medium',value=2,variable=choice,font=Font)
mediumradioButton.grid(pady=5)

#for strong radio button

strongradioButton=Radiobutton(root,text='Strong',value=3,variable=choice,font=Font)
strongradioButton.grid(pady=5)

#like password lable weve used lengthlable for displaying 

lengthLabel=Label(root,text='Password Length',font=Font,bg='gray20',fg='white')
lengthLabel.grid(pady=5)

#for spinboxclass length_box weve used root for passing in root
#and .grid method for adding and displaying

length_Box=Spinbox(root,from_=5,to_=18,width=5,font=Font)
length_Box.grid(pady=5)

#for generate button varablie generatebutton and cmd generator fun is for while we click
#and .grid method for displaying

generateButton=Button(root,text='Generate',font=Font,command=generator)
generateButton.grid(pady=5)

#entryclass for password generation bd for border
#and .grid method for displaying

passwordField=Entry(root,width=25,bd=2,font=Font)
passwordField.grid()

#same as generate button variable is copy button

copyButton=Button(root,text='Copy',font=Font,command=copy)
copyButton.grid(pady=5)


  #object variable to keep window on loop for output
    
     
root.mainloop()


# In[ ]:





# In[ ]:




