# შექმენით calculator ფუნქცია რომელსაც ექნება ყველა მათემატიკური მოქმედება მაგალითად: +,-,*,/. ფუნქციას გადაეცით 3 არგუმენტი. პირველი იქნება პირველი რიცხვი, მეორე მეორე რიცხვი და მესამე მათემატიკური ოპერაციის ოპერატორი (+,-...).

def math_genious():
        user_choise = input("enter what do you want to do with CALCULATOR: ")
        if user_choise == "multiply":
            def math():
                num = int(input("enter any number : "))
                num1 = int(input("enter any number : "))
                print(num)
                print("*")
                print(num1)
        
                print("is:")
                print(num * num1)
            math()
        elif user_choise == "plus":
            def math():
                num2 = int(input("enter any number : "))
                num3 = int(input("enter any number : "))
                print(num2)
                print("+")
                print(num3)
        
                print("is:")
                print(num2 + num3)
            math()
        elif user_choise == "divide":
            def math():
                num4 = int(input("enter any number : "))
                num5 = int(input("enter any number : "))
                print(num4)
                print("/")
                print(num5)
            
                print("is:")
                print(num4 / num5)
            math()
        elif user_choise == "minus":
            def math():
                num6 = int(input("enter any number : "))
                num7 = int(input("enter any number : "))
                print(num6)
                print("-")
                print(num7)
            
                print("is:")
                print(num6 - num7)
            math()
math_genious()
