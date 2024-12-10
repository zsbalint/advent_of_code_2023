import re

digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

file = open('input.txt', 'r')
raw_content = file.readlines()
content = []
for item in raw_content:   
    content.append(item.replace('\n', ''))


changed_content = []

for row in content:
    # az első "szám" megkeresése:
    indices_found = []
    result = ''
    # betűvel írva
    for i in range(len(digits)):
        texts_found = [m.start() for m in re.finditer(digits[i], row)]
        if len(texts_found) > 0:
            for i in range(len(texts_found)):
                indices_found.append(texts_found[i])
    # számmal írva
    for i in range(len(row)):
        if row[i].isdigit():
            indices_found.append(i)
    
    print(row)
    print(indices_found)

    if len(indices_found) == 0:
        changed_content.append(row)
    else:
        min_index = min(indices_found)
        max_index = max(indices_found)
        if row[min_index].isdigit():
            result += row[min_index]
        else:
            for i in range(len(digits)):
                if row[min_index:min_index+len(digits[i])] == digits[i]:
                    result += str(i+1)
        if row[max_index].isdigit():
            result += row[max_index]
        else:
            for i in range(len(digits)):
                if row[max_index:max_index+len(digits[i])] == digits[i]:
                    result += str(i+1)

            
        changed_content.append(result)


print(changed_content)

sum = 0
for row in changed_content:
    numbers = re.findall("\d", row)
    result = numbers[0] + numbers[-1]
    print(numbers,result)
    sum += int(result)

print(sum)