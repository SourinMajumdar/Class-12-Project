#Creating the database
import mysql.connector as mc
mydb = mc.connect(host="localhost",user="root",password="sourin")
mycursor = mydb.cursor()
mycursor.execute("create database if not exists sourin2")
mycursor.execute("use sourin2")

#Creating the required tables
mycursor.execute("create table if not exists flight(fl_no varchar(10) primary key, fl_name varchar(15), source varchar(20), destination varchar(20),tod varchar(10), toa varchar(10), fare decimal(6))")
mycursor.execute("create table passenger (p_id varchar(30), p_name varchar(30), address varchar(50), phone varchar(12), fl_no varchar(10), pnr varchar(11))")
mycursor.execute("create table booking(fl_no varchar(10), fl_name varchar(15), source varchar(20), destination varchar(20),tod varchar(10), toa varchar(10),p_name varchar(30), address varchar(50), phone varchar(12),nop varchar(5),fare decimal(10))")

=========================================================================================================================================================================================================================================================


def mainmenu():
    c = 'y'
    while c == 'y':
        print("MAIN MENU")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        x = input("Enter your choice: ")
        print("")
        if x   == '1':
            adminmenu()
        elif x == '2':
            usermenu()
        elif x == '3':
            exit(0)
        else:
            print("Invalid choice.")
            print("")
            c = input("Do you wish to continue? - yes / no : ")
            print("")
            if c == 'yes':
                mainmenu()
            else:
                exit(0)


#_______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


def adminmenu():
    c = 'y'
    while c == 'y':
        print("ADMIN MENU")
        print("1. Create a flight record")
        print("2. Display flight records")
        print("3. Update a record")
        print("4. Delete a record")
        print("5. Back to main menu.")
        x = input("Enter your choice: ")
        print("")
        if x   == '1':
            create_flight_record()
        elif x == '2':
            display_flight_record()
        elif x == '3':
            update_flight_record()
        elif x == '4':
            delete_flight_record()
        elif x == '5':
            mainmenu()
        else:
            print("Invalid input")
            print("")
            input("Press ENTER to go back to admin menu...")
            print("")
            adminmenu()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
def usermenu():
    c = 'y'
    while c == 'y':
        print("USER MENU")
        print("1. Create a passenger record")
        print("2. Delete a record")
        print("3. Update a record")
        print("4. Search")
        print("5. Booking")
        print("6. Cancellation")
        print("7. Back to main menu.")
        x = input("Enter your choice: ")
        print("")
        if x   == '1':
            create_passenger_record()
        elif x == '2':
            delete_passenger_record()
        elif x == '3':
            update_passenger_record()
        elif x == '4':
            search()
        elif x == '5':
            Booking()
        elif x == '6':
            Cancellation()
        elif x == '7':
            mainmenu()
        else:
            print("Invalid input !")
            print("")
            input("Press ENTER to go back to user menu...")
            print("")
            usermenu()

#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


def create_flight_record():
        try:
            import mysql.connector as mc
            mydb        = mc.connect(host="localhost", user="root",password="sourin",database="sourin2")
            mycursor    = mydb.cursor()
            fl_no       = input("Enter flight number      : ")
            fl_name     = input("Enter airline name       : ")
            source      = input("Flight taking off from   : ")
            destination = input("Flight going to          : ")
            tod         = input("Time of departure        : ")
            toa         = input("Time of arrival          : ")
            fare        = input("Flight fare:             : ")
            print("")
            sql = "insert into flight (fl_no,fl_name,source,destination,tod,toa,fare) values(%s,%s,%s,%s,%s,%s,%s)"
            val = (fl_no,fl_name,source,destination,tod,toa,fare)
            mycursor.execute(sql,val)
            mydb.commit()
            print("----------------------------------")
            print("FLIGHT RECORD CREATED SUCCESSFULLY ! ")
            print("----------------------------------")
            print("")
            input("Press ENTER to continue...")
            print("")
        except Exception as e:
            print(e)

