def main():
    # Declaring var
    num1 = 1
    num2 = 2
    num3 = 3

    # Print menu
    print("Menu")
    print("-------------")
    print(f"{num1}. Encode")
    print(f"{num2}. Decode")
    print(f"{num3}. Quit\n")

    # Get user input
    option = input("Please enter an option: ")

    if option == num1:
        encode_pass = input("Please enter your password to encode")
        pass
    elif option == num2:
        decode_pass = input("The encoded password is {}, and the original password is {}.\n")
        pass
    elif option == num3:
        quit()


    # this is my first GitHub addition

    print("hello world")


if __name__ == '__main__':
    main()
