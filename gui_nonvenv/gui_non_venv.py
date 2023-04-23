from tkinter import *
from tkinter import messagebox
window=Tk() #The master window
window.title('Welcome')
img=PhotoImage(master=window,file='welcome.png')
label=Label(window,image=img)
label.pack(expand=True)

#add a welcome text boy

def sign_act():
    '''Sign up page'''
    window=Tk()
    window.title('Sigh Up here')
    right_frame= Frame(window,height=800,width=600,bg='white',bd=5)#Frame for the profile options
    right_frame.pack(side='right')
    image=PhotoImage(master=window,file='main.png')
    Label(window,image=image).pack(side='left')
    Label(right_frame,width=30,height=5,text='Sign Up',fg='Pink',bg='white',font=('Comic Sans MS',20,'bold')).place(x=30,y=50)
    
    #Username section
    
    def on_enter(x):
        '''Deletes the temp text once clicked''' 
        if username.get()=='Username':
            username.delete(0,'end')
            
        
    def on_leave(x):
        '''If no entries, inserts temp text'''
        name= username.get()
        if name=='':
            username.insert(0,'Username')
            username['show']=name

    username= Entry(right_frame,bg='white',width=50,bd=0) #where the user will make the name entry
    Frame(right_frame,width=305,height=2,bg='pink').place(x=20,y=225) #Line under the entry bar
    username.insert(0,'Username') #Temporary text
    username.place(x=20,y=200) #Postioning of the entry bar
    username.bind("<FocusIn>", on_enter)
    username.bind("<FocusOut>", on_leave)
    
    #Email section

    def on_enter(x):
        '''Deletes the temp text once clicked''' 
        if sign_email.get()=='Email':
            sign_email.delete(0,'end')
            
        
    def on_leave(x):
        '''If no entries, inserts temp text'''
        mail= sign_email.get()
        if mail=='':
            sign_email.insert(0,'Email')
            sign_email['show']=mail

    sign_email= Entry(right_frame,bg='white',width=50,bd=0) #Recent changes here
    Frame(right_frame,width=305,height=2,bg='pink').place(x=20,y=275)
    sign_email.insert(0,'Email')
    sign_email.place(x=20,y=250)
    sign_email.bind("<FocusIn>", on_enter)
    sign_email.bind("<FocusOut>", on_leave)

    #Password section
    
    def on_enter(x):
        '''Deletes the temp text''' #--------Fix here------#
        if password.get()=='Password':
            password.delete(0,'end')
            password['show']='*'
        
        
    def on_leave(x):
        '''If no entries, inserts temp text'''
        passw= password.get()
        if passw=='':
            password.insert(0,'Password')
            password['show']=passw
    
    password= Entry(right_frame,bg='white',width=50,bd=0)
    
    def show():
        '''Show password'''
        if password['show']=='*':
            password['show'] = ''
    def hide():
        '''Hide password'''
        if password['show']!='*':
            password['show'] = '*'
        
    
    
    show_button=Button(right_frame, text="show", bg='white',fg='pink',
                                    font=('Arabian',10,'bold'),bd=0, command=show,activebackground='white',activeforeground='pink')
    show_button.place(x=240,y=300)

    hide_button= Button(right_frame, text="hide", bg='white',fg='pink',
                                    font=('Arabian',10,'bold'),bd=0, command=hide,activebackground='white',activeforeground='pink')
    hide_button.place(x=280,y=300)
    

    Frame(right_frame,width=305,height=2,bg='pink').place(x=20,y=325)
    password.insert(0,'Password')
    password.place(x=20,y=300)
    password.bind("<FocusIn>", on_enter) #Once clicked, removes the temp text
    password.bind("<FocusOut>", on_leave)#Once away, returns the temp text

    def sign():
        '''Action when the Sign up button is clicked'''
        screen=Toplevel(window)
        print('YES')
        screen.title('Welcome')
        Label(screen,height=800,width=1000,bg='white',bd=0,text='Welcome',font=('Arabian',24,'bold')).pack(expand=True)
        screen.mainloop()
    
    #Sign Up button to finish signing up
    sign_up_button=Button(right_frame,text='Sign up',bg='pink',fg='white',width=25,height=2,font=('Arabian',10,'bold'),
    bd=0.3,command=sign)
    sign_up_button.place(x=20,y=350)
     
    #Already have an account?
    have_acct=Label(right_frame,width=30,height=2,text='Already have account?',fg='black',bg='white',anchor='w',
            font=('Calibri',10,'bold'))
    have_acct.place(x=20,y=390)

    #Login button if you already have
    login_button=Button(right_frame,text='Login',fg='pink',bg='white',anchor='s',bd=0,
    activebackground='white',activeforeground='pink',command=login_act)
    login_button.place(x=147,y=396)

    window.mainloop()