#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

        
def update_flight_record():
    try:
        import mysql.connector as mc
        mydb     = mc.connect(host="localhost", user="root",password="sourin",database="sourin2")
        mycursor = mydb.cursor()
        print("Flight Data Modification -")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^")
        display_in_mod_and_del1()
        FN       = input("Enter the flight number of the row you want to modify: ")
        print('')
        print("Your selected row :")
        sql = "select * from flight where fl_no=(%s)"
        val = [(FN)]
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        for x in result:
            print(x)
        print('')
        c = input("Are you sure you want to modify this record? - yes / no :  ")
        print("")
        if c == 'yes':
            fl_no       = input("Enter flight number      : ")
            fl_name     = input("Enter airline name       : ")
            source      = input("Flight taking off from   : ")
            destination = input("Flight going to          : ")
            tod         = input("Time of departure        : ")
            toa         = input("Time of arrival          : ")
            fare        = input("Flight fare:             : ")
            print("")
            sql = "update flight set fl_no=(%s), fl_name=(%s),source=(%s),destination=(%s),tod=(%s),toa=(%s),fare=(%s) where fl_no=(%s)"
            val = (fl_no,fl_name,source,destination,tod,toa,fare,FN)
            mycursor.execute(sql,val)
            mydb.commit()
            print("------------------------------------")
            print("FLIGHT RECORD UPDATED SUCCESSFULLY !")
            print("------------------------------------")
            print("")
            input("Press ENTER to continue")
            print("")
        elif c == 'no':
            input("Press ENTER to go back to admin menu...")
            print("")
        else:
            print("Invalid input.")
            input("Press ENTER to go back to admin menu...")
            print("")
    except Exception as e:
        print(e)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def display_flight_record():
        try:
            import mysql.connector as mc
            mydb     = mc.connect(host="localhost", user="root",password="sourin",database="sourin2")
            mycursor = mydb.cursor()
            mycursor.execute("Select * from flight")
            result   = mycursor.fetchall()
            l        = len(result)
            if l>0:
                print("")
                print("Flight Records")
                print("--------------")
                print("")
                for x in result:
                    print(x)
                    print("")
                input("Press ENTER to go back to admin menu...")
                print("")
            else:
                print("No records.")
                input("Press ENTER to go back to admin menu...")
                print("")
        except Exception as e:
            print(e)

#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


def display_in_mod_and_del1():
    try:
        import mysql.connector as mc
        mydb     = mc.connect(host="localhost", user="root", password="sourin", database="sourin2")
        mycursor = mydb.cursor()
        mycursor.execute("Select * from flight")
        result   = mycursor.fetchall()
        l        = len(result)
        if l > 0:
            print("")
            print("Flight Records present in database")
            print("----------------------------------")
            print("")
            for x in result:
                print(x)
                print("")
    except Exception as e:
        print(e)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def delete_flight_record():
    try:
        import mysql.connector as mc
        mydb     = mc.connect(host="localhost", user="root",password="sourin",database="sourin2")
        mycursor = mydb.cursor()
        display_in_mod_and_del1()
        fl_no    = input("Enter flight number of the row you want to delete : ")
        print('')
        print("Your selected row :")
        sql = "select * from flight where fl_no=(%s)"
        val = [(fl_no)]
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        for x in result:
            print(x)
        print('')
        c        = input("Are you sure you want to delete this record ? - yes / no : ")
        print("")
        sql      = "delete from flight where fl_no=(%s)"
        delete   = [(fl_no)]
        if c=='yes':
            mycursor.execute(sql,delete)
            mydb.commit()
            print("------------------------------------")
            print("FLIGHT RECORD DELETED SUCCESSFULLY !")
            print("------------------------------------")
            print("")
            input("Press ENTER to go back to admin menu...")
            print("")
        else:
            print("Flight record not deleted.")
            print("")
            input("Press ENTER to go back to admin menu...")
            print("")
    except Exception as e:
        print(e)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def create_passenger_record():
    try:
        import mysql.connector as mc
        mydb     = mc.connect(host="localhost", user="root",password="sourin",database="sourin2")
        mycursor = mydb.cursor()
        p_id     = input("Enter the passenger ID (Aadhar no. / PAN / Passport no. / Driving license no. / Voter id no.): ")
        p_name   = input("Enter passenger's name           : ")
        address  = input("Residential address of passenger : ")
        phone    = input("Passenger phone number           : ")
        fl_no    = input("Passenger's flight number        : ")
        pnr      = input("Passenger's PNR number           : ")
        print("")
        sql      = "insert into passenger (p_id,p_name,address,phone,fl_no,pnr) values(%s,%s,%s,%s,%s,%s)"
        val      = (p_id,p_name,address,phone,fl_no,pnr)
        mycursor.execute(sql,val)
        mydb.commit()
        print("---------------------------------------")
        print("PASSENGER RECORD CREATED SUCCESSFULLY !")
        print("---------------------------------------")
        print("")
        input("Press ENTER to continue...")
        print("")
    except Exception as e:
        print(e)

