f = open('TheText', 'r', encoding='utf8')
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
#print(textwords)
textwordsnew = []


for word in textwords:
    fl = word[0]
    ll = word[-1:]
    middle = word[1:-1]
    #print(fl, middle, ll)
    scramble = middle[::-1]
    #print(fl, scramble, ll)
    newword = fl + scramble + ll
    #print(newword)
    textwordsnew.append(newword)


#print(textwordsnew)
newtext = ''
for word in textwordsnew:
    newtext += word + ' '

print(newtext)