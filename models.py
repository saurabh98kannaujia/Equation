import numpy as np
import cmath
from flask import Flask,request,render_template

class Equation:

    def linerEquation_1(self):
        a1 = int(request.form['a_value'])
        b1 = int(request.form['b_value'])
        c1 = int(request.form['c_value'])

        a2 = int(request.form['a1'])
        b2 = int(request.form['b1'])
        c2 = int(request.form['c1'])
        if(a1 == a2 and b1==b2 and c1==c2):
            res = ["No result","No result"]
            return render_template ("res.html",res = res)
        else:
            result =[[0],[0]]
            Inv = np.array(
                    [
                        [a1,b1],
                        [a2,b2]
                    ]
                )
            X = (np.linalg.inv(Inv)).tolist()

            Y  = [[c1],[c2]]
           

             # iterate through rows of X
            for i in range(len(X)):
            # iterate through columns of Y
                for j in range(len(Y[0])):
                    # iterate through rows of Y
                        for k in range(len(Y)):
                            result[i][j] += X[i][k] * Y[k][j]

        print(result)
                # for r in result:
                #     print(r)
        print()
        m =float("".join(map(str,result[0])))
        n =float("".join(map(str,result[1])))
        y = "{:.2f}".format(n)
        x = "{:.2f}".format(m)
        res = [x,y]
        return res

    def linerEquation_2(self):
        a1 = int(request.form['a1'])
        b1 = int(request.form['b1'])
        c1 = int(request.form['c1'])
        d1 = int(request.form['d1'])

        a2 = int(request.form['a2'])
        b2 = int(request.form['b2'])
        c2 = int(request.form['c2'])
        d2 = int(request.form['d2'])

        a3 = int(request.form['a3'])
        b3 = int(request.form['b3'])
        c3 = int(request.form['c3'])
        d3 = int(request.form['d3'])

        if(a1 == a2 == a3 and b1==b2 ==b3 and c1==c2 and d1==d2):
            res = ["No result","No result"]
            return render_template ("res.html",res = res)
        else:    
            result =[[0],[0],[0]]
            Inv = np.array(
                        [
                            [a1,b1,c1],
                            [a2,b2,c2],
                            [a3,b3,c3]
                        ]
                    )
            X = (np.linalg.inv(Inv)).tolist()

            Y  = [[d1],[d2],[d3]]
            

            # iterate through rows of X
            for i in range(len(X)):
            # iterate through columns of Y
                for j in range(len(Y[0])):
                    # iterate through rows of Y
                        for k in range(len(Y)):
                            result[i][j] += X[i][k] * Y[k][j]

            print(result)
                    # for r in result:
                    #     print(r)
            print()
            m =float("".join(map(str,result[0])))
            n =float("".join(map(str,result[1])))
            o =float("".join(map(str,result[2])))
            x = "{:.2f}".format(m)
            y = "{:.2f}".format(n)
            z = "{:.2f}".format(o)
            
            res = [x,y,z]
            return res

    def QuadraticEquation(self):
        '''
            x = (-b**2 -+ ((b**2) - 4*a*c)**(1/2)) / 2*a

        '''
        a = int(request.form['a'])
        b = int(request.form['b'])
        c = int(request.form['c'])
        d = (b**2) - (4*a*c)
        x1 = (-b-cmath.sqrt(d))/(2*a)
        x2 = (-b+cmath.sqrt(d))/(2*a)
        res = [x1,x2]
        return res


