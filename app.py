# from flask import Flask,render_template,request,url_for,session,redirect,flash
# import sqlite3
# from flask import *
# from flask_mail import Mail, Message

# app=Flask(__name__)
# app.secret_key = '122343434'



# conn=sqlite3.connect("Books.db",check_same_thread=False)
# conn.execute("""create table if not exists userdb(id integer primary key autoincrement,username text,
#              password text)""")
# conn.execute("""create table if not exists admindb(id integer primary key autoincrement,username text,
#              password text)""")
# conn.execute("""create table if not exists availablebooksdb(id integer primary key autoincrement,
#              bookname text,authorname text)""")
# conn.execute("""create table if not exists soldbooksdb(id integer primary key autoincrement,
#              bookname text,authorname text)""")

# def insertadmindata():
#     username="venkatesan.uniq@gmail.com"
#     password="12345678"
#     conn.execute("insert into admindb(username,password) values(?,?)",(username,password))
#     conn.commit()
# def insertavailablebooks():
#     book1="python"
#     book2="java"
#     author1="guido"
#     author2="vann"
#     conn.execute("insert into availablebooksdb(bookname,authorname) values(?,?)",(book1,author1))
#     conn.execute("insert into availablebooksdb(bookname,authorname) values(?,?)",(book2,author2))
#     conn.commit()

# @app.route("/default")
# def default():
#     insertadmindata()
#     insertavailablebooks()
#     return render_template("home.html")

# @app.route("/")
# def home():
#     return render_template("home.html")


# @app.route("/signin",methods=["GET","POST"])
# def signin():
#     if request.method=="POST":
#         username=request.form["username"]
#         password=request.form["password"]
        
#         conn.execute("insert into userdb(username,password) values(?,?)",(username,password))
#         conn.commit()
#         return redirect("/")
#     return render_template("signin.html")

# @app.route("/login")
# def login():
#     return render_template("login.html")

# @app.route("/userlogin",methods=["GET","POST"])
# def userlogin():
#     if request.method=="POST":
#         username=request.form["username"]
#         password=request.form["password"]
        
#         select=conn.execute("select * from userdb where username=? and password=?",(username,password))
#         check=select.fetchone()
#         # user1=check[1]
#         # user2=check[2]
#         # if username in check and password in check:
#         if check:
#             if username in check and password in check:
#                 check=conn.execute("select * from availablebooksdb")
#                 data=check.fetchall()
#                 return render_template("userloggedin.html",data=data)
#         else:
#                     return redirect(url_for("userlogin"))  
#     return render_template("userlogin.html")
    
# @app.route("/adminlogin",methods=["GET","POST"])
# def adminlogin():
#      if request.method=="POST":
#         username=request.form["username"]
#         password=request.form["password"]
        
#         select=conn.execute("select * from admindb where username=? or password=?",(username,password))
#         print("select",select)       
#         check=select.fetchone()
#         print("check:",check)
#         if check:
#             print("chek if statement")
#             if username in check and password in check:
#                 return render_template("adminloggedin.html")
#             else:
#                 flash('Invalid Admin user credentials', 'error')
#                 return redirect(url_for("adminlogin"))  
#         else:
#                 return render_template("adminlogin.html")  
#      return render_template("adminlogin.html")   
        
# @app.route("/buybook/<string:book>")
# def buybook(book):
#     data2=conn.execute("select * from soldbooksdb where bookname=?",(book,) )
#     verify=data2.fetchone()
#     if verify:
#         return "Selected Book is sold out"
    
#     data=conn.execute("select * from availablebooksdb where bookname=?",(book,))
#     check=data.fetchone()
#     if check:
#         buybookname= check[1]
#         buyauthorname= check[2]
#         conn.execute("insert into soldbooksdb(bookname,authorname) values(?,?)",(buybookname,buyauthorname) )
#         conn.commit()
#         return render_template("purchase.html")
#     return "Book not found in avialable database "

