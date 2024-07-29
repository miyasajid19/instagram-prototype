from tkinter import *
from tkinter import messagebox, ttk,filedialog
from PIL import Image, ImageTk
import webbrowser
import sqlite3
import random
import os
import shutil
import random

root = Tk()
root.config(bg="#000")
root.title("Instagram")
root.iconbitmap(r"images/icon.ico")

root.geometry("+0+0")
root.resizable(False, False)

head = Frame(root, bg="#000")
head.grid(row=0, column=0, sticky="ew")
body = Frame(root, background="#000")
body.grid(row=1, column=0, sticky="nsew")
foot = Frame(root, background="#000")
foot.grid(row=2, column=0, sticky="ew")

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
def back(id,data):
    if id=="addpost":
        addframe.destroy()
        home(data)
        addpost.config(state="normal")
    if id=="myposts":
        home(data)
    
    if id=="updatepost":
        updateframe.destroy()
        myposts(data)
        myimages.config(state="normal")
    if id=="comment":
        home(data)
    if id=='all':
        try:
            addframe.destroy()
            addpost.config(state="normal")
        except:
            pass
        try:
            updateframe.destroy()
        except:
            pass
        try:
            homeframe.destroy()
        except:
            pass
        home(data)
def deleteprofile():
    c=messagebox.askokcancel("warning","your are about delete your account")
    if c ==True:
        conn,cursor=connection()
        cursor.execute("delete  from `posts` where username=?",(data[1],))
        cursor.execute("delete  from `users` where username=?",(data[1],))
        homeframe.destroy()
        conn.commit()
        conn.close()
        main()
def updateaccount():
    conn,cursor=connection()
    cursor.execute("update users set `username`=?, `full_name`=?,`passkey`=? where `contact`=?",(username.get(),name.get(),userkey.get(),contact.get()))
    cursor.execute("select * from users where `username`=? and `passkey`=?",(username.get(),userkey.get()))
    global data
    data=cursor.fetchone()
    conn.commit()
    conn.close()
    home(data)
def updatemyprofile():
    global loginframe, userkey, contact, name, username, homeframe
    
    if homeframe:
        homeframe.destroy()

    homeframe = Frame(body, background="#000")
    homeframe.pack(fill=BOTH, expand=1)

    Label(homeframe, text="Update Profile", font="Helvetica 24 bold", bg="#000", fg="white").grid(row=0, column=0, columnspan=3, pady=20)
    Label(homeframe, text="Email/Phone No.:", font="Helvetica 18", bg="#000", fg="white").grid(row=1, column=0, sticky=E, padx=10, pady=10)
    contact = Entry(homeframe, font="Helvetica 14 italic", width=30)
    contact.insert(0, data[0])
    contact.config(state="readonly")
    contact.grid(row=1, column=1, columnspan=2, pady=10)

    Label(homeframe, text="Username:", font="Helvetica 18", bg="#000", fg="white").grid(row=2, column=0, sticky=E, padx=10, pady=10)
    username = Entry(homeframe, font="Helvetica 14 italic", width=30)
    username.insert(0, data[1])
    username.config(state="readonly")
    username.grid(row=2, column=1, columnspan=2, pady=10)

    Label(homeframe, text="Full Name:", font="Helvetica 18", bg="#000", fg="white").grid(row=3, column=0, sticky=E, padx=10, pady=10)
    name = Entry(homeframe, font="Helvetica 14 italic", width=30)
    name.insert(0, data[2])
    name.grid(row=3, column=1, columnspan=2, pady=10)

    Label(homeframe, text="Password:", font="Helvetica 18", bg="#000", fg="white").grid(row=4, column=0, sticky=E, padx=10, pady=10)
    userkey = Entry(homeframe, font="Helvetica 14 italic", width=30, show="*")
    userkey.insert(0, data[3])
    userkey.grid(row=4, column=1, columnspan=2, pady=10)

    Button(homeframe, text="Update", font="Poppins 14 italic", border=2, background="sky blue", width=40, command=updateaccount).grid(row=5, column=0, columnspan=3, pady=20)

