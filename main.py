def password_encoder(data):
    result = ''
    for digit in data:
        new_digit = str((int(digit) + 3) % 10)
        result += new_digit
    return result
    pass


# Did the encoder, believe the decoder should just be the inverse of encoder
def password_decoder(data):
    result = ''
    for digit in data:
        decoded = str((int(digit) - 3) % 10)
        result += decoded
    return result


def main():
    while True:
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
        option = int(input("Please enter an option: "))

        if option == num1:
            encode_pass = input("Please enter your password to encode: ")
            pass_encoded = password_encoder(encode_pass)
            print("Your password has been encoded and stored!")
            pass
        elif option == num2:
            # Possible issue with print statement if passed before choosing option 1
            pass_decoded = password_decoder(pass_encoded)
            print(f"The encoded password is {pass_encoded} and the original password is {pass_decoded}.\n")
            pass
        elif option == num3:
            break
        else:
            print("Invalid menu option.")


if __name__ in '__main__':
    main()
