#finding nth occurance of a substring
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

#knapsack-approach
def fantasyknapsack(fantasyknapsack_limit, player_values, player_points, player_names, n):
    arr = [[0 for x in range( fantasyknapsack_limit + 1 )] for x in range( n + 1 )]
    name_list = [['' for x in range( fantasyknapsack_limit + 1 )] for x in range( n + 1 )]
    count = 0

    for i in range(n+1):
        for weight in range( fantasyknapsack_limit + 1 ):
            if i == 0 or weight == 0:
                arr[i][weight] = 0
            elif player_values[i-1] <= weight:
                arr[i][weight] = max(player_points[i-1]+arr[i-1][weight-player_values[i-1]], arr[i-1][weight])
                count +=1
                if (player_points[i-1]+arr[i-1][weight-player_values[i-1]]) > (arr[i-1][weight]):
                    name_list[i][weight] = player_names[i-1]+ '\n' + name_list[i-1][weight-player_values[i-1]]
                else:
                    name_list[i][weight] = name_list[i-1][weight]
            else:
                arr[i][weight] = arr [i-1][weight]

    return arr[n][fantasyknapsack_limit],name_list[n][fantasyknapsack_limit]


fname = input('Enter the file name (write \'players.txt\'): ')
if len(fname) < 1 : fname = "players.txt" 

fhandle = open(fname)

player_points = list()
player_values = list()
player_names = list()

#Taking data from .txt file
for i in fhandle:
    if not i.startswith('Name :'):
        continue
    i.rstrip()
    line_splitted = i.split()
    points_start = i.find('Points :')
    points_end = i.find('pt')
    value_start = i.find('Value :')
    value_end = i.find('mil')
    name_start = i.find('Name :')
    name_end = i.find('|')
    player_points.append(int(i[points_start+9:points_end].strip())) #treated as item value in knapsack
    player_values.append(int(i[value_start+8:value_end].strip()))   #treated as item weightight in knapsack
    player_names.append(i[name_start+7:name_end].strip())

#Taking general inputs
fantasyknapsack_limit = input('Enter The Max Player Value LIMIT (default 200) : ')
if len(fantasyknapsack_limit) < 1 : fantasyknapsack_limit=200 #just to be sure
else: fantasyknapsack_limit=int(fantasyknapsack_limit)

n = len(player_names)
res = fantasyknapsack(fantasyknapsack_limit, player_values, player_points, player_names, n)
final_points = res[0]
names = res[1]
p_no = names.count('\n')

#error handle [if max player value is low]
if(p_no <11):
    print('\nYour list has only',names.count('\n')-1, 'plyers Increase the Max Player Value LIMIT to get 11 Player ')
    print('\n\nFinal Point :', final_points)
    print('Final Player List - \n')
    print(names)
    quit()

p_find = find_nth(names,'\n',p_no-12)
final_list = names[p_find:].strip()

print('\n\nFinal Point :', final_points)
print('Final Player List - \n')
print(final_list)