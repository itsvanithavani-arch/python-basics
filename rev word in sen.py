text="I LOVE LORD SHIVA"
words=text.split()
rev=""
for word in words:
    rev=word[::-1]+""+rev
print(rev)    
