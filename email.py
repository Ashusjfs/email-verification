# email=input("Please enter your email address: ")
# if len(email) <= 6:
#     print("Email length must be at least 7 characters.")
# else:
#     print("Email accepted.")
# if email[0].isalpha()==False:
#     print("1st letter of email must be an alphabet.")
# else:
#     print("Thank you for providing a valid email address.")
# if (email.count("@")==1):
#     print("This is a valid email address.")
# else: print("Email must contain exactly one '@' symbol.")
# if email[-5] == "." and email[-4] == ".":
#     print("Two dots are not allowed in the email address.")
# else: print("Used single dot, so this email is correct")
# if ".." in email: 
#     print("Two consecutive dots are not allowed")
# else: print("No consecutive dots found, email is valid.")

# for i in email: 
#     if i.isspace()==True:
#         print("Spaces are not allowed in the email address.")
#         break
# else: print("No spaces found, email is valid.")
# if email.islower()==False:
#         print("All characters in the email address must be lowercase.")
                                          
# else: print("All characters are lowercase, email is valid.")
# for i in email:
#     if not (i.isalpha() or i.isdigit() or i in "@._"):
#         print("Email contains invalid characters.")
# else: print("Email contains valid characters.")



#Refactored code with functions and improved structure

#1st rule
email = input("Please enter your email address: ")
is_valid = True

#2nd rule
if len(email) <=6:
    print("Email must contain at least 7 characters.")
    is_valid = False

#3rd rule
if not email[0].isalpha():
    print("1st letter of email address must be an alphabet.")
    is_valid = False

#4 rule
if email.count("@") != 1: 
    print("Email must contain exactly one '@' symbol")
    is_valid = False

#5 rule
if ".." in email:
    print("Two consecutive dots are not allowed in a single email address")
    is_valid = False

#6 rule
if " " in email:
    print("No spaces are allowed")
    is_valid = False

#7 rule
if not email.islower() == True:
    print("Email must be in lowercase letters")
    is_valid = False

#8 rule
for i in email:
    if not (i.isalpha() or i.isdigit() or i in "_@."):
        print("Only letters, digits and '_', '@' ,'.' are allowed" )
        is_valid = False
        break

    if is_valid:
        print("Valid email address")
    else: 
        print ("Invalid email address")