# @app.route("/newadmin",methods=["GET","POST"])
# def newadmin():
#  if request.method=="POST":
#      username=request.form["username"]
#      password=request.form["password"]
#      conn.execute("insert into admindb(username,password) values(?,?)",(username,password))
#      conn.commit()
#      flash('New Admin Added in Database', 'error')
#      return render_template("adminloggedin.html")
#  return render_template("newadmin.html")

# @app.route("/uploadbook",methods=["GET","POST"])
# def uploadbook():
#  if request.method=="POST":
#      bookname=request.form["bookname"]
#      authorname=request.form["authorname"]
#      conn.execute("insert into availablebooksdb(bookname,authorname) values(?,?)",(bookname,authorname))
#      conn.commit()
#      flash('New Book Added in Database', 'error')
#      return render_template("adminloggedin.html")
#  return render_template("uploadbook.html")

# @app.route("/deletebook")
# def delete():
#     check=conn.execute("select * from availablebooksdb")
#     data=check.fetchall()
#     print(data)
#     return render_template("deletebook.html",datas=data)

# @app.route("/deleteprogress/<string:bookname>", methods=["GET","POST"])
# def deleteprogress(bookname):
#     conn.execute("delete from availablebooksdb where bookname=?",(bookname,))
#     conn.commit()
#     flash('Book deleted in Database', 'error')
#     return redirect("/deletebook")

# @app.route("/availablebook")
# def availablebook():
#     check=conn.execute("select * from availablebooksdb")
#     data=check.fetchall()
#     return render_template("availablebook.html",datas=data)

# if __name__== "__main__":
#     app.run(debug=True)
    


"Same as last program,added otp verification via mail"
from flask import Flask,render_template,request,url_for,session,redirect,flash
import random
import sqlite3
from flask import *
from flask_mail import Mail, Message

from threading import Thread

from app import app as flask_app
app=Flask(__name__)
def start_flask():
    flask_app.run()

app.secret_key = '122343434'
app.config["MAIL_SERVER"]="smtp.gmail.com"
app.config["MAIL_PORT"]=587
app.config["MAIL_USERNAME"]="gthunder298@gmail.com"
app.config["MAIL_PASSWORD"]="zpbs wjnx xkfz lndj"
app.config["MAIL_USE_TLS"]=True
mail=Mail(app)


conn=sqlite3.connect("Books.db",check_same_thread=False)
conn.execute("""create table if not exists userdb(id integer primary key autoincrement,username text,
             password text)""")
conn.execute("""create table if not exists admindb(id integer primary key autoincrement,username text,
             password text)""")
conn.execute("""create table if not exists availablebooksdb(id integer primary key autoincrement,
             bookname text,authorname text)""")
conn.execute("""create table if not exists soldbooksdb(id integer primary key autoincrement,
             bookname text,authorname text)""")


def generateotp():
    otp=random.randint(1000,9999)
    return str(otp)
    
def insertadmindata():
    username="venkatesan.uniq@gmail.com"
    password="12345678"
    conn.execute("insert into admindb(username,password) values(?,?)",(username,password))
    conn.commit()
def insertavailablebooks():
    book1="python"
    book2="java"
    author1="guido"
    author2="vann"
    conn.execute("insert into availablebooksdb(bookname,authorname) values(?,?)",(book1,author1))
    conn.execute("insert into availablebooksdb(bookname,authorname) values(?,?)",(book2,author2))
    conn.commit()

@app.route("/default")
def default():
    insertadmindata()
    insertavailablebooks()
    return render_template("home.html")

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/signin",methods=["GET","POST"])
def signin():
    if request.method=="POST":
        user=request.form["username"]
        passw=request.form["password"]
        session["username"]=user
        session["password"]=passw
    
        username=session["username"]
        otp=generateotp()
        msg=Message("OTP VERIFICATION ",sender="gthunder298@gmail.com",recipients=[username])
        msg.body=f"Your otp is {otp} "
        mail.send(msg)
        session["otp"]=otp
        return render_template("enterotp.html")
    else:
        
       return render_template("signin.html")