def myprofile(data):
    global homeframe, contentframe, show_var
    try:
        homeframe.destroy()
    except:
        pass
    conn,cursor=connection()
    cursor.execute("select * from users where `contact`=?",(data[0],))
    conn.commit()
    conn.close()
    def reveal_password(event=None):
        password_label.config(text=data[3])
    
    def hide_password(event=None):
        password_label.config(text="*" * len(data[3]))

    root.geometry("500x800+0+0")
    root.resizable(True,True)
    homeframe = Frame(body, bg="#000")
    homeframe.pack(fill=BOTH, expand=1)

    Label(homeframe, text="Contact: ", bg="#000", fg="wheat", font=("Monotype Corsiva", 20, "bold")).grid(row=0, column=0)
    Label(homeframe, text=data[0], bg="#000", fg="wheat", font=("Monotype Corsiva", 20, "italic")).grid(row=0, column=1)
    Label(homeframe, text="Username: ", bg="#000", fg="wheat", font=("Monotype Corsiva", 20, "bold")).grid(row=1, column=0)
    Label(homeframe, text=data[1], bg="#000", fg="wheat", font=("Monotype Corsiva", 20, "italic")).grid(row=1, column=1)
    Label(homeframe, text="Name: ", bg="#000", fg="wheat", font=("Monotype Corsiva", 20, "bold")).grid(row=2, column=0)
    Label(homeframe, text=data[2], bg="#000", fg="wheat", font=("Monotype Corsiva", 20, "italic")).grid(row=2, column=1)
    Label(homeframe, text="Current Password: ", bg="#000", fg="wheat", font=("Monotype Corsiva", 20, "bold")).grid(row=3, column=0)
    
    password_label = Label(homeframe, text="*" * len(data[3]), bg="#000", fg="wheat", font=("Monotype Corsiva", 20, "italic"),wraplength=400)
    password_label.grid(row=3, column=1)
    
    show_var = IntVar()
    show_checkbox = Checkbutton(homeframe, text="Show", variable=show_var, bg="#000", fg="wheat", font=("Monotype Corsiva", 20, "bold"))
    show_checkbox.grid(row=4, column=1)
    show_checkbox.bind('<ButtonPress>', reveal_password)
    show_checkbox.bind('<ButtonRelease>', hide_password)

    Label(homeframe, text="Followers: ", bg="#000", fg="wheat", font=("Monotype Corsiva", 20, "bold")).grid(row=5, column=0)
    if data[4] != None:
        Label(homeframe, text="\n".join(data[4].split(",")), bg="#000", fg="wheat", font=("Monotype Corsiva", 20, "italic")).grid(row=5, column=1)
    
    Label(homeframe, text="Following: ", bg="#000", fg="wheat", font=("Monotype Corsiva", 20, "bold")).grid(row=6, column=0)
    if data[5] != None:
        Label(homeframe, text="\n".join(data[5].split(",")), bg="#000", fg="wheat", font=("Monotype Corsiva", 20, "italic")).grid(row=6, column=1)
    
    Button(homeframe, text="Update", font="stencil 20 italic", bg="#000", fg="white", border=0, command=updatemyprofile).grid(row=7, column=0)
    Button(homeframe, text="Delete", font="stencil 20 italic", bg="#000", fg="white", border=0, command=deleteprofile).grid(row=7, column=1)

def foooter():
    Label(foot, text="built with ❤️ by Sajid Miya", font="stencil 15 bold", fg="wheat", bg="#000").grid(row=0)
    Label(foot, text="© 2024 Sajid Miya. All Rights Reserved.", font="stencil 15 bold", fg="wheat", bg="#000").grid(row=1)

def imageid():
    x = random.randint(1000000000, 9999999999)
    conn, cursor = connection()
    if conn and cursor:
        try:
            cursor.execute("SELECT * FROM posts WHERE imageid=?", (x,))
            if cursor.fetchone():
                conn.close()
                return imageid()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error checking image ID: {e}")
        finally:
            conn.close()
    return x
def addposts():
    global file_path,pid
    try:
        conn,mycursor=connection()
        mycursor=conn.cursor()
        mycursor.execute(f"INSERT INTO `posts`(`username`, `imageid`,`captions`) VALUES ('{data[1]}','{pid}','{captions.get("1.0", "end-1c")}')")
        conn.commit()
        conn.close()
        messagebox.showinfo("info","added successfully")
        if not os.path.exists("posts"):
            os.makedirs("posts")
        image_name = os.path.basename(file_path)
        _, image_ext = os.path.splitext(image_name)
        new_image_name = f"Post_{pid}{image_ext}"
        destination = os.path.join("posts", new_image_name)
        shutil.copyfile(file_path, destination)
        messagebox.showinfo("info"," image saved successfully")
        back("addpost",data)
    except Exception as e:
        pass
def addnewpost():
    global homeframe,addframe,data,addpost
    addpost.config(state="disabled")
    homeframe.destroy()
    root.geometry("520x800+0+0")
    root.resizable(True,True)
    def upload_image():
        global file_path
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            load_image(file_path)
    def load_image(image_path):
        if uploaded_image_label.winfo_exists():
            uploaded_image_label.grid_forget()
        image = Image.open(image_path)
        image.thumbnail((500, 350))  
        photo = ImageTk.PhotoImage(image)
        uploaded_image_label.config(image=photo)
        uploaded_image_label.image = photo
        uploaded_image_label.grid(row=0, column=0, columnspan=2, pady=10)  
    addframe = Frame(body, background="#000")
    global pid
    pid = imageid()
    global uploaded_image_label
    img = Image.open("images/dummy.jpg")
    img = img.resize((500, 400))  
    img = ImageTk.PhotoImage(img)
    uploaded_image_label = Label(addframe,image=img)
    uploaded_image_label.image=img
    uploaded_image_label.grid(row=0, column=0, columnspan=2, pady=10)  
    global captions

    upload_button = Button(addframe, text="Upload Image", command=upload_image,bg="#333",fg="wheat",border=0)
    upload_button.grid(row=5, column=0, columnspan=2, pady=10)
    Label(addframe, text="Captions :", background="#000", fg="white", font="poppins 20 bold").grid(row=6, column=0)
    captions=Text(addframe,height=4,width=40)
    captions.grid(row=6,column=1)
    Button(addframe, text="Add", font="stencil 20 italic", bg="#000", fg="white", border=0,command=addposts).grid(row=7,column=0)
    Button(addframe, text="Back", font="stencil 20 italic", bg="#000", fg="white", border=0,command=lambda : back("addpost",data)).grid(row=7,column=1)
    addframe.pack()
