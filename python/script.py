file = open('temp.txt', 'r')
text = file.read()
file.close()

text = text.replace(' ', '').split('\n')[:-1]
array = map(lambda x: int(x), text)
print array
