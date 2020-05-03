def reverse (sentence):
    words = sentence.split()
    words.reverse()
    return ' '.join(words)

if __name__ == "__main__":
    print(reverse ("She sells sea shells"))