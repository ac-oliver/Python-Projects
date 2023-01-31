#Email Splicer

def main():
    print("Welcome to the Email Splicer: ")
    print("")

    email_input = input("Enter your email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username is: ", username)
    print("Domain is: ", domain)
    print("Extension is: ", extension)

main()

#note how it defines variables with the split method.