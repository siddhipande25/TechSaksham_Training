import random
data = ['cat','rat','net','ten','act']
score = 0
letters = list(random.choice(data))
print('your word',letters)
print(''.join(letters))
for i in range(3):
    user_word = input('enter your choice:')
    l=True

    for letter in user_word:
        if letter in letters:
            letters.remove(letter)
        else:
           l=False
    if l and user_word in data:
        score +=3
        print('correct word')
        print(f'your score is {score}')
    else:
        score -=3
        print(f'oh you lost your {score} ! Better luck nexttime')