#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


def delete_passenger_record():
    try:
        import mysql.connector as mc
        mydb     = mc.connect(host="localhost", user="root", password="sourin", database="sourin2")
        mycursor = mydb.cursor()
        display_in_mod_and_del2()
        p_id      = input("Enter passenger id of the row you want to delete : ")
        print("")
        print("Yor selected row :")
        sql = "select * from passenger where p_id=(%s)"
        val = [(p_id)]
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        for x in result:
            print(x)
        print("")
        c        = input("Are you sure you want to delete this record ? - yes / no : ")
        print("")
        sql      = "delete from passenger where p_id=(%s)"
        delete   = [(p_id)]
        if c == 'yes':
            mycursor.execute(sql, delete)
            mydb.commit()
            print("---------------------------------------")
            print("PASSENGER RECORD DELETED SUCCESSFULLY !")
            print("---------------------------------------")
            print("")
            input("Press ENTER to go back to user menu...")
            print("")
        else:
            print("Flight record not deleted.")
            print("")
            input("Press ENTER to go back to user menu...")
            print("")
    except Exception as e:
        print(e)

        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def update_passenger_record():
    try:
        import mysql.connector as mc
        mydb     = mc.connect(host="localhost", user="root",password="sourin",database="sourin2")
        mycursor = mydb.cursor()
        print("Passenger Record Modification")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("")
        display_in_mod_and_del2()
        print("")
        PID  = input("Enter the Passenger ID of the row you want to modify: ")
        print("")
        print("Your selected row : ")
        sql = "select * from passenger where p_id=(%s)"
        val = [(PID)]
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        for x in result:
            print(x)
        print("")
        c = input("Are you sure you want to modify this record? - yes / no :  ")
        print("")
        if c == 'yes':
            p_id=input("Enter the passenger ID (Aadhar No. / PAN / Passport no. / Driving license no. / Voter id no.): ")
            p_name  = input("Enter passenger name               : ")
            address = input("Residential addresss of passenger  : ")
            phone   = input("Passenger phone number             : ")
            fl_no   = input("Passenger's flight number          : ")
            pnr     = input("Passenger's PNR number             : ")
            sql="update passenger set p_id=(%s), p_name=(%s), address=(%s), phone=(%s), fl_no=(%s),pnr=(%s) where p_id=(%s)"
            val = (p_id,p_name,address,phone,fl_no,pnr,PID)
            mycursor.execute(sql,val)
            mydb.commit()
            print("")
            print("---------------------------------------")
            print("PASSENGER RECORD UPDATED SUCCESSFULLY !")
            print("---------------------------------------")
            print("")
            input("Press ENTER to continue...")
            print("")
        elif c == 'no':
            input("Press ENTER to go back to user menu...")
            print("")
        else:
            print("Invalid input.")
            input("Press ENTER to continue...")
            print("")
    except Exception as e:
        print(e)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def display_in_mod_and_del2():
    try:
        import mysql.connector as mc
        mydb     = mc.connect(host="localhost", user="root", password="sourin", database="sourin2")
        mycursor = mydb.cursor()
        mycursor.execute("Select * from passenger")
        result   = mycursor.fetchall()
        l        = len(result)
        if l > 0:
            print("")
            print("Passenger Records present in database")
            print("-------------------------------------")
            print("")
            for x in result:
                print(x)
                print("")
    except Exception as e:
        print(e)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def search():
    c = 'y'
    while c == 'y':
        print("FLIGHT-SEARCH MENU")
        print("^^^^^^^^^^^^^^^^^^")
        print("")
        print("How would you like to search flights ? ")
        print("")
        print("1. By flight number")
        print("2. By flight name")
        print("3. By source and destination")
        print("- Press 'e' to go back to user menu.")
        print("")
        x = input("Enter your choice :")
        print("")
        if x == '1':
            search_by_flno()
        elif x == '2':
            search_by_fname()
        elif x == '3':
            search_by_sd()
        elif x =='e':
            usermenu()
        else:
            print("Invalid input !")
            print("")
            c = input("Do you wish to try again ? - yes / no : ")
            print("")
            if c=='yes':
                search()
            else:
                usermenu()


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def search_by_flno():
    try:
        import mysql.connector as mc
        mydb     = mc.connect(host="localhost", user="root", password="sourin", database="sourin2")
        mycursor = mydb.cursor()
        fl_no    = input("Enter flight number : ")
        sql      = "select * from flight where fl_no=(%s)"
        val      = [(fl_no)]
        mycursor.execute(sql,val)
        result   = mycursor.fetchall()
        l = len(result)
        if l > 0:
            print("")
            print("Your searched flight records : ")
            print("")
            for x in result:
                print(x)
                print("")
            input("Press ENTER to go back to search menu...")
            print("")
        else:
            print("No records.")
            input("Press ENTER to go back to search menu...")
            print("")
    except Exception as e:
        print(e)


