def countDigits (number):
    number = str(number)
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    result = 0
    for digit in digits:
        if digit in number:
            result += 1
    return result

if __name__ == "__main__":
    print(countDigits(55000))