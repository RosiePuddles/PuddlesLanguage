text = input().split(', ')
for i in range(len(text)):
    print(f'self.{text[i]} = {text[i]}')
