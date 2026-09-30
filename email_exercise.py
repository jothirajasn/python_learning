import sys 

first_name = sys.argv[1]
last_name = sys.argv[2]

email= first_name.lower().replace(" ", ".") + last_name + "@gmail.com"

print("\n--- Your profile ----")
print("Full Name :", first_name+last_name)
print("Generated Email :", email)
