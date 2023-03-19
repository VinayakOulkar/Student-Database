import mysql.connector

choice=1
while(choice==1): #Loop runs till the user's choice is 1

    print("1.Select\n2.Insert\n3.Update\n4.Delete")
    req=int(input("Enter your Choice:"))

    #Connection to DB
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="studentdb")
    mycursor = mydb.cursor(buffered=True)


    if(req==1):   # Select Block

        mycursor.execute("SELECT * FROM student")
        res=mycursor.fetchall()
        print("RollNO\t\tNAME\tAGE")
        for i in res:
            print("  ",i[0],"\t",i[1],"\t",i[2])
        mydb.close()

    elif(req==2): # Insert Block

            t=0
            RollNo = int(input("Enter Student Rno:"))
            name=input("Enter Student Name:")
            age=int(input("Enter Student Age:"))
            per=int(input("Enter Percentage:"))
            query="SELECT RollNO from student where RollNO={}".format(RollNo)

            mycursor.execute(query)

            if(mycursor.rowcount == 0): #If RollNo is Not Already Existing than new Data can is Added
                query="INSERT INTO STUDENT VALUE({},'{}',{},{})".format(RollNo,name,age,per)
                mycursor.execute(query)
                mydb.commit()
            else:
                print("RollNo can be Same,Your Entered RollNo already Exists")


    elif(req==3): #Update Block

        RollNo=int(input("Enter Student RollNo of which Updation is to be Done:"))
        print("1.Name\n2.Age\n3.Percentage")

        req=int(input()) #User's Choice for Updating Particular Field

        if(req==1): #Name Updation
            name=input("Enter New Name:")
            query="UPDATE student SET NAME='{}' WHERE RollNO={};".format(name,RollNo)
            mycursor.execute(query)
            mydb.commit()

        elif(req==2): #Age Updation
            age=int(input("Enter New Age:"))
            query = "UPDATE student SET AGE='{}' WHERE RollNO={};".format(age, RollNo)
            mycursor.execute(query)
            mydb.commit()

        elif(req==3): #Percentage Updation
            per=int(input("Enter New Percentage:"))
            query = "UPDATE student SET PERC='{}' WHERE RollNO={};".format(per, RollNo)
            mycursor.execute(query)
            mydb.commit()

        else:
            print("Invalid Input!")

    elif(req==4): #Delete Block
        RollNo=int(input("Enter The RollNo to Delete the Data:"))
        query="SELECT RollNO from student WHERE RollNO={}".format(RollNo)
        mycursor.execute(query)

        if(mycursor.rowcount>0):  #If RollNO exists than Deletion is done
            query = "DELETE FROM student WHERE RollNO={}".format(RollNo)
            mycursor.execute(query)
            mydb.commit()
            # print("Hi")
        else:
            print("Entered RollNo does not exist!!!")



    choice = int(input("Do you want to Continue(1/0):"))
    mydb.close() #DB Connection Close

print("-------PROGRAM TERMINATED--------")