def header():
    global data,addpost,myimages
    Button(head, text="Instagram", bg="#000", fg="wheat", font=("Monotype Corsiva", 20, "bold"), border=0,command=lambda : back("all",data)).grid(row=0, column=0, padx=(0, 200))
    img = Image.open(r"images/addpost.png").resize((50, 50))
    img = ImageTk.PhotoImage(img)
    addpost = Button(head, image=img, bg="wheat", fg="wheat", font=("Monotype Corsiva", 20, "bold"), border=0,command=addnewpost)
    addpost.grid(row=0, column=1, padx=(0,10))
    addpost.image = img
    img = Image.open(r"images/like.png").resize((50, 50))
    img = ImageTk.PhotoImage(img)
    myimages = Button(head, image=img, bg="wheat", fg="wheat", font=("Monotype Corsiva", 20, "bold"), border=0,command=lambda: myposts(data))
    myimages.image = img
    myimages.grid(row=0, column=2)

    img = Image.open(r"images/dummy.jpg").resize((50, 50))
    img = ImageTk.PhotoImage(img)
    myimages = Button(head, image=img, bg="wheat", fg="wheat", font=("Monotype Corsiva", 20, "bold"), border=0,command=lambda: myprofile(data))
    myimages.image = img
    myimages.grid(row=0, column=3,padx=(10,0))
def changepassword():
    conn, cursor = connection()
    try:
        cursor.execute("UPDATE users SET passkey=? WHERE username=?", (userkey.get(), userid.get()))
        conn.commit()  
        
        login(userid.get(),userkey.get())
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))
        conn.rollback()  
        conn.close()


def forgetpassword(id):
    global loginframe, userid, userkey
    try:
        loginframe.destroy()
    except Exception as e:
        pass
    loginframe = Frame(body, background="#000")
    loginframe.pack(fill=BOTH, expand=1)
    Label(loginframe, text="Instagram", font=("Monotype Corsiva", 40, "bold"), bg="#000", fg="white").grid(row=0, column=0, columnspan=3, padx=100, pady=70)
    Label(loginframe, text="username : ", font="helvetica 18", bg="#000", fg="white").grid(row=1, column=0)
    userid = Entry(loginframe, font="helvetica 14 italic", width=30)
    userid.grid(row=1, column=1, columnspan=2)
    Label(loginframe, text="New password : ", font="helvetica 18", bg="#000", fg="white").grid(row=2, column=0)
    userkey = Entry(loginframe, font="helvetica 14 italic", width=30, show="*")
    userkey.grid(row=2, column=1, columnspan=2)
    Button(loginframe, text="Change password", font="poppins 14 italic", border=2, background="sky blue", width=40, command=changepassword).grid(row=4, column=0, columnspan=3, pady=20)
    
