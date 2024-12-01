# შექმენით რაიმე list'ი და for loopის მეშვეობით გამოთვალეთ რამდენია მასში მყოფი რიცხვების ჯამი.

arr = [0, 1, 2, 3]
number = 0
for i in range(len(arr)):
    number += arr[i]
print(number)