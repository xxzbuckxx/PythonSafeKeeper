import time
import os
import sys
import random

##Variables##
    #Global#
firstime = True
Loggedon = False
    #Section#
newperson = True
search = False
login = False
#####################



##Functions## ###############################
    ##Jump 100 Lines
def cls():
    print "\n" * 100
    ##Print character by character
def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % (c))
        time.sleep(Sleeptime)

def home():
    global newperson
    global login
    global search
    newperson = False
    login = False
    search = True

def create_folder(name):
    if not os.path.exists(name):
        os.mkdir('%s' % name)

def create_file(destination, name, info):
    destination = "%s\\" %(destination)
    filname = "%s.txt" % (name)
    if not (os.path.exists(destination + filname)):
        f = open(destination + filname,'w')
        f.write("%s" % (info))
        f.close()

def edit_file(destination, name, line, newinfo):
    destination = "%s\\" % (destination)
    filename = "%s.txt" % (name)
    if os.path.exists(destination + filename):
        f = open(destination + filename,'r')
        Newline = f.readlines()
        Newline[line] = "%s" % (newinfo)
        f.close()
        os.remove(destination + filename)
        f = open(destination + filename, "a")
        for s in Newline:
            if not s == "\n" or s == "":
                f.write(s + "\n")
        f.close()

    
def remove_file(destination, name):
    destination = "%s\\" % (destination)
    filename = "%s.txt" % (name)
    if os.path.exists(destination + filename):
        os.remove(destination + filename)

def open_file(destination, name, rw):
    destination = "%s\\" % (destination)
    filename = "%s.txt" % (name)
    if os.path.exists(destination + filename):
        global f
        f = open(destination + filename, rw)

def exists(destination, name):
    destination = "%s\\" % (destination)
    filename = "%s.txt" % (name)
    os.path.exists(destination + filename)
#############################################



##Classes## #############################################################
    #Person Class#
class person:
    """                                                                 

    Personal Info and password
    """
    def __init__(self, fname, lname, age, gender, compname, password):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender
        self.compname = compname
        self.password = password
#########################################################################


