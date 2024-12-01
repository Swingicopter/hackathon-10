# შექმენით ფუნქცია რომელსაც გადაეცემა რაიმე string და დააბრუნეთ ეს string uppercase'ში

def string(str1):
    ls1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "j", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    ls2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ls3 = []
    str2 = str1.lower
    for i in str1:
        ls3.append(ls1[ls2.index(i)])
    return "".join(ls3)

print(string("hello"))