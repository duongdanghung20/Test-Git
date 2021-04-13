#! /usr/bin/python

if __name__ == '__main__':
    f = open('Git Push Test.txt', 'r')
    l1 = f.readline()
    l2 = f.readline()
    print(f"Line 1 of GPT: {l1}" + f"Line 2 of GPT: {l2}")
    f.close()
    l3 = "This line is added to test Python write"
    f = open('Git Push Test.txt', 'w')
    f.write(l1)
    f.write(l2)
    f.write(l3)
    f.close()