@app.route("/checkotp", methods=["POST"])
def checkotp():
    if "otp" in request.form:  # Check if "otp" is in the form data
        otp = request.form["otp"]  # Retrieve the OTP from the form data
        if "otp" in session and session["otp"] == otp:
              username=session["username"]
              password=session["password"]
              conn.execute("insert into userdb(username,password) values(?,?)",(username,password))
              conn.commit()
              message = "OTP verified successfully"
              flash("Account created Successfully","error")
              return redirect("/")
        else:
            message="OTP does not match"
            return render_template("signin.html")
    else:
        return "No OTP provided"


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/userlogin",methods=["GET","POST"])
def userlogin():
    if request.method=="POST":
        username=request.form["username"]
        password=request.form["password"]
        
        select=conn.execute("select * from userdb where username=? and password=?",(username,password))
        check=select.fetchone()
        # user1=check[1]
        # user2=check[2]
        # if username in check and password in check:
        if check:
            if username in check and password in check:
                check=conn.execute("select * from availablebooksdb")
                data=check.fetchall()
                return render_template("userloggedin.html",data=data)
        else:
                    return redirect(url_for("userlogin"))  
    return render_template("userlogin.html")
    
@app.route("/adminlogin",methods=["GET","POST"])
def adminlogin():
     if request.method=="POST":
        username=request.form["username"]
        password=request.form["password"]
        
        select=conn.execute("select * from admindb where username=? or password=?",(username,password))
        print("select",select)       
        check=select.fetchone()
        print("check:",check)
        if check:
            print("chek if statement")
            if username in check and password in check:
                return render_template("adminloggedin.html")
            else:
                flash('Invalid Admin user credentials', 'error')
                return redirect(url_for("adminlogin"))  
        else:
                return render_template("adminlogin.html")  
     return render_template("adminlogin.html")   
        
@app.route("/buybook/<string:book>")
def buybook(book):
    data2=conn.execute("select * from soldbooksdb where bookname=?",(book,) )
    verify=data2.fetchone()
    if verify:
        return "Selected Book is sold out"
    
    data=conn.execute("select * from availablebooksdb where bookname=?",(book,))
    check=data.fetchone()
    if check:
        buybookname= check[1]
        buyauthorname= check[2]
        conn.execute("insert into soldbooksdb(bookname,authorname) values(?,?)",(buybookname,buyauthorname) )
        conn.commit()
        return render_template("purchase.html")
    return "Book not found in avialable database "

@app.route("/newadmin",methods=["GET","POST"])
def newadmin():
 if request.method=="POST":
     username=request.form["username"]
     password=request.form["password"]
     conn.execute("insert into admindb(username,password) values(?,?)",(username,password))
     conn.commit()
     flash('New Admin Added in Database', 'error')
     return render_template("adminloggedin.html")
 return render_template("newadmin.html")

@app.route("/uploadbook",methods=["GET","POST"])
def uploadbook():
 if request.method=="POST":
     bookname=request.form["bookname"]
     authorname=request.form["authorname"]
     conn.execute("insert into availablebooksdb(bookname,authorname) values(?,?)",(bookname,authorname))
     conn.commit()
     flash('New Book Added in Database', 'error')
     return render_template("adminloggedin.html")
 return render_template("uploadbook.html")

@app.route("/deletebook")
def delete():
    check=conn.execute("select * from availablebooksdb")
    data=check.fetchall()
    print(data)
    return render_template("deletebook.html",datas=data)

@app.route("/deleteprogress/<string:bookname>", methods=["GET","POST"])
def deleteprogress(bookname):
    conn.execute("delete from availablebooksdb where bookname=?",(bookname,))
    conn.commit()
    flash('Book deleted in Database', 'error')
    return redirect("/deletebook")

@app.route("/availablebook")
def availablebook():
    check=conn.execute("select * from availablebooksdb")
    data=check.fetchall()
    return render_template("availablebook.html",datas=data)

if __name__== "__main__":
        # Start Flask app in a separate thread
   app.run(debug=True)
 
    




   