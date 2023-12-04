array = []
totaal = 0

#open de file en lees er door heen
with open("D:\Github\Advent_of_code_2023\Dag1\Input.txt", "r") as file:
    array = file.readlines()
    
# alle letters uit de string halen
for i in array:
    current = ''.join(j for j in i if j.isdigit())
    totaal += int(current[0] + current[-1])
print (totaal)
