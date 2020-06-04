def displayPathtoPrincess(n,grid):
    pos_col = {}
    pos_row = {}
    not_find = True

    for i in range(n):
        line = len(grid[i])
        for j in range(line):
            if grid[i][j] == 'm':
                pos_row['m'] = i
                pos_col['m'] = j
            elif grid[i][j] == 'p':
                pos_row['p'] = i
                pos_col['p'] = j

    while (not_find):
        if pos_row['m'] < pos_row['p']:
            pos_row['m'] = pos_row['m'] + 1
            print ('DOWN')
        elif pos_row['m'] > pos_row['p']:
            pos_row['m'] = pos_row['m'] - 1
            print ('UP')

        if pos_col['m'] < pos_col['p']:
            pos_col['m'] = pos_col['m'] + 1
            print ('RIGHT')
        elif pos_col['m'] > pos_col['p']:
            pos_col['m'] = pos_col['m'] - 1
            print ('LEFT')

        if pos_col['m'] == pos_col['p'] and pos_row['m'] == pos_row['m']:
            not_find = False

#print all the moves here
m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
