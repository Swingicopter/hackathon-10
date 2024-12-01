# "შექმენით number guess თამაში. 
# description: შექმენით ცვლადი და მიანიჭეთ რაიმე int მნიშვნელობა. შექმენით მეორე ცვლადი რომელშიც მომხმარებელს შემოატანინებთ რაიმე რიცხვს. სანამ არ გამოიცნობს რა რიცხვი იყო პირველ ცვლადში, 
# დაუწერეთ: ""Try again"" თუ გამოიცნობს მაშინ: ""Congrats. You guessed the number"". (გამოიყენეთ while loop'ი)"

numberichose = 87
playerguess = int(input('(Hint: It is from 1 to 100) Type what you think is the number I chose: '))

while playerguess != numberichose:
    playerguess = int(input('Try again: '))

    
print('You guessed it right.')