class Matrics:
    def Additon(self):
        l = "mat_add"
        r = int(request.form['r'])
        c = int(request.form['c'])
        mat1 = []
        mat2 = []
        res1 = []
       
        n=0
       
        for i in range(r):
            temp1 = []
            temp2 = []
            res2 = []
            for j in range(c):
                a = "a"+str(i)+str(j)
                b = "b"+str(i)+str(j)
                m = int(request.form[a])
                n = int(request.form[b])
                if n == " " or n =="" and m == " " or m=="":
                    n = 0
                    m = 0
                    temp1.append(m)
                    temp2.append(n)
                else:   
                    temp1.append(int(request.form[a]))
                    temp2.append(int(request.form[b]))
                res2.append(0)
            mat1.append(temp1)
            mat2.append(temp2)
            res1.append(res2)
        
        # for i in range(r):
        #     for j in range(c):
        #         print(mat1[i][j], end = " ")

        # print("######")
        # for i in range(r):
        #     for j in range(c):
        #         print(mat2[i][j], end = " ")

        for i in range(len(mat1)):  
    
            for j in range(len(mat1[0])):
                res1[i][j] = mat1[i][j] + mat2[i][j]

        return res1

    def Multiplication(self):
        l = "mat_mul"
        r1 = int(request.form['r1'])
        c1 = int(request.form['c1'])
        r2 = int(request.form['r2'])
        c2 = int(request.form['c2'])
        X = []
        Y = []
        res1 = []
       
        n=0
       
        for i in range(r1):
            temp1 = []
            for j in range(c1):
                a = "a"+str(i)+str(j)
                temp1.append(int(request.form[a])) 
            X.append(temp1)

        for i in range(r2):
            temp2 = []
            for j in range(c2):
                b = "b"+str(i)+str(j)
                temp2.append(int(request.form[b])) 
            Y.append(temp2)

        for i in range(r1):
            res2 = []
            for j in range(c2):
                res2.append(0) 
            res1.append(res2)
           
        print(res1)
        print()
        print(X)
        print()
        print(Y)

        for i in range(len(X)):
            for j in range(len(Y[0])):
                for k in range(len(Y)):
                    res1[i][j] += X[i][k] * Y[k][j]
        print(res1)
        return res1

    def determinent(self):
        r = int(request.form['r'])
        c = int(request.form['c'])
        mat1 = []
        for i in range(r):
            temp1 = []
            for j in range(c):
                a = "a"+str(i)+str(j)
                m = int(request.form[a])      
                if  m == " " or m=="":
                    n = 0
                    m = 0
                    temp1.append(m)   
                else:   
                    temp1.append(int(request.form[a]))    
            mat1.append(temp1)
        print(mat1)
        arr = np.matrix(mat1)
        print("arr")
        print(arr)
        print("inv")
        print(np.linalg.det(arr))

        x = np.linalg.det(arr)
        print(x)
        return x

    def Inverse(self):
        l = "mat_inv"
        r = int(request.form['r'])
        c = int(request.form['c'])
        mat1 = []
        
        res1 = []
       
        n=0
       
        for i in range(r):
            temp1 = []
            
            res2 = []
            for j in range(c):
                a = "a"+str(i)+str(j)
               
                m = int(request.form[a])
                
                if n == " " or n =="" and m == " " or m=="":
                    n = 0
                    m = 0
                    temp1.append(m)
                   
                else:   
                    temp1.append(int(request.form[a]))
                   
                res2.append(0)
            mat1.append(temp1)
            res1.append(res2)
        print(mat1)
        arr = np.matrix(mat1)
        print("arr")
        print(arr)
        print("inv")
        print(np.linalg.inv(arr))
        x = (np.linalg.inv(arr)).tolist()
        return x


    def transpose(self):
        l = "mat_transpose"
        r = int(request.form['r'])
        c = int(request.form['c'])
        mat1 = []
        n=0
        for i in range(r):
            temp1 = [] 
            for j in range(c):
                a = "a"+str(i)+str(j)
                m = int(request.form[a])
                if n == " " or n =="" and m == " " or m=="":
                    n = 0
                    m = 0
                    temp1.append(m)
                else:   
                    temp1.append(int(request.form[a]))
            mat1.append(temp1)

        print(mat1)
        x = np.transpose(mat1)
        print(x)
        return x
    
    