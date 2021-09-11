import os



def clearScr():
    os.system('clear')

clearScr()

print( '''
_  _ ____ ____ _  _ _    _ _  _ _
|\/| |__| [__  |_/  |    | |\ | |_/
|  | |  | ___] | \_ |___ | | \| | \_
''')

print("Developed By King-Nazim And MishalMMSS")

print("")

link = input("Enter your Ngrok Link Here:")

fakelink = input("Enter Fake link Here(eg:google.com,free-follow.com,etc):")


print("Masked Link Is ready")
print("")
print(fakelink+"@"+link)
