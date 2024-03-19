def check_eligibility_tovote():
    age = int(input("Enter your age: "))
    if age>=18:
        print("You are eligible to vote")
    else:
        print("you are not eligible to vote")
check_eligibility_tovote()