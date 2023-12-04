array = []
totaal = 0
#open de file en lees er door heen
with open("D:\Github\Advent_of_code_2023\Dag1\Input.txt", "r") as file:
    array = file.readlines()
    
number_mapping = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

for i in array:
    for number_word, digit in number_mapping.items():
        while number_word in i:
            number_index = i.find(number_word) +1
            i = i[:number_index] + digit + i[number_index + len(number_word) - 2:]

    current = ''.join(j for j in i if j.isdigit())
    totaal += int(current[0] + current[-1])
print (totaal)