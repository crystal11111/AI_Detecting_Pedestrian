import sqlite3, random

connection = None
cursor = None

def connect(database):
    global connection, cursor
    
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA foreign_keys=ON; ')
    connection.commit()
    return


def tables():
    global connection, cursor
    

    #query = 
    cursor.executescript(query)
    connection.commit()

def generateUsrID(name):
    global connection, cursor

    #generate a user ID
    while True:
        name = name.lower()
        name = name.replace(" ", "")
        randomNum = random.randint(1, 9999)
        usrId = name + str(randomNum)

        #check if user ID already exists
        cursor.execute("SELECT * FROM users WHERE usr = ?", (usrId,)) #is the comma necessary after usrId???????
        usrExists = cursor.fetchone()

        if usrExists is None: #or should it be ==0 ????
            return usrId

def main():
    global connection, cursor

    #create login screen
    loginSuccessful = False
    while loginSuccessful == False:

        #check if user is registered
        userInput = input('Select 1 if you are a registered user \n 2 if you are a unregistered user \n 3 if you would like to the program.\n')

        #login if registered
        if int(userInput) == 1:
            usrId = input('Enter user id: ')
            password = input('Enter password: ')

            #checks validity of input
            cursor.execute(
                "SELECT * FROM users WHERE usr = ? AND pwd = ?;",
                (usrId, password),
            )
            validInput = cursor.fetchone()

            if validInput is not None: #or should it be !=0?????
                loginSuccessful = True
            else:
                print("Invalid user id or password, try again.")

        #sign up if unregistered
        elif int(userInput) == 2:
            name = input('Enter name: ')
            email = input('Enter email: ')
            city = input('Enter city: ')
            timezone = input('Enter timezone: ')
            password = input('Create password: ')
            usrId = generateUsrID(name)

            #add user to the database
            insertions = [(usrId, password, name, email, city, timezone)]

            cursor.execute(
                "INSERT INTO users VALUES (?, ?, ?, ?, ?, ?);",
                insertions,
            )

            loginSuccessful = True

        #exit
        elif int(userInput) == 3:
            print("Program closing.")
            break

        #re prompt if invalid input
        else:
            print("Invalid entry, try again.") 
    
    # read file containing queries for tables
    # then pass to define_tables()
    # then execute queries

    connection.commit()
    connection.close()
    return

if __name__ == "__main__":
    main()