def login_act():
    '''Login page'''
    window=Tk()
    window.title('Log In')
    right_frame= Frame(window,height=800,width=600,bg='white',bd=5)#Frame for the profile options
    right_frame.pack(side='right')
    image2=PhotoImage(master=window,file='main.png')
    Label(window,image=image2).pack(expand=True)
    Label(right_frame,width=30,height=5,text='Login',fg='Pink',bg='white',font=('Comic Sans MS',20,'bold')).place(x=30,y=50)
    
    #Email section

    def on_enter(x):
        '''Deletes the temp text once clicked''' 
        if email.get()=='Email':
            email.delete(0,'end')
            
        
    def on_leave(x):
        '''If no entries, inserts temp text'''
        mail= email.get()
        if mail=='':
            email.insert(0,'Email')
            email['show']=mail

    email= Entry(right_frame,bg='white',width=50,bd=0)
    Frame(right_frame,width=305,height=2,bg='pink').place(x=20,y=275)
    email.insert(0,'Email')
    email.place(x=20,y=250)
    email.bind("<FocusIn>", on_enter)
    email.bind("<FocusOut>", on_leave)

    #Password section

    def on_enter(x):
        '''Deletes the temp text once clicked''' #--------Fix here------#
        if password.get()=='Password':
            password.delete(0,'end')
            password['show']='*'
        

    def on_leave(x):
        '''If no entries, inserts temp text'''
        passw= password.get()
        if passw=='':
            password.insert(0,'Password')
            password['show']=passw
    
    password= Entry(right_frame,bg='white',width=50,bd=0) #Space for password entry
    
    def show():
        '''Show password'''
        if password['show']=='*':
            password['show'] = ''
    def hide():
        '''Hide password'''
        if password['show']!='*' or password['show']!='Password':
            password['show'] = '*'
        
    
    show_button= Button(right_frame, text="show", bg='white',fg='pink',
                                    font=('Arabian',10,'bold'),bd=0, command=show,activebackground='white',activeforeground='pink')
    show_button.place(x=240,y=300)

    hide_button= Button(right_frame, text="hide", bg='white',fg='pink',
                                    font=('Arabian',10,'bold'),bd=0, command=hide,activebackground='white',activeforeground='pink')
    hide_button.place(x=280,y=300)
    
    Frame(right_frame,width=305,height=2,bg='pink').place(x=20,y=325)
    password.insert(0,'Password')
    password.place(x=20,y=300)
    password.bind("<FocusIn>", on_enter) #Once clicked, removes the temp text
    password.bind("<FocusOut>", on_leave)#Once away, returns the temp text

    def log():
        '''Action when the Login button is clicked'''
        if email.get()=='ekundayodavid123@gmail.com' and password.get()=='12345':
            screen=Toplevel(window)
            print('YES')
            screen.title('Welcome')
            Label(screen,height=800,width=1000,bg='white',bd=0,text='Welcome',font=('Arabian',24,'bold')).pack(expand=True)
            screen.mainloop()
        else:
            messagebox.showerror('Error','Input Valid details')

    #Want to Sign up?
    create_acct=Label(right_frame,width=30,height=2,text='Dont have an account?',fg='black',bg='white',anchor='w',
            font=('Calibri',10,'bold'))
    create_acct.place(x=20,y=390)

    #Sign up button if you dont have
    signup_button=Button(right_frame,text='Sign Up',fg='pink',bg='white',anchor='s',bd=0,
    activebackground='white',activeforeground='pink',command=sign_act)
    signup_button.place(x=147,y=396)
            

    
    #Login button to finish signing up
    login_button=Button(right_frame,text='Login',bg='pink',fg='white',width=25,height=2,font=('Arabian',10,'bold'),
    bd=0.3,command=log)
    login_button.place(x=20,y=350)
    window.mainloop()


#----Welcome Page---#

#Welcome Text



#Login option in Welcome page
login_option=Button(window,text='Login',bg='pink',fg='white',bd=0,width=25,height=2,
            font=('Arabian',10,'bold'),command=login_act).place(x=20,y=300)

#Sign up option in Welcome page
sign_up_option=Button(window,text='Sign Up',bg='pink',fg='white',bd=0,width=25,height=2
            ,font=('Arabian',10,'bold'),command=sign_act).place(x=20,y=225)

window.mainloop()