#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


def search_by_fname():
    try:
        import mysql.connector as mc
        mydb = mc.connect(host="localhost", user="root", password="sourin", database="sourin2")
        mycursor = mydb.cursor()
        fl_name = input("Enter flight name : ")
        sql = "select * from flight where fl_name=(%s)"
        val = [(fl_name)]
        mycursor.execute(sql,val)
        result = mycursor.fetchall()
        l = len(result)
        if l > 0:
            print("")
            print("Your searched flight records : ")
            print("")
            for x in result:
                print(x)
                print("")
            input("Press ENTER to go back to search menu...")
            print("")
        else:
            print("No records.")
            input("Press ENTER to go back to search menu...")
            print("")
    except Exception as e:
        print(e)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def search_by_sd():
    try:
        import mysql.connector as mc
        mydb        = mc.connect(host="localhost", user="root", password="sourin", database="sourin2")
        mycursor    = mydb.cursor()
        source      = input("Enter the source of flight : ")
        destination = input("Enter flight destination   : ")
        sql         = "select * from flight where source=(%s) and destination=(%s)"
        val         = (source,destination)
        mycursor.execute(sql,val)
        result      = mycursor.fetchall()
        l = len(result)
        if l > 0:
            print("")
            print("Your searched flight records : ")
            print("")
            for x in result:
                print(x)
                print("")
            input("Press ENTER to go back to search menu...")
            print("")
        else:
            print("")
            print("No flights.")
            print("")
            input("Press ENTER to go back to search menu...")
            print("")
    except Exception as e:
        print(e)


#========================================================================================================================================================================================================================================================