def connection():
    try:
        conn = sqlite3.connect('instaserver.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                contact VARCHAR(255) UNIQUE,
                username VARCHAR(255) PRIMARY KEY,
                full_name VARCHAR(255) NOT NULL,
                passkey VARCHAR(255) NOT NULL,
                followers TEXT,
                following TEXT
            );
        ''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS posts (
    username VARCHAR(255),
    imageid VARCHAR(255) PRIMARY KEY,
    captions TEXT,
    likecounts INT DEFAULT 0,
    likedby TEXT,
    comments TEXT
);

        ''')
        conn.commit()
        return conn, cursor
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Error connecting to database: {e}")
        return None, None
def updateposts(caption,postid):

    try:
        conn,mycursor=connection()
        mycursor=conn.cursor()
        mycursor.execute(f"update  `posts` set `captions`=? where `imageid`=?", (caption,postid))
        
        conn.commit()
        conn.close()
        messagebox.showinfo("info","updated successfully")

        back("updatepost",data)
    except Exception as e:
        pass
def updatepost(postid):
    conn,cursor=connection()
    cursor.execute("select * from `posts` where `imageid`=?",(postid,))
    data=cursor.fetchone()
    conn.commit()
    conn.close()
    global homeframe,updateframe,addpost

    homeframe.destroy()
    root.geometry("520x800+0+0")
    root.resizable(True,True)
    
    updateframe = Frame(body, background="#000")
    global pid
    pid = postid
    global uploaded_image_label
    def display_image(image_name_without_extension, label):
        folder_path = "./posts"
        possible_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
        found = False
        for ext in possible_extensions:
            image_path = os.path.join(folder_path, image_name_without_extension + ext)
            if os.path.exists(image_path):
                found = True
                break
        if found:
            img = Image.open(image_path)
            img = img.resize((500, 400))
            img_tk = ImageTk.PhotoImage(img)
            label.config(image=img_tk)
            label.image = img_tk
        else:
            pass
    image_name_without_extension = f"Post_{postid}"
    uploaded_image_label = Label(updateframe,image=None)
    uploaded_image_label.grid(row=0, column=0, columnspan=2, pady=10)  
    display_image(image_name_without_extension, uploaded_image_label)
    global captions

    upload_button = Button(updateframe, text="Upload Image", command=None,bg="#333",fg="wheat",border=0)
    upload_button.grid(row=5, column=0, columnspan=2, pady=10)
    Label(updateframe, text="Captions :", background="#000", fg="white", font="poppins 20 bold").grid(row=6, column=0)
    captions=Text(updateframe,height=4,width=40)
    captions.insert("1.0",data[2])
    captions.grid(row=6,column=1)
    Button(updateframe, text="UPDATE", font="stencil 20 italic", bg="#000", fg="#36fc27", border=0,command=lambda: updateposts(captions.get("1.0","end-1c"),postid)).grid(row=7,column=0)
    Button(updateframe, text="Back", font="stencil 20 italic", bg="#000", fg="white", border=0,command=lambda : back("updatepost",data)).grid(row=7,column=1)
    updateframe.pack()
def myposts(data):
    global homeframe,contentframe
    try:
        homeframe.destroy()
    except :
        pass
    root.geometry("500x800+0+0")
    homeframe = Frame(body, bg="#000")
    homeframe.pack(fill=BOTH, expand=1)
    mycanvas = Canvas(homeframe, bg="#000")
    mycanvas.pack(side=LEFT, fill=BOTH, expand=1)
    myscrollbar = ttk.Scrollbar(homeframe, orient=VERTICAL, command=mycanvas.yview)
    myscrollbar.pack(side=RIGHT, fill=Y)
    mycanvas.configure(yscrollcommand=myscrollbar.set)
    mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox("all")))

    def on_mouse_wheel(event):
        mycanvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def on_arrow_key(event):
        if event.keysym == 'Up':
            mycanvas.yview_scroll(-1, "units")
        elif event.keysym == 'Down':
            mycanvas.yview_scroll(1, "units")

    mycanvas.bind_all("<MouseWheel>", on_mouse_wheel)
    root.bind_all("<Up>", on_arrow_key)
    root.bind_all("<Down>", on_arrow_key)

    contentframe = Frame(mycanvas, bg="#000")
    mycanvas.create_window((0, 0), window=contentframe, anchor='nw')

    conn, cursor = connection()
    cursor.execute("SELECT * FROM `posts`")
    posts = cursor.fetchall()
    random.shuffle(posts)
    conn.commit()
    conn.close()

    def display_image(image_name_without_extension, label):
        folder_path = "./posts"
        possible_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
        found = False
        for ext in possible_extensions:
            image_path = os.path.join(folder_path, image_name_without_extension + ext)
            if os.path.exists(image_path):
                found = True
                break
        if found:
            img = Image.open(image_path)
            img = img.resize((500, 600))
            img_tk = ImageTk.PhotoImage(img)
            label.config(image=img_tk)
            label.image = img_tk
        else:
            pass

    r = -1
    for i in posts:
        r+=1
        if i[0] != data[1]:
            continue
        Button(contentframe, text=f"UPDATE", font=("Monotype Corsiva", 16, "bold"),border=0,activebackground="#000",  bg="#000", fg="#36fc27",command=lambda pid=i[1]: updatepost(pid)).grid(row=r,column=0)
        Button(contentframe, text=f"DELETE", font=("Monotype Corsiva", 16, "bold"),border=0,activebackground="#000",  bg="#000", fg="red",command=None).grid(row=r,column=1)
        Button(contentframe, text=f"BACK", font=("Monotype Corsiva", 16, "bold"),border=0,activebackground="#000",  bg="#000", fg="red",command=lambda : back("myposts",data)).grid(row=r,column=2)

        r+=1
        image_name_without_extension = f"Post_{i[1]}"
        postfeed = Label(contentframe, image=None, bg="#000")
        postfeed.grid(row=r, columnspan=5)
        r += 1
        Label(contentframe, text=i[2], font=("Monotype Corsiva", 20, "italic"), bg="#000", fg="white", wraplength=400).grid(row=r, columnspan=5)
        r += 1
        
        img=Image.open(r"images/like.png").resize((20,20))
        img=ImageTk.PhotoImage(img)
        love=Button(contentframe,image=img,bg="wheat",border=0)
        love.grid(row=r,column=1)
        love.image=img
        likebutton = Button(contentframe, text=f"Liked by : {i[-2]}", font=("Monotype Corsiva", 16, "bold"),border=0,activebackground="#000",  bg="#000", fg="white",command=None,wraplength=500)
        likebutton.grid(row=r, column=0)
        likebutton.config(fg="red")
        love.config(bg="red",fg="blue")

        conn,cursor=connection()

        cursor.execute("select `comments` from `posts` where `imageid`=?",(i[1],))
        r+=1
        allcomments=list(cursor.fetchone())
        try:
            allcomments=allcomments[0].split(',') 
        except :
            pass
        for j in allcomments:
            Label(contentframe, text=j, font=("Monotype Corsiva", 20, "italic"), bg="#000", fg="aqua", wraplength=400,justify="left").grid(row=r, columnspan=5)
            r+=1
        conn.commit()
        conn.close()
        Label(contentframe, text="_"*35, font=("Monotype Corsiva", 20, "italic"), bg="#000", fg="white").grid(row=r, columnspan=5)
        display_image(image_name_without_extension, postfeed)

def createaccount():
    global loginframe, userkey, contact, name, username
    conn, cursor = connection()
    if conn and cursor:
        try:
            cursor.execute("INSERT INTO users (contact, username, full_name, passkey) VALUES (?, ?, ?, ?)",
                           (contact.get(), username.get(), name.get(), userkey.get()))
            conn.commit()
            messagebox.showinfo("Success", "Account created successfully!")
            login(username.get(), userkey.get())
            newframe.destroy()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error inserting data: {e}")
        finally:
            conn.close()

def newaccount():
    global loginframe, userkey, contact, name, username, newframe
    loginframe.destroy()
    newframe = Frame(body, background="#000")
    newframe.pack(fill=BOTH, expand=1)
    Label(newframe, text="Instagram", font=("Monotype Corsiva", 40, "bold"), bg="#000", fg="white").grid(row=0, column=0, columnspan=3, padx=30, pady=30)
    Label(newframe, text="Sign up to see photos and videos ", font=("Monotype Corsiva", 20, "bold"), bg="#000", fg="white").grid(row=1, column=0, columnspan=3)
    Label(newframe, text="from your friends.", font=("Monotype Corsiva", 20, "bold"), bg="#000", fg="white").grid(row=2, column=0, columnspan=3)
    Button(newframe, text="Log in with Facebook", font=("Monotype Corsiva", 14, "bold"), border=0, background="sky blue", width=40).grid(row=3, column=0, columnspan=3, padx=10, pady=10)
    Label(newframe, text="--------------------OR--------------------", font=("Monotype Corsiva", 14, "bold"), bg="#000", fg="white").grid(row=4, column=0, columnspan=3, padx=10, pady=10)
    Label(newframe, text="email/phone no. : ", font="helvetica 18", bg="#000", fg="white").grid(row=5, column=0)
    contact = Entry(newframe, font="helvetica 14 italic", width=30)
    contact.grid(row=5, column=1, columnspan=2)
    Label(newframe, text="Full Name : ", font="helvetica 18", bg="#000", fg="white").grid(row=6, column=0)
    name = Entry(newframe, font="helvetica 14 italic", width=30)
    name.grid(row=6, column=1, columnspan=2)
    Label(newframe, text="Username : ", font="helvetica 18", bg="#000", fg="white").grid(row=7, column=0)
    username = Entry(newframe, font="helvetica 14 italic", width=30)
    username.grid(row=7, column=1, columnspan=2)
    Label(newframe, text="Password : ", font="helvetica 18", bg="#000", fg="white").grid(row=8, column=0)
    userkey = Entry(newframe, font="helvetica 14 italic", width=30, show="*")
    userkey.grid(row=8, column=1, columnspan=2)
    Label(newframe, text="People who use our service may have uploaded your contact information to Instagram.", font=("Monotype Corsiva", 15, "bold"), bg="#000", fg="white", wraplength=400, anchor=W).grid(row=9, column=0, columnspan=2, pady=(20, 0))
    Button(newframe, text="learn more", font="arial 10 italic", fg="violet", bg="#000", command=lambda: webbrowser.open("http://www.sajidmiya.com.np"), border=0).grid(row=9, column=2, pady=(40, 0), sticky='w')
    Label(newframe, text="By signing up, you agree to our Terms ,", font=("Monotype Corsiva", 15, "bold"), bg="#000", fg="white").grid(row=10, column=0, columnspan=2)
    Button(newframe, text=" Privacy Policy and Cookies Policy .", font="arial 10 italic", fg="violet", bg="#000", command=lambda: webbrowser.open("http://www.sajidmiya.com.np"), border=0, wraplength=150, anchor=W).grid(row=10, column=2, sticky='w')
    Button(newframe, text="Sign Up", font="poppins 14 italic", border=2, background="sky blue", width=40, command=createaccount).grid(row=11, column=0, columnspan=3)
    Label(newframe, text="Have an account?", font="helvetica 18", bg="#000", fg="white").grid(row=12, column=0, columnspan=2, pady=20)
    Button(newframe, text="Log In", font="arial 10 italic", fg="sky blue", bg="#000", command=signup, border=0).grid(row=12, column=2, pady=20, sticky='W')


def updatelike(imageid, likecount, likebutton,love):
    
    conn, cursor = connection()
    cursor.execute("SELECT likedby FROM posts WHERE imageid=?", (imageid,))
    likedbytuple = cursor.fetchone()
    if likedbytuple:
        try:
            likedbylist = list(likedbytuple[0].split(','))  
        except Exception as e:
            likedbylist=list()
        if '' in likedbylist:
            likedbylist.remove('')
        if data[1] in likedbylist:
            likedbylist.remove(data[1])
            likecount=len(likedbylist)
            likebutton.config(fg="white")
            love.config(bg="wheat")
        else:
            likedbylist.append(data[1])
            likecount=len(likedbylist)
            likebutton.config(fg="red")
            love.config(bg="red")
        
        likedbystr = ','.join(likedbylist)
        cursor.execute("UPDATE posts SET likecounts = ?, likedby = ? WHERE imageid = ?", (likecount, likedbystr, imageid))
        conn.commit()

    conn.close()
    likebutton.config(text=f"Likes: {likecount}")
def follow(contentcreater,userid,btn):
    conn,cursor=connection()
    cursor.execute("SELECT `followers` from `users` where username=?",(contentcreater,))
    followers=cursor.fetchone()
    followers=list(followers)
    cursor.execute("SELECT `following` from `users` where username=?",(userid,))
    following=cursor.fetchone()
    
    if followers:
        try:
            followerlist = list(followers[0].split(',')) 
        except Exception as e:
            followerlist=list()
    if userid in followerlist:
        followerlist.remove(userid)
        btn.config(text="follow")
    else:
        followerlist.append(userid)
        btn.config(text="following")
    if following:
        try:
            followinglist = list(following[0].split(','))
        except Exception as e:
            followinglist=list()
    if contentcreater in followinglist:
        followinglist.remove(contentcreater)
    else:
        followinglist.append(contentcreater)
    followerstr = ','.join(followerlist)
    followingstr = ','.join(followinglist)
    cursor.execute("UPDATE `users` SET `followers`=? where  `username`=?",(followerstr,contentcreater))
    conn.commit()
    cursor.execute("UPDATE `users` SET `following`=? where  `username`=?",(followingstr,userid))
    conn.commit()

    conn.close()
    root.after(1,home(data))
    contentframe.after(1,home(data))

def isinfollowings(contentcreater,userid):
    conn,cursor=connection()
    cursor.execute("SELECT `following` from `users` where username=?",(userid,))
    followings=cursor.fetchone()                                
    try:
        if followings:
            try:
                followinglist = list(followings[0].split(','))
            except Exception as e:
                followinglist=list()
        conn.commit()
        conn.close()
        if contentcreater in followinglist:
            return True
        else:
            return False
    except :
        return False

def addcomment(details, comments, imageid):
    
    conn, cursor = connection()
    new_comment = f"{details[1]} \n {comments}\n"
    
    try:
        cursor.execute("SELECT `comments` FROM `posts` WHERE `imageid`=?", (imageid,))
        existing_comment = cursor.fetchone()
        
        if existing_comment:
            existing_comment = existing_comment[0]
            try:
                existing_comment_list = existing_comment.split(',')
            except Exception as e:
                existing_comment_list = []
        else:
            existing_comment_list = []

        existing_comment_list.append(new_comment)

        updated_comments = ','.join(existing_comment_list)

        cursor.execute("UPDATE `posts` SET `comments`=? WHERE `imageid`=?", (updated_comments, imageid))
        conn.commit()
        home(data)
    except sqlite3.Error as e:
        pass
    except Exception as e:
        pass
    finally:
        conn.close()
def likestate(imageid):
    conn, cursor = connection()
    cursor.execute("SELECT likedby FROM posts WHERE imageid=?", (imageid,))
    likedbytuple = cursor.fetchone()
    
    if likedbytuple:
        try:
            likedbylist = likedbytuple[0].split(',')  
        except Exception as e:
            likedbylist = []
        if data[1] in likedbylist:
            conn.close()
            return True
        else:
            conn.close()
            return False
    else:
        conn.close()
        return False
def stockprofile(uid,data):
    global homeframe,contentframe
    try:
        homeframe.destroy()
    except :
        pass
    root.geometry("500x800+0+0")
    homeframe = Frame(body, bg="#000")
    homeframe.pack(fill=BOTH, expand=1)
    mycanvas = Canvas(homeframe, bg="#000")
    mycanvas.pack(side=LEFT, fill=BOTH, expand=1)
    myscrollbar = ttk.Scrollbar(homeframe, orient=VERTICAL, command=mycanvas.yview)
    myscrollbar.pack(side=RIGHT, fill=Y)
    mycanvas.configure(yscrollcommand=myscrollbar.set)
    mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox("all")))

    def on_mouse_wheel(event):
        mycanvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def on_arrow_key(event):
        if event.keysym == 'Up':
            mycanvas.yview_scroll(-1, "units")
        elif event.keysym == 'Down':
            mycanvas.yview_scroll(1, "units")

    mycanvas.bind_all("<MouseWheel>", on_mouse_wheel)
    root.bind_all("<Up>", on_arrow_key)
    root.bind_all("<Down>", on_arrow_key)

    contentframe = Frame(mycanvas, bg="#000")
    mycanvas.create_window((0, 0), window=contentframe, anchor='nw')

    conn, cursor = connection()
    cursor.execute("SELECT * FROM `posts`")
    posts = cursor.fetchall()
    random.shuffle(posts)
    conn.commit()
    conn.close()

    def display_image(image_name_without_extension, label):
        folder_path = "./posts"
        possible_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
        found = False
        for ext in possible_extensions:
            image_path = os.path.join(folder_path, image_name_without_extension + ext)
            if os.path.exists(image_path):
                found = True
                break
        if found:
            img = Image.open(image_path)
            img = img.resize((500, 600))
            img_tk = ImageTk.PhotoImage(img)
            label.config(image=img_tk)
            label.image = img_tk
        else:
            pass

    r = -1
    for i in posts:
        print(data)
        if i[0] == uid:
            r += 1
            seeprofile=Button(contentframe, text=i[0], font=("Monotype Corsiva", 20, "italic"), bg="#000", fg="white",border=0,borderwidth=0, wraplength=400,command=None)
            seeprofile.config(command=lambda uid=i[0], btn=seeprofile: stockprofile(uid, data))
            seeprofile.grid(row=r, column=0)
            followbtn=Button(contentframe, text=None, font=("Monotype Corsiva", 20, "italic"), bg="#000", fg="sky blue",border=0,activebackground="#000",activeforeground="wheat", wraplength=400,justify="left",command=None)
            followbtn.config(command=lambda uid=i[0], btn=followbtn: follow(uid, data[1], btn))
            state=isinfollowings(i[0], data[1])
            if state:
                followbtn.config(text="following")
            else:
                followbtn.config(text="follow")
            followbtn.grid(row=r, column=1)
            r+=1
            image_name_without_extension = f"Post_{i[1]}"
            postfeed = Label(contentframe, image=None, bg="#000")
            postfeed.grid(row=r, columnspan=5)
            r += 1
            Label(contentframe, text=i[2], font=("Monotype Corsiva", 20, "italic"), bg="#000", fg="white", wraplength=400).grid(row=r, columnspan=5)
            r += 1
            
            img=Image.open(r"images/like.png").resize((20,20))
            img=ImageTk.PhotoImage(img)
            love=Button(contentframe,image=img,bg="wheat",border=0)
            love.grid(row=r,column=1)
            love.image=img
            likebutton = Button(contentframe, text=f"Likes: {i[3]}", font=("Monotype Corsiva", 16, "bold"),border=0,activebackground="#000",  bg="#000", fg="white",command=None)

            likebutton.config(command=lambda uid=i[1], like=i[-2], btn=likebutton,lbl=love: updatelike(uid, like, btn,lbl))
            love.config(command=lambda uid=i[1], like=i[-2], btn=likebutton,lbl=love: updatelike(uid, like, btn,lbl))
            likebutton.grid(row=r, column=0)
            like=likestate(i[1])
            if like:
                likebutton.config(fg="red")
                love.config(bg="red",fg="blue")
            else:
                pass
            r+=1
            conn,cursor=connection()
            cursor.execute("select `comments` from `posts` where `imageid`=?",(i[1],))
            allcomments=list(cursor.fetchone())
            try:
                allcomments=allcomments[0].split(',') 
            except :
                pass
            for j in allcomments:
                Label(contentframe, text=j, font=("Monotype Corsiva", 20, "italic"), bg="#000", fg="#36fc27", wraplength=400,justify="left").grid(row=r, columnspan=5)
                r+=1
            conn.commit()
            conn.close()
            comment=Text(contentframe,height=3,width=30,font=("Monotype Corsiva", 16, "bold"))
            comment.grid(row=r,column=0,columnspan=2,padx=30)
            Button(contentframe, text="Add",font=("Monotype Corsiva", 16, "bold"),border=0,activebackground="#000",  bg="#000", fg="white",command=lambda a=comment,imgid=i[1]: addcomment(data,a.get("1.0", "end-1c"),imgid)).grid(row=r, column=3)
            r+=1
            Label(contentframe, text="_"*35, font=("Monotype Corsiva", 20, "italic"), bg="#000", fg="white").grid(row=r, columnspan=5)
            display_image(image_name_without_extension, postfeed)

def home(data):
    global homeframe,contentframe
    try:
        homeframe.destroy()
    except :
        pass
    root.geometry("500x800+0+0")
    homeframe = Frame(body, bg="#000")
    homeframe.pack(fill=BOTH, expand=1)
    mycanvas = Canvas(homeframe, bg="#000")
    mycanvas.pack(side=LEFT, fill=BOTH, expand=1)
    myscrollbar = ttk.Scrollbar(homeframe, orient=VERTICAL, command=mycanvas.yview)
    myscrollbar.pack(side=RIGHT, fill=Y)
    mycanvas.configure(yscrollcommand=myscrollbar.set)
    mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox("all")))

    def on_mouse_wheel(event):
        mycanvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def on_arrow_key(event):
        if event.keysym == 'Up':
            mycanvas.yview_scroll(-1, "units")
        elif event.keysym == 'Down':
            mycanvas.yview_scroll(1, "units")

    mycanvas.bind_all("<MouseWheel>", on_mouse_wheel)
    root.bind_all("<Up>", on_arrow_key)
    root.bind_all("<Down>", on_arrow_key)

    contentframe = Frame(mycanvas, bg="#000")
    mycanvas.create_window((0, 0), window=contentframe, anchor='nw')

    conn, cursor = connection()
    cursor.execute("SELECT * FROM `posts`")
    posts = cursor.fetchall()
    random.shuffle(posts)
    conn.commit()
    conn.close()

    def display_image(image_name_without_extension, label):
        folder_path = "./posts"
        possible_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
        found = False
        for ext in possible_extensions:
            image_path = os.path.join(folder_path, image_name_without_extension + ext)
            if os.path.exists(image_path):
                found = True
                break
        if found:
            img = Image.open(image_path)
            img = img.resize((500, 600))
            img_tk = ImageTk.PhotoImage(img)
            label.config(image=img_tk)
            label.image = img_tk
        else:
            pass

    r = -1
    for i in posts:
        if i[0] == data[1]:
            continue
        r += 1
        seeprofile=Button(contentframe, text=i[0], font=("Monotype Corsiva", 20, "italic"), bg="#000", fg="white",border=0,borderwidth=0, wraplength=400,command=None)
        seeprofile.config(command=lambda uid=i[0], btn=seeprofile: stockprofile(uid, data))
        seeprofile.grid(row=r, column=0)
        followbtn=Button(contentframe, text=None, font=("Monotype Corsiva", 20, "italic"), bg="#000", fg="sky blue",border=0,activebackground="#000",activeforeground="wheat", wraplength=400,justify="left",command=None)
        followbtn.config(command=lambda uid=i[0], btn=followbtn: follow(uid, data[1], btn))
        state=isinfollowings(i[0], data[1])
        if state:
            followbtn.config(text="following")
        else:
            followbtn.config(text="follow")
        followbtn.grid(row=r, column=1)
        r+=1
        image_name_without_extension = f"Post_{i[1]}"
        postfeed = Label(contentframe, image=None, bg="#000")
        postfeed.grid(row=r, columnspan=5)
        r += 1
        Label(contentframe, text=i[2], font=("Monotype Corsiva", 20, "italic"), bg="#000", fg="white", wraplength=400).grid(row=r, columnspan=5)
        r += 1
        
        img=Image.open(r"images/like.png").resize((20,20))
        img=ImageTk.PhotoImage(img)
        love=Button(contentframe,image=img,bg="wheat",border=0)
        love.grid(row=r,column=1)
        love.image=img
        likebutton = Button(contentframe, text=f"Likes: {i[3]}", font=("Monotype Corsiva", 16, "bold"),border=0,activebackground="#000",  bg="#000", fg="white",command=None)

        likebutton.config(command=lambda uid=i[1], like=i[-2], btn=likebutton,lbl=love: updatelike(uid, like, btn,lbl))
        love.config(command=lambda uid=i[1], like=i[-2], btn=likebutton,lbl=love: updatelike(uid, like, btn,lbl))
        likebutton.grid(row=r, column=0)
        like=likestate(i[1])
        if like:
            likebutton.config(fg="red")
            love.config(bg="red",fg="blue")
        else:
            pass
        r+=1
        conn,cursor=connection()
        cursor.execute("select `comments` from `posts` where `imageid`=?",(i[1],))
        allcomments=list(cursor.fetchone())
        try:
            allcomments=allcomments[0].split(',') 
        except :
            pass
        for j in allcomments:
            Label(contentframe, text=j, font=("Monotype Corsiva", 20, "italic"), bg="#000", fg="#36fc27", wraplength=400,justify="left").grid(row=r, columnspan=5)
            r+=1
        conn.commit()
        conn.close()
        comment=Text(contentframe,height=3,width=30,font=("Monotype Corsiva", 16, "bold"))
        comment.grid(row=r,column=0,columnspan=2,padx=30)
        Button(contentframe, text="Add",font=("Monotype Corsiva", 16, "bold"),border=0,activebackground="#000",  bg="#000", fg="white",command=lambda a=comment,imgid=i[1]: addcomment(data,a.get("1.0", "end-1c"),imgid)).grid(row=r, column=3)
        r+=1
        Label(contentframe, text="_"*35, font=("Monotype Corsiva", 20, "italic"), bg="#000", fg="white").grid(row=r, columnspan=5)
        display_image(image_name_without_extension, postfeed)


def login(id, key):
    global data
    conn, cursor = connection()
    if conn and cursor:
        try:
            header()
            cursor.execute("SELECT * FROM users WHERE username=? AND passkey=?", (id, key))
            data = cursor.fetchone()
            if data:
                try:
                    loginframe.destroy()
                except:
                    pass
                home(data)
            else:
                messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error fetching data: {e}")
        finally:
            conn.commit()
            conn.close()

def signup():
    global loginframe, userid, userkey
    try:
        global newframe
        newframe.destroy()
    except Exception as e:
        pass
    loginframe = Frame(body, background="#000")
    loginframe.pack(fill=BOTH, expand=1)
    Label(loginframe, text="Instagram", font=("Monotype Corsiva", 40, "bold"), bg="#000", fg="white").grid(row=0, column=0, columnspan=3, padx=100, pady=70)
    Label(loginframe, text="username : ", font="helvetica 18", bg="#000", fg="white").grid(row=1, column=0)
    userid = Entry(loginframe, font="helvetica 14 italic", width=30)
    userid.grid(row=1, column=1, columnspan=2)
    Label(loginframe, text="Password : ", font="helvetica 18", bg="#000", fg="white").grid(row=2, column=0)
    userkey = Entry(loginframe, font="helvetica 14 italic", width=30, show="*")
    userkey.grid(row=2, column=1, columnspan=2)
    Button(loginframe, text="Log in", font="poppins 14 italic", border=2, background="sky blue", width=40, command=lambda: login(userid.get(), userkey.get())).grid(row=4, column=0, columnspan=3, pady=20)
    Label(loginframe, text="--------------------OR--------------------", font=("Monotype Corsiva", 14, "bold"), bg="#000", fg="white").grid(row=5, column=0, columnspan=3, padx=10, pady=10)
    Button(loginframe, text="Log in with Facebook", font=("Monotype Corsiva", 14, "bold"), border=0, bg="#000", fg="white").grid(row=6, column=0, columnspan=3, padx=10, pady=10)
    Button(loginframe, text="forget password?", font="arial 10 italic", fg="light green", bg="#000", command=lambda: forgetpassword(userid.get()), border=0).grid(row=7, column=0, columnspan=3)
    Label(loginframe, text="Don't have an account?", font="helvetica 18", bg="#000", fg="white").grid(row=8, column=0, columnspan=2)
    Button(loginframe, text="Sign Up", font="arial 10 italic", fg="light green", bg="#000", command=newaccount, border=0).grid(row=8, column=2)

def main():
    signup()
    foooter()

main()
root.mainloop()

