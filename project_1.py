'''
Create a Class Ticketbooking

i)Bookticket
ii)Removeticket


Available tickets
i)Bookticket


Get email address as username

a)List of movies
To choose the movie
No. of tickets --> 2
First check whether tickets are available
Print the Cost of tickets --> 300
You need food
List of combos
Select ur combo
No. of combos
Combos value --> 500

Finally print the total amount 800

ii)Removeticket

a) Username:email address
b) OTP
c)OTP is confirmed..cancel tickets '''


class Ticketbooking():

    def Bookticket(self):

        usrname = input("enter mail id : ")

        print("Movies playing now : ")
        f = "Call me by your name"
        g = "Little woman"
        h = "Eternal sunshine of the spotless mind"
        j = "La La Land"
        k = "The fault in our stars"
        print(f)
        print(g)
        print(h)
        print(j)
        print(k)

        movname = input("enter movie name you want tickets for : ")

        if movname == f or g or h or j or k :
            print("Great !, you have selected the movie : ", movname)

            notick = int(input("enter number of tickets : "))

            x = int(notick * 300)

            avtic = 70

            print("number of tickets available are ",avtic)

            if notick < avtic:
                print("the price of the tickets are : ", x)

                print("combos available :")
                print("1.Burger combo")
                print("2.Nachos combo")
                print("3.Popcorn Combo")

                u = int(input("enter your combo number : "))

                z = int(input("How many combos do u want : "))
                y = int(z * 500)

                print("your cost for food is : ", y)

                print("Total amount to be paid is : ", x + y)
            else:
                print("Insufficient number of Tickets ! ")


        else:
            print("Incorrect movie name !")

    def Removeticket(self):

        q_usr = input("Enter email id : ")

        w = input("Are u sure u wan to cancel your tickets : ")

        if w == 'yes' :
            otp = int(input("Enter OTP : "))

            p = 7795
            if otp == p :
                print("OTP confirmed !")
                print("tickets cancelled successfully !")
            else:
                print("Incorrect OTP Try again ")

        if w == 'no' :
            print("tickets are not cancelled.")


o1 = Ticketbooking()
o1.Bookticket()
'''
o2 = Ticketbooking()

o2.Removeticket()'''

