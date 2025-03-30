import json
import os
import glob

folder_path = "data/"

#blacklist = ['I Shall Exterminate Everything Around Me That Restricts Me from Being the Master', 'CBYW', "1898–99 Michigan State Normal Normalites men's basketball team", 'OASIS International Hospital', '1905 in the United States', 'I Shall Exterminate Everything Around Me That Restricts Me from Being the Master', 'Yvonne Wartiainen', 'Typewriter (TV series)', '416th', "Ne'er-do-well", 'Owney (dog)', 'Toastmaster (disambiguation)', '10β,17β-Dihydroxyestra-1,4-dien-3-one', 'Łubienko', 'Jack Hedley (disambiguation)', 'Oh How We Danced', 'NAACP Image Award for Outstanding Television Movie, Mini-Series or Dramatic Special', 'Listing Rules', 'List of English cardinals', 'Nabis reuteri', 'École secondaire publique Mille-Îles', 'Haraucourt-sur-Seille', 'Sudden Impact (disambiguation)', 'Antsiferovskaya, Ust-Kubinsky District, Vologda Oblast', '641', 'Royal Brompton and Harefield NHS Foundation Trust', 'J. S. S. Malelu', 'C3H5NO4', 'CY-1', '1953 Kategoria e Parë', 'Kura, Iran', "List of college sports teams in the United States with different nicknames for men's and women's teams", 'Human-based computation game', 'Carrow Road', '1892–93 Stoke F.C. season', "2014 Central American and Caribbean Games Women's Football Squads", 'CV8', 'How to Cook Everything', 'Laminate (band)', 'Venom (Marvel Comics character)', 'List of Marathi films of 1947', 'Lao silk', 'N100', 'Catharism', '125 High Speed Mode', 'Special Tribunal for Lebanon', 'WGI', 'Nobel Committee for Chemistry', 'List of Bienes de Interés Cultural in the Province of Santa Cruz de Tenerife', 'College and university rankings in the United States']

blacklist = []

titles = []
# Iterate over all files in the folder
for file_path in glob.glob(os.path.join(folder_path, "*")):  # Adjust pattern if needed (e.g., "*.txt" for only text files)
    if os.path.isfile(file_path):  # Ensure it's a file, not a directory
        with open(file_path, 'r', encoding='utf-8') as file:
            first_line = file.readline()
            titles.append(first_line[:-1])

f = open("answers.json", "r")

data = json.load(f)

n = len(data)
av = 0
sc = []

blocked = []
for i in range(n):
    bl = False
    for x in data[i]:
        if x in blacklist:
            bl = True
            break
    blocked.append(bl)
    if not bl:
        print(data[i])


for i in range(n):
    for j in range(i+1, n):
        if blocked[i] or blocked[j]: 
            continue
        s = 0
        for x in data[i]:
            if x not in titles:
                print(x, "not in titles!")
            if x in data[j]:
                s += 1
        av += s
        sc.append(s)
        #print(s, i, j, data[i], data[j])
        if(s == 10):
            print(data[i])

av /= n*(n-1)/2

sc.sort()

print(sc)
print(sc[-1])
print(sc[len(sc)//2])
print(av)

print("\n\n")