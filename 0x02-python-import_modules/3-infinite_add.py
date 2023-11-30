#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    result = 0
    for i in sys.argv[1:]:
        try:
            result += int(i)
        except ValueError:
            print("Skipping non-integer argument: {}".format(i))

    print("Result: {}".format(result))

