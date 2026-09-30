name="Raja"
password="Raja123"

u_name=input("Enter Username : ")
u_password=input("Enter user password : ")


def validate_Credientials():
    if name==u_name and password==u_password:
        return "TRUE"
    else:
        return "false"



print(validate_Credientials())
