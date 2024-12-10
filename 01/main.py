file = open('input.txt', 'r')
raw_content = file.readlines()
content = []
# sorvégjelek törlése
for item in raw_content:
    content.append(item.replace("\n", ""))


print(content)