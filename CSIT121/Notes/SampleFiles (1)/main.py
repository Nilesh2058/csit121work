def digit_count(n):
    #function that counts how many digits
    if n < 10:
        return 1
    else:
        return 1 + digit_count(n // 10)

if __name__ == '__main__':
    again="Y"
    while again=="Y":
        num = int(input("I will count digits magically! Enter a number: "))
        digit = digit_count(num)
        print(num, "has", digit, "digits!")
        again=input("Again? Enter Y or N: ")
