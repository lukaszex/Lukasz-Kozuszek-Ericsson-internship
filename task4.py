def checkPalindrome (string):
    string = string.lower()
    string = string.replace(" ", "")
    for i in range(int(len(string) / 2)):
        if string[i] != string[-(i + 1)]:
            return False
        else:
            continue
    return True

if __name__ == "__main__":
    print(checkPalindrome("abCcc ba"))
