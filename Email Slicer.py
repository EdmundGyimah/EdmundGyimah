#Slicing the email to username, domain and extension
#Collect email from user
#Split the email using the "@", the first part is the username, the second part is saved as domain.
#Split the domain using ".", the first part is the domain name, the second part becomes the extension


def main():
    print("Welcome to the email slicer")
    print("")

    email_input = input("Input your email address: ")
    (username, domain)= email_input.split("@")
    (domain, extension)= domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)

while True:
    main()