def fl_disp_in_booking():
    try:
        import mysql.connector as mc
        mydb = mc.connect(host="localhost", user="root", password="sourin", database="sourin2")
        mycursor = mydb.cursor()
        source = input("Enter the source of flight : ")
        destination = input("Enter flight destination   : ")
        sql = "select * from flight where source=(%s) and destination=(%s)"
        val = (source, destination)
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        l = len(result)
        if l > 0:
            print("")
            print("Flights available: ")
            print("")
            for x in result:
                print(x)
                print("")
            print("")
        else:
            print("")
            print("No flights available.")
            print("")
            input("Press ENTER to go back to User menu...")
            print("")
            usermenu()
    except Exception as e:
        print(e)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def Booking():
    try:
        import mysql.connector as mc
        mydb = mc.connect(host="localhost", user="root", password="sourin", database="sourin2")
        mycursor = mydb.cursor()
        print("Flight Booking")
        print("^^^^^^^^^^^^^^")
        print("")
        fl_disp_in_booking()
        print("Choose your flight :")
        print("")
        fl_no       = input("Enter your flight number         : ")
        print("")
        print("Your chosen flight: ")
        sql1 = "select * from flight where fl_no=(%s)"
        val1 = [(fl_no)]
        mycursor.execute(sql1, val1)
        result = mycursor.fetchall()
        for x in result:
            print(x)
        print("")
        fl_name     = input("Enter airline name               : ")
        source      = input("Flight taking off from           : ")
        destination = input("Flight going to                  : ")
        tod         = input("Time of departure                : ")
        toa         = input("Time of arrival                  : ")
        perheadfare = int(input("Flight fare:                     : "))
        nop         = int(input("Number of passengers             : "))
        fare        = nop*perheadfare
        p_name      = input("Enter your name (Passenger - 1)  : ")
        phone       = input("Enter your phone number          : ")
        address     = input("Enter your address               : ")
        age         = input("Enter your age                   : ")
        print("")
        if nop>1:
            print("Enter other passengers' details below: ")
            print("")
            for i in range(nop-1):
                print("Passenger - ", i+2)
                pname   = input("Enter passenger's name           : ")
                address_= input("Residential address of passenger : ")
                age_    = input("Age in years       : ")
                phoneno = input("Enter phone number : ")
                print("")
        else:
            pass
        sql = "insert into booking (fl_no,fl_name,source,destination,tod,toa,p_name,address,phone,nop,fare) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (fl_no,fl_name,source,destination,tod,toa,p_name,address,phone,nop,fare)
        c = input("Confirm booking ? yes / no       : ")
        print("")
        if c == 'yes':
            mycursor.execute(sql, val)
            mydb.commit()
            print("THANK YOU FOR CHOOSING", fl_name.upper(),"!")
            print("")
            print("See you next time ...")
            print("")
            input("Press ENTER to go back to user menu...")
            print("")
        else:
            print("Try next time...")
            print("")
            input("Press ENTER to go back to user menu...")
            print("")
    except Exception as e:
        print(e)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def Cancellation():
    try:
        import mysql.connector as mc
        mydb = mc.connect(host="localhost", user="root", password="sourin", database="sourin2")
        mycursor = mydb.cursor()
        print("Flight Cancellation")
        print("^^^^^^^^^^^^^^^^^^^")
        print("")
        fl_no = input("Enter your flight number : ")
        print("")
        sql = "select * from booking where fl_no=(%s)"
        val = [(fl_no)]
        mycursor.execute(sql,val)
        result = mycursor.fetchall()
        for x in result:
            print(x)
        print("")
        c = input("Are you sure you want to cancel this flight ? yes / no : ")
        print("")
        if c == 'yes':
            sql1   = "delete from booking where fl_no=(%s)"
            delete = [(fl_no)]
            mycursor.execute(sql1,delete)
            mydb.commit()
            print("FLIGHT CANCELLED")
            print("")
            input("Press ENTER to go back to user menu...")
            print("")
        else:
            print("Try again later...")
            print("")
    except Exception as e:
        print(e)

mainmenu()
