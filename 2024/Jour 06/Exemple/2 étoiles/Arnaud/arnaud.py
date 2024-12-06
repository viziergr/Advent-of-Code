# Variables
fichier_emp = '2024/Jour 06/Exemple/2 étoiles/Arnaud/input.txt'
data = []
dep_count = []
in_b = True
direction = ''

ordre = []


# Lecture du fichier
def get_data():
    input = []
    with open(fichier_emp, 'r') as fichier:
        for ligne in fichier :
            tab = []
            for char in ligne.strip() :
                tab.append(char)
            input.append(tab)
    return input

def trouver_pos_dir(tab) :
    for i, ligne in enumerate(tab):
        for j, val in enumerate(ligne):
            if val == '^' :
                return i, j, 'up'
            elif val == '>' :
                return i, j, 'right'
            elif val == 'v' :
                return i, j, 'down'
            elif val == '<' :
                return i, j, 'left'
            
def next_action(tab, i, j, dir) :
    if dir == "up" and i-1 >= 0:
        if tab[i-1][j] == '#' :
            tab[i][j] = '>'
            return tab, False, "right"
        else : 
            return tab, True, "up"
    elif dir == "right" and j+1 < len(tab[i]) :
        if tab[i][j+1] == '#' :
            tab[i][j] = 'v'
            return tab, False, "down"
        else : 
            return tab, True, "right"
    elif dir == "down" and i+1 < len(tab) :
        if tab[i+1][j] == '#' :
            tab[i][j] = '<'
            return tab, False, "left"
        else : 
            return tab, True, "down"
    elif dir == "left" and j-1 >= 0:
        if tab[i][j-1] == '#' :
            tab[i][j] = '^'
            return tab,False, "up"
        else : 
            return tab, True, "left"
    else :
        return tab, False, "end"
    
def avancer(tab, i , j, dir) :
    if dir == 'up' :
        tab[i][j] = '.'
        tab[i-1][j] = '^'
    elif dir == 'right' :
        tab[i][j] = '.'
        tab[i][j+1] = '>'
    elif dir == 'down' :
        tab[i][j] = '.'
        tab[i+1][j] = 'v'
    elif dir == 'left':
        tab[i][j] = '.'
        tab[i][j-1] = '<'
    return tab

def score_count(tab) :
    total = 0
    for ligne in tab:
        for val in ligne:
            total += val
    return total

# Main

data = get_data()
print(data)
dep_count = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]
print (dep_count)
count = 0
while  direction != 'end':
    count +=1
    y, x, direction = trouver_pos_dir(data)
    dep_count[y][x] = 1
    data, avancer_b, direction = next_action(data, y, x, direction)
    if avancer_b :
        data = avancer(data, y, x, direction)
        if [y,x] not in ordre :
            ordre.append([y,x])
        
score = score_count(dep_count)

#Suite du pb

ordre.pop(0)
ordre.append([121, 0])
# ordre.append([0, 101])
# ordre.append([9, 7])
print(ordre)
print(len(ordre), ordre[0])

nb_caisse = 0
for couple in ordre :
    modif_data = get_data()
    modif_data[couple[0]][couple[1]] = '#'

    direction = 'up'
    count = 0
    while  direction != 'end':
        count += 1
        y, x, direction = trouver_pos_dir(modif_data)
        modif_data, avancer_b, direction = next_action(modif_data, y, x, direction)
        if avancer_b :
            modif_data = avancer(modif_data, y, x, direction)
        if count > 10000 :
            print(couple)
            nb_caisse += 1
            direction = 'end'
            
# Résultat
print('score :',score,' nb caisse :', nb_caisse)



