"""Read a file as text."""


def main():
    with open('ex_01.text', 'r') as fin:
        filedata = fin.readlines()

    input("\nPress Enter to see data type")
    print(type(filedata))

    input("\nPress Enter to see list data")
    print(filedata)

    input("\nPress Enter to see first item in filedata")
    print(filedata[0].rstrip())

    input("\nPress Enter to see last item in filedata")
    print(filedata[-1].rstrip())

    input("\nPress Enter to exclude first item in filedata")
    print(filedata[1:])

    input("\nPress Enter to print each item in filedata")
    for item in filedata:
        print(item.rstrip())

    input("\nPress Enter to print each item in filedata using format")
    for index, value in enumerate(filedata):
        print("Line {}: {}".format(index, value.rstrip()))

    input("\nPress Enter to print each item in filedata using f-strings")
    for index, value in enumerate(filedata):
        print(f"Line {index}: {value.rstrip()}")


if __name__ == "__main__":
    main()
