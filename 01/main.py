import re

file = open('input.txt', 'r')
raw_content = file.readlines()
content = []
# sorvégjelek törlése
for item in raw_content:
    content.append(item.replace("\n", ""))
sum = 0
for row in content:
    numbers = re.findall("\d", row)
    result = numbers[0] + numbers[-1]
    sum += int(result)

print(sum)