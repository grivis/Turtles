from functools import reduce
f = open('Text2', 'r', encoding='utf8')
text = f.read()

replacedic = {',':'', '.':'', '-':' ', ';':''}

textplain = ''
for letter in text:
    ltr = replacedic.get(letter, letter)
    textplain += ltr
text = textplain

# text = text.replace(',', '')
# text = text.replace('.', '')
# text = text.replace('-', ' ')
# text = text.replace(';', '')


textwords = text.split()
textwordsnew = []


for word in textwords:
    if len(word) > 4:
        fl = word[0]
        ll = word[-1:]
        middle = word[1:-1]
        # scramble = middle[::-1]
        scramble = middle[-1:] + middle[1:-1] + middle[1]
        newword = fl + scramble + ll
    else:
        newword = word
    textwordsnew.append(newword)


newtext = ''
for word in textwordsnew:
    newtext += word + ' '

print(newtext)