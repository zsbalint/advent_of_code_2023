RED = 12
GREEN = 13
BLUE = 14

file = open('input.txt', 'r')
raw_content = file.readlines()
content = {}
for item in raw_content:
    item = item.replace('\n', '')
    key = item.split(':')[0]
    key = key[5:]
    values = item.split(':')
    values.pop(0)
    values = values[0].split(';')
    all_shows = []
    for v in values:
        show_dict = {'green': '0', 'red': '0', 'blue':'0'}
        current_round = []
        current_round.append(v.split(','))
        for show in current_round[0]:
            number, color = show.lstrip().split(' ')
            show_dict[color] = number
        all_shows.append(show_dict)
    content[key] = all_shows

##### PART A #####
# sum = 0

# for key, value in content.items():
#     correct = True
#     for showing in value:
#         if int(showing['red']) > RED or int(showing['green']) > GREEN or int(showing['blue']) > BLUE:
#             correct = False
#     if correct:
#         sum += int(key)
# print(sum)

##### PART B #####
power_sum = 0

for key, value in content.items():
    red, blue, green = 0, 0, 0
    for showing in value:
        if int(showing['red']) > red:
            red = int(showing['red'])
        if int(showing['green']) > green:
            green = int(showing['green'])
        if int(showing['blue']) > blue:
            blue = int(showing['blue'])
    power_sum += red*blue*green   

print(power_sum)