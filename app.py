from flask import Flask,render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
from numpy import matrix
import pymongo
from models import Equation,Matrics

import bcrypt

app = Flask(__name__)

conn_str = "mongodb+srv://spgamer9898:8291651056@demo.ozx5y.mongodb.net/demo?retryWrites=true&w=majority"
# set a 5-second connection timeout
# mongo = pymongo.MongoClient("mongodb+srv://spgamer9898:829165156@demo.ozx5y.mongodb.net/demo?retryWrites=true&w=majority")
# db = client.test
mongo = pymongo.MongoClient(conn_str)
db = mongo["DemoDB"]
col = db["demo"]
# post = {"name":"demo","process":"done"}
# col.insert_one(post)
# try:
#     print(col.find_one())
# except Exception:
#     print("not connect")


@app.route("/")
def index():
    if 'username' in session:
        s = session['username']
        return render_template("main.html",s = s)

    return render_template('index.html')

@app.route("/logout",methods=['POST'])
def logout():
    if request.method=='POST':
        session.clear()
        return redirect('/') 

@app.route('/login', methods=['POST'])
def login():
    
    login_user = col.find_one({'uname' : request.form['username']})

    if login_user:
        if request.form['pass']== login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('index'))

    return 'Invalid username/password combination'

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        
        existing_user = col.find_one({'uname' : request.form['username']})

        if existing_user is None:
            # hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            col.insert({'uname' : request.form['username'], 'password' : request.form['pass'],'name' : request.form['name']})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        return 'That username already exists!'

    return render_template('register.html')


@app.route("/res", methods = ["POST","GET"])
def res():
    if request.method == "POST":
        main_id = request.form['main_id']
        
        #For Linear Equation 1
        if main_id == "1":
            res = Equation().linerEquation_1()
            print(res)
            print(len(res))
            l = len(res)
            return render_template ("res.html",res = res,l = l)
       
        #For Linear Equation 2
        elif main_id == "2":
            res = Equation().linerEquation_2()
            print(res)
            print(len(res))
            l = len(res)
            return render_template ("res.html",res = res,l = l)

        #For Qudratic Equation
        elif main_id == "3":
            res = Equation().QuadraticEquation()
            l = 4
            return render_template ("res.html",res = res,l = l)   

              

@app.route("/mat_res",methods=["POST","GET"])
def mat():   
    if request.method == "POST":
        l = "mat_add"
        res1 = Matrics().Additon()
        for r in res1:
            print(r)
        l1 = len(res1[0])
        le1 = len(res1) 
        
        return render_template("res.html",res1 = res1,l = l,le = l1,le1 = le1)

@app.route("/mat_mul",methods=["POST","GET"])
def mat_mul():   
    if request.method == "POST":
        l = "mat_mul"
        res1 = Matrics().Multiplication()
        for r in res1:
            print(r)
        l1 = len(res1[0])
        le1 = len(res1)
        
        return render_template("res.html",res1 = res1,l = l,le = l1,le1 = le1)

@app.route("/mat_inv",methods = ["POST","GET"])
def mat_inv():
    if request.method == "POST":
        l = "mat_inv"
        res1 = Matrics().Inverse()
        l1 = len(res1[0])
        le1 = len(res1)
        return render_template("res.html",res1 = res1,l = l,le = l1,le1 = le1)

@app.route('/mat_draw',methods=["POST","GET"])
def mat_draw():
    if "username" in session:
        if request.method == "POST":
            matrix_d = request.form['mat_draw']
            if matrix_d == "matrix_add":
                r = int(request.form['r'])
                c = int(request.form['c'])
                a = "a"
                b = "b"
                return render_template("matrix_draw.html",matrix_d = matrix_d, r=r,a=a,b=b,c = c)
            
            elif matrix_d == "matrix_mul":
                r1 = int(request.form['r1'])
                c1 = int(request.form['c1'])
                r2 = int(request.form['c1'])
                c2 = int(request.form['c2'])
                a = "a"
                b = "b"
                return render_template("matrix_draw.html",matrix_d = matrix_d ,r1=r1,a=a,b=b,c1 = c1,c2=c2,r2=r2)
            
            elif matrix_d == "matrix_inv":
                r = int(request.form['r'])
                c = int(request.form['r'])
                a = "a"
                b = "b"
                return render_template("matrix_draw.html",matrix_d = matrix_d, r=r,a=a,b=b,c = c)
                         
    return redirect('/') 


@app.route('/mat_det_draw',methods=["POST","GET"])
def mat_det_draw():
    if "username" in session:
        if request.method == "POST":
            matrix_d = "matrix_det"
            r = int(request.form['r'])
            c = int(request.form['c'])
            if r < 2 :
                err = "Row should be greater then 2"
                return render_template("main.html",matrix_d = matrix_d,err = err)
            elif c < 2 :
                err = "Column should be greater then 2"
                return render_template("main.html",matrix_d = matrix_d,err = err)
            elif r!=c:
                err = "It is not a square matrix Row and Column must be equal.!"
                return render_template("main.html",matrix_d = matrix_d,err = err)
            
            else:
                a = "a"
                b = "b"
                return render_template("matrix_draw.html",matrix_d = matrix_d, r=r,a=a,b=b,c = c)
    return redirect('/')

@app.route('/mat_det',methods=["POST","GET"])
def mat_det():
    if request.method == "POST":
        l = "mat_det"
        res1 = Matrics().determinent()
        return render_template("res.html",res1 = res1,l = l)


@app.route("/mat_transpose_ans",methods = ["POST","GET"])
def mat_transpose_ans():
    if request.method == "POST":
        l = "mat_transpose"
        res1 = Matrics().transpose()
        l1 = len(res1[0])
        le1 = len(res1)
        return render_template("res.html",res1 = res1,l = l,le = l1,le1 = le1)

@app.route('/mat_transpose',methods = ["POST","GET"])
def mat_transpose():
    if "username" in session:
        if request.method == "POST":
            matrix_d = request.form['mat_draw']
            r = int(request.form['r'])
            c = int(request.form['c'])
            a = "a"
            b = "b"
            return render_template("matrix_draw.html",matrix_d = matrix_d, r=r,a=a,b=b,c = c)




if __name__ == "__main__":
    app.secret_key = 'mysecret'
    app.run(debug=True)



    
    '''
# api.add_resource(route.Login,'/<string:name>')
# api.add_resource(route.Register,'/Reg')
# # api.add_resource(route.Read,'/home')

# api.add_resource(route.Demo.Home,"/home"
# )
# def home():
#     return render_template("index.html")

    '''