#Loops Forever
while True:
    if firstime:
        create_folder('Accounts')
        create_folder('Variables')
        print "folders created"
        if os.path.exists("Variables\\Variables.txt"):
            print "variables folder exists"
            open_file('Variables', 'Variables', 'r')
            if not os.stat("Variables\\Variables.txt").st_size == 0:
                print "Variables folder not empty"
                f.read
                var = f.readlines()
                if var[0] == "setuptrue\n":
                    f.close()
                    time.sleep(.1)
                    cls()
                    home()
                f.close()
            else:
                print "variables folder empty"
                open_file("Variables","Variables","w")
                f.write("\nusers = []\nSleeptime = 0.01")
                f.close()
        else:
            print "Empty Variables folder"
            create_file("Variables", "Variables", "setupfalse\nusers = []\nSleeptime = 0.01")
        if exists("Accounts", "users"):
            open_file("Accounts","users","r")
            if os.stat("Accounts\\users.txt").st_size == 0:
                date = time.strftime("%m/%d/%y")
                f.write("created %s" % (date))
        else:
            date= time.strftime("%m/%d/%y")
            create_file("Accounts","users","created %s" % (date))
        open_file("Variables", "Variables", "r")
        varfile = f.readlines()
        print varfile
        exec(varfile[1])
        exec(varfile[2])
        f.close()
        firstime = False
    #New User Section#
    while newperson == True:
        
        #Jump 100 lines down (clear)
        cls()
        #First Name#
        delay_print("What is your first name?")
        fname = raw_input("\n: ")

        #Last Name#
        delay_print("And your last?")
        lname = raw_input("\n: ")

        #Gender#
        delay_print('Gender?')
        gender = raw_input("\n: ").lower()
        
        delay_print('Hello %s %s!\n' % (fname, lname))

        #Age#
        delay_print('How old are you %s?' % (fname))
        age = raw_input("\n: ")
        if age.isdigit():
            time.sleep(.01)
        else:
            age = 0
            delay_print("That's not an age!\n")
        #Turns string to interger to positive number (in case negative)
        age = int(age)
        age = abs(age)
        if gender == "male" or gender == "m":
            gender = "male"
            gendercalled = "boy"
                
        elif gender == "female" or gender == "f":
            gender = "female"
            gendercalled = "gal"
                
        else:
            gendercalled = gender
           
        if 0 < age < 18:
            delay_print("You're a very smol %s ain't ya? \n" % (gendercalled))
            
        elif age >= 18:
            delay_print("you a big %s aren't ya?! \n" % (gendercalled))

        else:
            delay_print("I Guess you just a special %s.\n" % (gendercalled))

        if gender != "male" and gender != "female":
            gender = "other"

        time.sleep(2)

        #Computer Name#
        delay_print("Well, it's about time I introduce myself, I'm... \n")
        time.sleep(2)
        delay_print("oh dear,")
        time.sleep(2)
        delay_print("\nIt seems I don't have a name....\n")
        Answer = False
        while Answer == False:
            delay_print("Can you name me?")
            Can = raw_input("\n: ").lower()
            Can.lower()
            if Can == "yes" or Can == "ya" or Can == "ye" or Can == "sure" or Can == "yas bitch, yas":
                delay_print("Thanks! \n")
                time.sleep(2)
                delay_print("So... what are you going to name me?")
                compname = raw_input("\n:")
                delay_print("%s? That's an interesting name...\n" % (compname))
                Answer = True

            elif Can == "no" or Can == "nah"  or Can == "hell no":
                delay_print("Then I guess I'll have to think of my own name. \nHow about...\n")
                time.sleep(3)
                rand = random.randint(0,9)
                randname = ['Bob', 'Vex', 'Joshua', 'Jorge', 'Martin', 'Pepper', 'Ginger', 'Ted', 'Watson', 'Esme']
                compname = randname[rand]
                delay_print("%s!" % (compname))
                time.sleep(1)
                delay_print(" Wow, I'm good at this!\n")
                time.sleep(1)
                Answer = True

                    
            else:
                delay_print("yes or no, \n")

        #Username & Password#
        delay_print("Oh ya! You're probably wondering why I'm here %s,\nand why I'm asking so many personal questions.\n" % (fname))
        time.sleep(2)
        delay_print("I'm A password keeper!\n")
        print("\n   Name: %s %s\n   Gender: %s\n   Age: %s\n\n         ~%s" % (fname, lname, gender, age, compname))
        delay_print("\nAbove is your account information.\nNow All you need is a Username and a password to finish setting up!\n")
        usernamepicked = False
        while usernamepicked == False:
            username = raw_input("username: ").lower()
            if any(username in s for s in users):
                delay_print("That username is taken! Try another one.\n")
            else:
                users.append(username)
                delay_print("Okay... Now a password?\n")
                usernamepicked = True
        
        edit_file("Variables","Variables",1,"users = %s" % users)  
        password = raw_input("Password: ")
        exec('%s = person("%s","%s","%s","%s","%s","%s")' % (username,fname,lname,age,gender,compname,password))
        edit_file("Variables","Variables",0,"setuptrue")
        
        
        delay_print("Remember your username and password!!! This is how you'll Login!\n")
        time.sleep(3)
        delay_print("Be careful, if you close this window your information will be lost forever!!!")
        time.sleep(3)
        cls()
        exec('global %s' % (username))
        search = True
        newperson = False


    #Search Section#
    while search == True:
        if Loggedon == False:
            delay_print("\n\n\n\nWhat would you like to do?\n")
            sys.stdout.write("Logged on:")
            if Loggedon == True:
                delay_print(" %s\n" % (user.fname))
            else:
                delay_print(" none\n")
            print "-----------------------"
            Option = ["1. New User", "2. Login", "3. About"]
            for str in Option:
                print str
                
            Choice = raw_input(": ").lower()

            #New User Choice#
            if Choice == "new user" or Choice == "newuser" or Choice == "1":
                delay_print("Are you sure?")
                sure = raw_input("\n: ").lower()
                if sure == "yes" or sure == "sure" or sure == "ya" or sure == "ye":
                    newperson = True
                    search = False
                

            #Login Choice#
            elif Choice == "login" or Choice == "2":
                delay_print("Are you sure?")
                sure = raw_input("\n: ").lower()
                if sure == "yes" or sure == "sure" or sure == "ya" or sure == "ye":
                    login = True
                    search = False

            #About Choice#
            elif Choice == "about" or Choice == "3":
                delay_print("Are you sure?")
                sure = raw_input("\n: ").lower()
                if sure == "yes" or sure == "sure" or sure == "ya" or sure == "ye":
                    about = True
                    search = False
                    
            #Command Prompt#
            elif Choice == "command prompt":
                command = raw_input()
                exec(command)

                
        elif Loggedon == True:
            delay_print("\n\n\n\nWhat would you like to do?\n")
            sys.stdout.write("Logged on:")
            delay_print(" %s\n" % (user.fname))
            print "-----------------------"
            Option = ["1. New User", "2. Logout", "3. About", "4. Safe Keep", "5. User Settings"]
            for str in Option:
                print str
                
            Choice = raw_input(": ").lower()

            #1. New User Choice#
            if Choice == "new user" or Choice == "1. new user" or Choice == "1":
                delay_print("Are you sure?")
                sure = raw_input("\n: ").lower()
                if sure == "yes" or sure == "sure" or sure == "ya" or sure == "ye":
                    newperson = True
                    search = False
                

            #2. Login Choice#
            elif Choice == "logout" or Choice == "2" or Choice == "2. logout":
                delay_print("Are you sure?")
                sure = raw_input("\n: ").lower()
                if sure == "yes" or sure == "sure" or sure == "ya" or sure == "ye":
                    login = True
                    search = False

            #3. About Choice#
            elif Choice == "about" or Choice == "3" or Choice == "3. about":
                delay_print("Are you sure?")
                sure = raw_input("\n: ").lower()
                if sure == "yes" or sure == "sure" or sure == "ya" or sure == "ye":
                    about = True
                    search = False

            #4. Safe Keep Choice#

            #5. User Settings Choice#
                    
            #Command Prompt#
            elif Choice == "command prompt":
                command = raw_input()
                exec(command)

    cls()
    
    while login == True:
        if Loggedon == False:
            isuser = True
            print "\n\n\n\n"
            delay_print("What is your username?\n")
            unameinput = raw_input(": ").lower()
            exec("user = '%s'" % (unameinput))
            if any(user in s for s in users) and isuser:
                exec("user = %s" % (unameinput))
                delay_print("Sup %s! \n" % (user.fname))
                time.sleep(1)
                delay_print("You are %s right?" % (user.fname))
                confirmuser = raw_input("\n: ")
                if confirmuser == "yes" or confirmuser == "sure" or confirmuser == "ya" or confirmuser == "ye":
                    trypassword = True
                else:
                    isuser = False
                    trypassword = False
                while trypassword == True:
                    delay_print("Remember your password?")
                    password = raw_input("\n: ")
                    if password == user.password:
                        delay_print("That's right!\n")
                        time.sleep(2)
                        global user
                        Loggedon = True
                        trypassword = False
                        isuser = False
                        home()
                        Option.append("5. User Settings")
                        cls()
                    else:
                        delay_print("No, that's not it...\n")
                        delay_print("Would you like to try again?")
                        retrypassword = raw_input("\n: ")
                        if retrypassword == "yes" or retrypassword == "sure" or retrypassword == "ya" or retrypassword == "ye":
                            delay_print("Okay,\n\n\n\n")
                            time.sleep(1)
                        else:
                            trypassword = False

            else:
                print "User not found"
                delay_print("would you like to try again?")
                confirmpassword = raw_input("\n: ")
                if confirmpassword == "yes" or confirmpassword == "sure" or confirmpassword == "ya" or confirmpassword == "ye":
                    time.sleep(1)
                else:
                    home()
        elif Loggedon == True:
            delay_print("\n\n\nYou Sure you want to Log out?")
            logoutconfirm = raw_input("\n: ")
            if logoutconfirm == "yes" or logoutconfirm == "sure" or logoutconfirm == "ya" or logoutconfirm == "ye":
                user = ""
                Loggedon = False
    cls()
                

    open_file("Variables","Variables","r")
    info = f.read
    if any("\n\n" in s for s in info):
        print "DAINDOADFNII WHY"






